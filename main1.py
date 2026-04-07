import re
from PyPDF2 import PdfReader

# predefined skill database
JOB_SKILLS = {
    "data scientist": ["python", "machine learning", "pandas", "numpy", "statistics", "sql"],
    "web developer": ["html", "css", "javascript", "react", "node", "mongodb"],
    "software engineer": ["python", "java", "c++", "data structures", "algorithms"]
}

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return set(words)

def analyze_resume(resume_text, role):
    extracted = extract_skills(resume_text)
    required = set(JOB_SKILLS.get(role.lower(), []))

    matched = extracted.intersection(required)
    missing = required - extracted

    return matched, missing

def main():
    print("=== AI Resume Analyzer ===")
    
    choice = input("Enter 1 for PDF or 2 for text input: ")

    if choice == "1":
        path = input("Enter PDF file path: ")
        resume_text = extract_text_from_pdf(path)
    else:
        resume_text = input("Paste your resume text: ").lower()

    role = input("Enter target role (Data Scientist / Web Developer / Software Engineer): ")

    matched, missing = analyze_resume(resume_text, role)
    print("\n📊 Analysis Complete")
    print("\n✅ Skills Found:", matched)
    print("❌ Missing Skills:", missing)

if __name__ == "__main__":
    main()