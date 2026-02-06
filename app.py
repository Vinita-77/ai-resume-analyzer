import streamlit as st
from PyPdf import PdfReader
from skills import job_roles

st.title("AI Resume Analyzer")

def extract_text_from_pdf(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("Resume Analysis")

    best_role = None
    best_score = 0
    missing_skills = []

    for role, skills in job_roles.items():
        matched = [skill for skill in skills if skill in text]
        score = len(matched) / len(skills) * 100

        if score > best_score:
            best_score = score
            best_role = role
            missing_skills = list(set(skills) - set(matched))

    st.success("Analysis Complete ✅")
    st.write(f"**Recommended Job Role:** {best_role}")
    st.write(f"**Resume Match Score:** {int(best_score)}%")
    st.write("**Missing Skills:**")
    st.write(missing_skills)