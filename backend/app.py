import streamlit as st
from resume_parser import (
    extract_text_from_pdf,
    extract_skills,
    calculate_similarity
)
st.markdown("""
<style>
.big-title {
    font-size:32px !important;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🚀 AI Resume & Career Optimizer</p>', unsafe_allow_html=True)

st.set_page_config(page_title="AI Resume Optimizer", layout="centered")

st.title("📄 AI Resume & Career Optimizer")
st.write("Upload your resume and paste a job description to see how well you match.")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste Job Description here", height=200)

if uploaded_file and job_description:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = extract_text_from_pdf("temp_resume.pdf")

    extracted_skills = extract_skills(resume_text)
    match_percentage = calculate_similarity(resume_text, job_description)

    st.subheader("✅ Extracted Skills")
    for skill in extracted_skills:
     st.markdown(f"- ✅ {skill}")

    st.subheader("📊 Match Percentage")
    st.progress(int(match_percentage))
    st.write(f"### {match_percentage}% Match")

    # Missing skills
    job_skills = extract_skills(job_description)
    missing_skills = list(set(job_skills) - set(extracted_skills))

    st.subheader("❌ Missing Skills")
    if missing_skills:
        st.warning(missing_skills)
    else:
        st.success("No missing skills 🎉")