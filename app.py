import streamlit as st
import openai
from prompts import get_analysis_prompt

# Set up OpenAI API Key (for local testing you can hardcode it here)
openai.api_key = st.secrets["OPENAI_API_KEY"] # API Key will be fetched from ".streamlit/secrets.toml"


st.set_page_config(page_title="AI Job Description Analyzer", layout="centered")

st.title("📄 AI Job Description Analyzer")
st.write("Compare your resume with a job description using GPT-4.")

# User Inputs
#jd_input = st.text_area("📝 Paste Job Description Here", height=200, placeholder="Copy and paste the job description...")
#resume_input = st.text_area("📄 Paste Resume Text Here", height=200, placeholder="Paste your resume content...")

col1, col2 = st.columns(2)

with col1:
    jd_input = st.text_area("📝 Job Description", height=350, placeholder="Paste or write the job description here...")

with col2:
    resume_input = st.text_area("📝 Resume", height=350, placeholder="Paste or write your resume here...")


# Analyze Button
col_center = st.columns(3)
with col_center[1]:
    analyze_clicked = st.button("🔍 Analyze Match")


if analyze_clicked:
    if not jd_input or not resume_input:
        st.warning("Please provide both job description and resume.")
    else:
        with st.spinner("Analyzing using GPT..."):
            prompt = get_analysis_prompt(jd_input, resume_input)
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",  # Use "gpt-3.5-turbo" if no access to GPT-4
                    messages=[{"role": "user", "content": prompt}]
                )
                output = response['choices'][0]['message']['content'] # For older version
                #output = response.choices[0].message.content # For version > 1.0.0
                st.markdown(output)
            except Exception as e:
                st.error(f"Error: {e}")
