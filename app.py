import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from preprocessing import load_or_build_data, clean_text, lemmatize_text
from model import match_job_description

# -----------------------------
# Streamlit Config
# -----------------------------
st.set_page_config(page_title="Resume Screening AI", page_icon="🧠", layout="wide")

st.markdown("""
<style>
.stApp {background-color: #f5f5f5;}
h1 {color: #1f77b4;}
h2 {color: #ff7f0e;}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Resume Screening & Matching AI")
st.markdown("""
Upload or paste a **job description** to find the most suitable resumes from your dataset.
""")

# -----------------------------
# Load Dataset
# -----------------------------
with st.spinner("Loading resumes dataset..."):
    df, vectorizer, tfidf_matrix = load_or_build_data("data")
st.success(f"✅ Loaded {len(df)} resumes across {df['category'].nunique()} categories!")

# -----------------------------
# Job Description Input
# -----------------------------
st.subheader("💼 Enter Job Description")
job_desc = st.text_area(
    "Paste the job description here:",
    height=200,
    placeholder="Example: We are looking for an experienced accountant familiar with Tally ERP, GST filings, and financial reporting..."
)

# -----------------------------
# Matching
# -----------------------------
if st.button("🔍 Find Matching Resumes") and job_desc.strip():
    with st.spinner("Analyzing and ranking resumes..."):
        # Preprocess job description
        job_text = lemmatize_text(clean_text(job_desc))
        # Match all resumes
        top_matches = match_job_description(job_text, df, vectorizer, tfidf_matrix, top_n=len(df))

    st.success("✅ Matching complete!")

    # -----------------------------
    # Pie Chart for Top 10
    # -----------------------------
    st.subheader("📊 Top 10 Resume Similarity Pie Chart")
    top10 = top_matches.head(10)
    fig, ax = plt.subplots(figsize=(6,6))
    sizes = top10["similarity"] * 100
    labels = top10["filename"]
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=plt.cm.tab20.colors)
    ax.axis('equal')
    st.pyplot(fig)

    # -----------------------------
    # Summary of Top Resume
    # -----------------------------
    best_resume = top_matches.iloc[0]
    st.subheader("🏆 Best Matching Resume")
    st.markdown(f"**Filename:** {best_resume['filename']}")
    st.markdown(f"**Category:** {best_resume['category']}")
    st.markdown(f"**Confidence:** {best_resume['similarity']*100:.2f}%")

    # -----------------------------
    # Top 10 Table
    # -----------------------------
    st.subheader("📄 Top 10 Matching Resumes")
    st.table(
        top10[["filename", "category", "similarity"]].assign(
            similarity=lambda x: (x["similarity"]*100).round(2)
        ).reset_index(drop=True)
    )

else:
    st.info("👆 Enter a job description above and click **Find Matching Resumes** to start.")


#streamlit run app.py