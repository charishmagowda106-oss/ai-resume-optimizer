import streamlit as st
from resume_parser import extract_text, extract_skills, calculate_match

st.set_page_config(page_title="AI Resume Optimizer", layout="centered")

st.title("📄 AI Resume & Career Optimizer")
st.write("Upload your resume and paste a job description to see how well you match.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description here", height=200)

if uploaded_file and job_description:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = extract_text("temp_resume.pdf")
    extracted_skills = extract_skills(resume_text)
    match_percentage = calculate_match(resume_text, job_description)

    st.subheader("Extracted Skills")
    for skill in extracted_skills:
        st.write(skill)

    st.subheader("Match Percentage")
    st.write(f"{match_percentage}%")