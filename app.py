# Resume Screener Backend using Streamlit + NLP

import streamlit as st
import pandas as pd
import PyPDF2
import docx2txt
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

def get_resume_text(file):
    ext = file.name.split('.')[-1].lower()
    if ext == 'pdf':
        return extract_text_from_pdf(file)
    elif ext == 'docx':
        return extract_text_from_docx(file)
    else:
        return ""

def calculate_similarity(jd_text, resume_text):
    texts = [jd_text, resume_text]
    embeddings = model.encode(texts)
    sim_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(sim_score * 100, 2)

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("AI-Powered Resume Screener")

st.markdown("""
This tool compares uploaded resumes with the given job description (JD) and scores how well they match using advanced NLP techniques.
""")

jd_input = st.text_area("Paste the Job Description here:", height=250)

uploaded_files = st.file_uploader("Upload Resumes (PDF or DOCX):", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Screen Resumes"):
    if not jd_input:
        st.warning("Please provide a job description.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        results = []
        with st.spinner("Analyzing resumes..."):
            for file in uploaded_files:
                resume_text = get_resume_text(file)
                score = calculate_similarity(jd_input, resume_text)
                results.append({"Candidate": file.name, "Match Score (%)": score})

        df_results = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
        st.success("Screening Complete!")
        st.dataframe(df_results)

        csv = df_results.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results as CSV", data=csv, file_name="screening_results.csv", mime="text/csv")