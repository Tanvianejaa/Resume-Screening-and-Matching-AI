import os
import re
import joblib
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from PyPDF2 import PdfReader

# -----------------------------
# ⚙️ Setup
# -----------------------------
nlp = spacy.load("en_core_web_sm")

CACHE_DF = "processed_resumes.csv"
CACHE_VEC = "vectorizer.pkl"
CACHE_TFIDF = "tfidf_matrix.pkl"

# -----------------------------
# 🧹 Text Preprocessing
# -----------------------------
def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print(f"⚠️ Error reading {pdf_path}: {e}")
    return text

def clean_text(text):
    """Remove non-alphabetic characters and lowercase the text."""
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower().strip()

def lemmatize_text(text):
    """Lemmatize and remove stopwords using spaCy."""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

# -----------------------------
# 📂 Load Resumes
# -----------------------------
def load_resumes(data_folder):
    """Read all resumes (PDFs) from subfolders and preprocess them."""
    data = []
    for category in os.listdir(data_folder):
        category_path = os.path.join(data_folder, category)
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                if file.endswith(".pdf"):
                    pdf_path = os.path.join(category_path, file)
                    text = extract_text_from_pdf(pdf_path)
                    clean = clean_text(text)
                    lemmatized = lemmatize_text(clean)
                    data.append({
                        "filename": file,
                        "category": category,
                        "resume_text": lemmatized
                    })
    return pd.DataFrame(data)

# -----------------------------
# 🔠 TF-IDF Vectorization
# -----------------------------
def vectorize_texts(texts):
    """Convert text data into TF-IDF vectors."""
    vectorizer = TfidfVectorizer(max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(texts)
    return vectorizer, tfidf_matrix

# -----------------------------
# ⚡ Cache System
# -----------------------------
def load_or_build_data(data_folder):
    """Load cached data if available, otherwise build and cache it."""
    if (
        os.path.exists(CACHE_DF)
        and os.path.exists(CACHE_VEC)
        and os.path.exists(CACHE_TFIDF)
    ):
        print("✅ Loading cached data...")
        df = pd.read_csv(CACHE_DF)
        vectorizer = joblib.load(CACHE_VEC)
        tfidf_matrix = joblib.load(CACHE_TFIDF)
    else:
        print("🧠 Building data from scratch (first run)...")
        df = load_resumes(data_folder)
        vectorizer, tfidf_matrix = vectorize_texts(df["resume_text"])
        df.to_csv(CACHE_DF, index=False)
        joblib.dump(vectorizer, CACHE_VEC)
        joblib.dump(tfidf_matrix, CACHE_TFIDF)
    return df, vectorizer, tfidf_matrix
