# 🧠 Resume Screening & Matching AI

## 📌 Overview
This project is an AI-powered Resume Screening and Matching System built using **Python, NLP, and Machine Learning**.

It allows users to input a **job description** and automatically finds the most relevant resumes using **TF-IDF vectorization** and **cosine similarity**.

---

## 🚀 Features
- Extracts text from PDF resumes
- Cleans and preprocesses text
- Lemmatization using spaCy
- TF-IDF vectorization
- Resume-job matching using cosine similarity
- Pie chart visualization using Matplotlib
- Interactive UI using Streamlit

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
# 🧠 Resume Screening & Matching AI

## 📌 Overview
This project is an AI-powered Resume Screening and Matching System built using **Python, NLP, and Machine Learning**.

It allows users to input a **job description** and automatically finds the most relevant resumes using **TF-IDF vectorization** and **cosine similarity**.

---

## 🚀 Features
- Extracts text from PDF resumes
- Cleans and preprocesses text
- Lemmatization using spaCy
- TF-IDF vectorization
- Resume-job matching using cosine similarity
- Pie chart visualization using Matplotlib
- Interactive UI using Streamlit

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
Resume-Screening-and-Matching-AI/
│
├── data/
│ ├── Accountant/
│ ├── Data_Scientist/
│ └── ...
│
├── app.py
├── model.py
├── preprocessing.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── (generated files - ignored)
├── processed_resumes.csv
├── vectorizer.pkl
└── tfidf_matrix.pkl

---

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/Tanvianejaa/Resume-Screening-and-Matching-AI.git
cd Resume-Screening-and-Matching-AI


### 2. Install dependencies
pip install -r requirements.txt

### 3. Install spaCy model
python -m spacy download en_core_web_sm

---

## ▶️ Usage

Run the Streamlit app:
streamlit run app.py


---

## 💼 How It Works

1. Loads resumes from dataset (PDFs)
2. Cleans text (removes symbols, lowercase)
3. Lemmatizes text using spaCy
4. Converts text into TF-IDF vectors
5. Matches job description using cosine similarity
6. Ranks resumes based on similarity score

---

## 📊 Output

- Best matching resume with confidence score
- Top 10 matching resumes
- Pie chart visualization

---

## ⚡ Note

Preprocessed dataset (`processed_resumes.csv`) is included for faster execution.

---

## 👩‍💻 Author

Tanvi Aneja