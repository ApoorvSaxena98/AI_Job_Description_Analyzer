# prompts.py

def get_analysis_prompt(jd, resume):
    return f"""
You are an AI HR Assistant.

Compare the following job description and resume.

Job Description:
{jd}

Resume:
{resume}

Tasks:
1. Rate how well the resume matches the JD on a scale of 0 to 100.
2. List the matching and missing skills.
3. Provide 3 suggestions to improve the resume for this role.

Return your analysis in clean, formatted Markdown.
"""
