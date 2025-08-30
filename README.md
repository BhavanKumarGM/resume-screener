# Resume Screener 📝

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-orange?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**AI-powered Resume Screening & Matching Tool**  
Simplifies resume screening by analyzing resumes against a Job Description (JD) and scoring the relevance. Useful for **recruiters** and **job seekers** alike.

---

## Features 🚀

- Upload **PDF, DOCX, or TXT** resumes or paste text directly.  
- Paste or upload **Job Description**.  
- **AI-powered scoring** using TF-IDF & cosine similarity.  
- Displays **match score**, **resume preview**, and **suggestions**.  
- Colorful, user-friendly **web interface** built with Flask.  

---

## Screenshots 🌈

*(Add screenshots of your web app here, e.g., `screenshots/homepage.png`)*

---

## Installation ⚡

1. **Clone the repository**
```bash
git clone https://github.com/BhavanKumarGM/resume-screener.git
cd resume-screener
Create a virtual environment (optional)

bash
Copy code
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Install dependencies

bash
Copy code
pip install flask==3.0.3 scikit-learn==1.5.1 PyPDF2==3.0.1 docx2txt==0.8
Run the app

bash
Copy code
python app.py
Open in browser

cpp
Copy code
http://127.0.0.1:5000
Usage 💡
Upload a resume or paste your resume text.

Paste the Job Description.

Click Analyze Resume.

See match score, resume preview, and suggestions.

Project Structure 📁
bash
Copy code
resume_screener/
│── app.py              # Main Flask app
│── utils.py            # Helper functions (file reading, scoring)
│── templates/
│    └── index.html     # HTML template (colorful UI)
│── uploads/            # Temporary folder for resumes
│── README.md           # Project documentation
Tech Stack 🛠️
Python 3.11

Flask 3.0.3 for web interface

scikit-learn (TF-IDF + cosine similarity)

PyPDF2 & docx2txt for parsing resumes

HTML/CSS for colorful UI

Future Enhancements ✨
Add OCR support for scanned PDFs.

Build a dashboard for recruiters to manage multiple resumes.

Highlight missing keywords directly in resume.

Add a progress bar for match score visualization.

Author 🧑‍💻
Bhavan Kumar GM

GitHub: BhavanKumarGM

Email: your_email@example.com

License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

yaml
Copy code

---

If you want, I can also **add a colorful GIF demo, badges for build/coverage, and a “Visit Live Demo” link** that makes your GitHub repo look like a product showcase — perfect for recruiters.  

Do you want me to do that next?







Ask ChatGPT
