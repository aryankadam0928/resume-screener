# 🧠 AI Resume Screener

A smart, AI-powered resume screening web app that helps recruiters quickly evaluate candidates based on job descriptions using Natural Language Processing (NLP) and BERT embeddings.

## 🚀 Features

- 📄 Upload multiple resumes (PDF or DOCX)
- 📝 Paste any job description
- 🤖 Match resumes using Sentence-BERT and cosine similarity
- 📊 View candidate match scores in a table
- 📥 Download screening results as CSV
- 🧪 Fast, lightweight, and effective — ideal for hiring and hackathons!

---

## 🧰 Tech Stack

- **Frontend/Backend**: [Streamlit](https://streamlit.io/)
- **ML Model**: [Sentence-BERT](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
- **Parsing Tools**: PyPDF2, docx2txt
- **Similarity Metric**: Cosine Similarity from Scikit-learn

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/aryankadam0928/resume-screener.git
cd resume-screener

# (Optional) Create a virtual environment
python -m venv venv
# Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install the required libraries
pip install -r requirements.txt
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
Then open your browser and go to http://localhost:8501
```


## 📄 Sample Job Description
Paste this in the app for testing:
We are seeking a passionate Machine Learning Engineer with experience in Python, TensorFlow, and deep learning. The ideal candidate will have hands-on knowledge of CNNs, NLP, and data preprocessing. Experience with Git, cloud tools, and real-world ML projects is a plus.


## 💬 Let's Connect!
Aryan Kadam
📧 aryankadam@gmail.com
🌐 https://www.linkedin.com/in/aryan-kadam-582a482a8

