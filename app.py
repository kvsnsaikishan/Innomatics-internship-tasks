import streamlit as st
from google import genai

# Paste your FULL real API key here
client = genai.Client(api_key="AIzaSyCAOtTVogjRst2ziUMe6xyFBNrdCtzpGI8")

st.title("🎓 AI Career Advisor Chatbot")

user_input = st.text_input("Ask your career question:")

if user_input:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
        )
        st.write("### 🤖 Advice:")
        st.write(response.text)
    except Exception as e:
        st.error(str(e))