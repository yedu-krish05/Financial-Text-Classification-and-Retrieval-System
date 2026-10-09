# Local Financial Article Classifier & Q&A Web Tool

This project is a 100% Free, Local, No-API Web Tool developed for an MCA Academic Project. It extracts article content from URLs, classifies the text using a custom Machine Learning model trained from scratch, and allows users to query the document using TF-IDF and Cosine Similarity for semantic matching (a Local RAG Engine).

## Features
- **Custom Text Classifier:** Built using `scikit-learn`'s `TfidfVectorizer` and `MultinomialNB`, trained on a subset of the 20 Newsgroups dataset (simulating categories like graphics, auto, space, and politics).
- **Web Content Extraction:** Cleanly parses article text from any valid URL using `trafilatura`.
- **Local RAG Q&A Engine:** Splits text into discrete sentences, computes vector spaces with TF-IDF, and retrieves top results using Cosine Similarity against the user's query.
- **Interactive UI:** A responsive web application built with Streamlit.

## Setup Instructions

### 1. Install Dependencies
Make sure you have Python installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Train the Model
Train the classification model to generate `financial_model.pkl`:
```bash
python train_model.py
```

### 3. Run the Web Application
Launch the Streamlit app:
```bash
streamlit run app.py
```

## Architecture Overview
- **Data Source:** Simulated document categories using scikit-learn's built-in `fetch_20newsgroups`.
- **ML Pipeline:** Raw Text → TF-IDF Vectorization → Naive Bayes Classification.
- **RAG Engine:** URL Text Extraction → Sentence Tokenization (via NLTK) → Ad-hoc TF-IDF fit → Cosine Similarity matching against Query.
"# Financial-Text-Classification-and-Retrieval-System" 
