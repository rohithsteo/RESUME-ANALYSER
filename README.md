# 🤖 AI Resume Analyzer + Skill Gap Detector

A Python-based tool that analyzes resumes and identifies missing skills based on a target job role.

---

## 🧠 Overview

This project takes a resume (either as text or PDF), extracts relevant skills, and compares them with predefined job requirements to identify skill gaps.

It helps users understand what skills they need to improve for a specific role.

---

## ⚙️ Features

- Resume input via text or PDF
- Skill extraction using text processing
- Comparison with job role requirements
- Displays matched and missing skills
- Simple and interactive CLI interface

---

## 🛠️ Tech Stack

- Python
- PyPDF2 (for PDF reading)
- Basic NLP using regex

---

## 📂 Project Structure

main.py              # Main program  
requirements.txt     # Dependencies  
README.md            # Project documentation  

---

## 🚀 How to Run

1. Install dependencies  
pip install -r requirements.txt  

2. Run the program  
python main.py  

---

## 📥 How It Works

1. User selects input method (PDF or text)  
2. Resume content is processed and cleaned  
3. Skills are extracted from the text  
4. Compared with predefined job roles  
5. Output shows:
   - Skills found
   - Missing skills  

---

## 🧠 Example

Input:  
Resume: "I know python, pandas and numpy"  
Role: data scientist  

Output:  
Skills Found: {'python', 'pandas', 'numpy'}  
Missing Skills: {'machine learning', 'sql', 'statistics'}  

---

## 📌 Future Improvements

- Better NLP using TF-IDF or embeddings  
- Support for real job descriptions  
- Web interface using Streamlit  
- Skill scoring system  

---

## 👨‍💻 Author

Rohith Raj  

---

## ⭐ If you like this project, consider starring the repo!
