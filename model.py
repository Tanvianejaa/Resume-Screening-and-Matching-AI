from sklearn.metrics.pairwise import cosine_similarity

def match_job_description(job_desc_text, df, vectorizer, tfidf_matrix, top_n=10):
    """
    Match a job description to resumes and return top N resumes.
    """
    # Convert job description to TF-IDF vector
    job_vec = vectorizer.transform([job_desc_text])
    # Compute cosine similarity with all resumes
    sims = cosine_similarity(job_vec, tfidf_matrix).flatten()
    df["similarity"] = sims
    # Sort top N resumes
    top_matches = df.sort_values(by="similarity", ascending=False).head(top_n)
    return top_matches
