import streamlit as st
import trafilatura
import joblib
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import sent_tokenize
import os

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

st.set_page_config(page_title="Local RAG & Classifier", layout="wide")

@st.cache_resource
def load_model():
    model_path = 'financial_model.pkl'
    if not os.path.exists(model_path):
        return None
    try:
        model_data = joblib.load(model_path)
        return model_data
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model_data = load_model()

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_content(url):
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        text = trafilatura.extract(downloaded)
        if text:
            return clean_text(text)
    return None

def process_qa(query, sentences):
    if not sentences:
        return []
    vectorizer = TfidfVectorizer(stop_words='english')
    corpus = sentences + [query]
    try:
        tfidf_matrix = vectorizer.fit_transform(corpus)
    except ValueError:
        return []
    
    query_vec = tfidf_matrix[-1]
    sentence_vecs = tfidf_matrix[:-1]
    
    similarities = cosine_similarity(query_vec, sentence_vecs).flatten()
    top_indices = similarities.argsort()[-3:][::-1]
    
    results = []
    for idx in top_indices:
        results.append({
            'sentence': sentences[idx],
            'score': similarities[idx]
        })
    return results

st.title("📊 Local Financial Article Classifier & Q&A Tool")
st.markdown("100% Free, Local, No-API Text Analysis Engine for MCA Project")

if model_data is None:
    st.error("Model file not found. Please run `train_model.py` to train the model first.")
    st.stop()

pipeline = model_data['pipeline']
target_names = model_data['target_names']

st.sidebar.header("Article Input")
url_input = st.sidebar.text_input("Enter Article URL:")
process_button = st.sidebar.button("Process & Index Article")

if "article_text" not in st.session_state:
    st.session_state.article_text = None
if "sentences" not in st.session_state:
    st.session_state.sentences = None
if "prediction" not in st.session_state:
    st.session_state.prediction = None

if process_button:
    if not url_input:
        st.sidebar.warning("Please enter a valid URL.")
    else:
        with st.spinner("Extracting content..."):
            text = extract_content(url_input)
            if text:
                st.session_state.article_text = text
                st.session_state.sentences = sent_tokenize(text)
                
                pred_idx = pipeline.predict([text])[0]
                st.session_state.prediction = target_names[pred_idx]
                
                st.sidebar.success("Article successfully extracted and indexed!")
            else:
                st.sidebar.error("Failed to extract content from the URL. Please verify the URL.")

col1, col2 = st.columns(2)

with col1:
    st.header("📄 Article Preview")
    if st.session_state.article_text:
        st.info(f"**Predicted Category:** {st.session_state.prediction}")
        st.text_area("Content", st.session_state.article_text, height=400)
    else:
        st.write("No article processed yet.")

with col2:
    st.header("❓ Local Q&A (RAG)")
    query = st.text_input("Ask a question about the article:")
    if st.button("Search"):
        if not query:
            st.warning("Please enter a question.")
        elif not st.session_state.sentences:
            st.warning("Please process an article first.")
        else:
            with st.spinner("Searching..."):
                results = process_qa(query, st.session_state.sentences)
                if not results:
                    st.warning("Could not find matching sentences.")
                else:
                    st.subheader("Top Matching Passages:")
                    for i, res in enumerate(results):
                        score = res['score']
                        if score > 0.0:
                            st.markdown(f"**Match #{i+1}** (Confidence: `{score:.4f}`)")
                            st.write(f"> {res['sentence']}")
                            st.divider()
                        else:
                            st.write(f"Match #{i+1}: No relevant overlap found.")
                            st.divider()
                    
                    with st.expander("Vector Match Metrics"):
                        for i, res in enumerate(results):
                            st.write(f"Sentence {i+1} Match Score: {res['score']:.4f}")
