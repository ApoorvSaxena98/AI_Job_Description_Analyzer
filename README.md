# 🧠 AI Job Description Analyzer
A simple Streamlit-based web app that uses GPT-4 or GPT-3.5-turbo to determine whether a resume and job description match the requirements of the position, and it offers recommendations for improvement. Ideal for job seekers and HR professionals.

---

**🛠️ Built With**
- Python
- Streamlit
- OpenAI GPT-4/GPT-3.5-turbo

---

## 📁 Project Structure
AI-Job-Description-Analyzer/
├── app.py # Main Streamlit application
├── prompts.py # Prompt builder for GPT input
├── requirements.txt # Project dependencies
├── streamlit/ # 🔁 Rename to ".streamlit" (see note below)
│ └── secrets.toml # OpenAI API key config (Enter your own api key)
├── assets/
│ └── sample_job_description.txt # Example job description
│ └── sample_resume.txt # Example resume for testing
└── README.md # Project documentation

**⚠️ IMPORTANT:**  
Rename the `streamlit` folder to `.streamlit` before running the app.  
**`.streamlit`** is a special hidden folder used to store configuration files for a Streamlit app. Located in your app/project directory. Commonly contains files like `secrets.toml` or `config.toml` for setting themes, ports, server options, etc.

---

## 🚀 Setup Instructions
**1. Install dependencies**
     pip install -r requirements.txt

**2. Inside the renamed .streamlit/ folder, create a file called secrets.toml and add:**
     OPENAI_API_KEY = "sk-your-api-key"
      
**3. Run the application**
     streamlit run app.py

---

**Sample Inputs**
Use the assets/ folder to test the app with example files:
- sample_resume.txt
- sample_job_description.txt


# Final Note
This project demonstrates how Generative AI can enhance recruitment workflows by intelligently matching resumes to job descriptions. Designed for learning purposes, it’s lightweight, easy to run, and leverages modern tools like Streamlit and OpenAI’s GPT-4, making it ideal for showcasing AI prototyping skills with practical business relevance.

# Screenshot
![AI_Job_Description_Analyzer](https://github.com/user-attachments/assets/06c671b1-a86b-4ed7-887d-51def36c2280)

