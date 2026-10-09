# Project Report: Local Financial Article Classifier & Q&A Web Tool

## 1. Abstract
With the exponential growth of digital information, extracting relevant insights from web-based articles has become a necessity. This project presents a 100% free, local, and No-API Web Tool developed for analyzing articles. It combines Web Scraping, Machine Learning Text Classification, and a Local Retrieval-Augmented Generation (RAG) Question & Answer Engine. The system extracts textual content from a given URL, predicts its category using a custom-trained model, and allows users to semantically query the text locally without relying on paid external APIs.

## 2. Introduction
Modern AI applications heavily rely on paid cloud LLM endpoints (like OpenAI or Gemini) for text classification and question-answering. This project demonstrates that highly effective text analysis can be achieved deterministically on local hardware. The application is built entirely in Python using Streamlit for the frontend interface and Scikit-Learn for the machine learning backbone. 

## 3. Objectives
- **Local Execution:** To build an AI tool that runs 100% locally without external API dependencies.
- **Web Scraping:** To extract clean, readable text from any given URL.
- **Text Classification:** To classify the extracted text into predefined categories using a custom-trained Machine Learning model.
- **Semantic Q&A (RAG):** To implement a Retrieval-Augmented Generation engine that finds the most relevant passages in the text based on a user's question using TF-IDF and Cosine Similarity.
- **Interactive UI:** To provide a seamless user experience via a web-based dashboard.

## 4. System Architecture
The system architecture follows a modular, pipeline-based approach:
1. **Input:** User provides an article URL via the Streamlit UI.
2. **Extraction Module:** `trafilatura` fetches and cleans the HTML content, extracting pure text.
3. **Classification Module:** The text is passed to a pre-trained `MultinomialNB` model which predicts the article's category.
4. **Indexing Module:** The text is tokenized into sentences using NLTK. A local `TfidfVectorizer` fits the sentences to create a vector space.
5. **Q&A Module:** When a user asks a question, it is vectorized. Cosine Similarity is computed against the indexed sentences to retrieve the top 3 matches.

## 5. Modules Description

### 5.1 Model Training (`train_model.py`)
- **Dataset:** Utilizes `scikit-learn`'s `fetch_20newsgroups` dataset to simulate diverse textual categories.
- **Algorithm:** Uses a pipeline combining `TfidfVectorizer` (for text-to-numerical feature extraction) and `MultinomialNB` (Naive Bayes for classification).
- **Persistence:** The trained model pipeline and target names are serialized and saved locally as `financial_model.pkl` using `joblib`.

### 5.2 Content Extractor
- Uses the `trafilatura` library to scrape the main body text from the provided URL, automatically filtering out ads, navbars, and footers.
- Cleans whitespace and formatting anomalies using Regular Expressions.

### 5.3 Local RAG Q&A Engine
- Uses `nltk.tokenize.sent_tokenize` to split the document into distinct sentences.
- Dynamically creates a TF-IDF matrix for the specific article.
- Employs `sklearn.metrics.pairwise.cosine_similarity` to measure the semantic distance between the user's query vector and the sentence vectors, returning the highest-scoring matches with confidence metrics.

### 5.4 Streamlit Frontend (`app.py`)
- A responsive, two-column web layout.
- The **Sidebar** manages URL inputs and processing state.
- The **Left Column** displays the predicted ML category and the extracted article text.
- The **Right Column** provides the search interface for the Q&A engine and displays vector match metrics inside expandable sections.

## 6. Software Requirements
- **Operating System:** Windows, macOS, or Linux.
- **Programming Language:** Python 3.8 or higher.
- **Libraries/Packages:**
  - `streamlit` (Web framework)
  - `scikit-learn` (Machine Learning & Vectorization)
  - `trafilatura` (Web scraping)
  - `nltk` (Natural Language Processing / Tokenization)
  - `joblib` (Model serialization)
  - `numpy`, `pandas` (Data manipulation)

## 7. Conclusion
This project successfully demonstrates the feasibility of building a robust, local AI text analysis tool without relying on expensive cloud infrastructure. By combining traditional machine learning techniques (TF-IDF, Naive Bayes) with modern architectural patterns (RAG, Streamlit), the application offers an efficient, private, and deterministic solution for web content classification and semantic search.
