import streamlit as st
import google.generativeai as genai
from prompts import get_analysis_prompt

# Load Gemini API key from .streamlit/secrets.toml
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash-001")

# Page configuration
st.set_page_config(page_title="AI Job Description Analyzer", layout="centered")
st.title("📄 AI Job Description Analyzer")
st.write("Compare your resume with a job description using Gemini AI (Google).")

# Layout: 2 input columns
col1, col2 = st.columns(2)

with col1:
    jd_input = st.text_area("📝 Job Description", height=350, placeholder="Paste or write the job description here...")

with col2:
    resume_input = st.text_area("📝 Resume", height=350, placeholder="Paste or write your resume here...")


# Analyze Button in the center
col_center = st.columns(3)
with col_center[1]:
    analyze_clicked = st.button("🔍 Analyze Match")

# On button click
if analyze_clicked:
    if not jd_input or not resume_input:
        st.warning("Please provide both job description and resume.")
    else:
        with st.spinner("Analyzing using Gemini..."):
            prompt = get_analysis_prompt(jd_input, resume_input)
            
            try:
           #     model = genai.GenerativeModel("gemini-2.0-flash-001")
                response = model.generate_content(prompt)
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error: {e}")
