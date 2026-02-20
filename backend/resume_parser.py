from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    print("Number of pages:", len(doc))

    for page in doc:
        page_text = page.get_text()
        print("Page text length:", len(page_text))
        text += page_text

    return text

import fitz

SKILL_SET = [
    "perl",
    "java",
    "c++",
    "html",
    "php",
    "mysql",
    "matlab",
    "machine learning",
    "artificial intelligence",
    "linux",
    "windows",
    "mac os"
]

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILL_SET:
        if skill in text:
            found_skills.append(skill)

    return found_skills
def calculate_similarity(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity_score[0][0] * 100, 2)

if __name__ == "__main__":
    file_path = "sample_resume.pdf"
    extracted_text = extract_text_from_pdf(file_path)

    # Skill extraction
    skills = extract_skills(extracted_text)
    print("\n--- EXTRACTED SKILLS ---\n")
    print(skills)
    # Job description (add your own)
    job_description = """
 We are looking for a Python developer with experience in
 machine learning, SQL, data analysis, communication, and teamwork.
 """

 # Calculate match percentage
    match_percentage = calculate_similarity(extracted_text, job_description)

    print("\n--- MATCH RESULTS ---\n")
    print("Match Percentage:", match_percentage, "%")

 # Extract skills from job description
    job_skills = extract_skills(job_description)

 # Find missing skills
    missing_skills = [skill for skill in job_skills if skill not in skills]

    print("Missing Skills:", missing_skills)

   