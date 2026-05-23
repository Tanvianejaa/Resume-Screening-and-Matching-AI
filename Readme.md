# 🧠 Resume Screening & Matching AI

## 📌 Overview
This project is an AI-powered Resume Screening and Matching System built using **Python, NLP, and Machine Learning**.  

It allows users to input a **job description** and automatically finds the most relevant resumes from a dataset using **TF-IDF vectorization** and **cosine similarity**.

---

## 🚀 Features
- 📂 Extracts text from PDF resumes
- 🧹 Cleans and preprocesses text (regex + NLP)
- 🔤 Lemmatization using spaCy
- 📊 TF-IDF vectorization
- 🤖 Resume-job matching using cosine similarity
- 📈 Visual representation (pie chart of top matches)
- 🖥️ Interactive UI using Streamlit

---

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- spaCy
- Streamlit
- Matplotlib
- PyPDF2
- Joblib

---

## 📂 Project Structure
project-folder/
│── data/ # Resume dataset (PDFs in category folders)
│── app.py # Streamlit frontend
│── model.py # Matching logic (cosine similarity)
│── preprocessing.py # Data loading & NLP preprocessing
│── processed_resumes.csv # Cached processed data
│── vectorizer.pkl # Saved TF-IDF vectorizer
│── tfidf_matrix.pkl # Saved TF-IDF matrix
│── README.md
---

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Resume-Screening-and-Matching-AI.git

