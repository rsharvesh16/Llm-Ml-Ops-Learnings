from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro") 

def generate_response(input_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([input_text, "", prompt])
    return response.text

def main():
    st.title("Text-2-Text Model")

    st.header("Google Gemini Pro AI Model")

    # Get user input
    input_text = st.text_input("Enter your text:", key="input")

    prompt = """You are an expert in understanding the given question and you have a clear mind.
    When a user gives a query give them accurate answers and explain them in detail with points,
    Answer them accurately and correctly and dont give wrong answers. You are an intellingent in
    doing this. Avoid speaking contents related to abuse, religion, sexual abuse etc which may
    give a conflict to the user. Be Polite and Generous."""

    if st.button("Generate Output"):
        # Generate and display the output
        response = generate_response(prompt, input_text)
        st.subheader("The Response Is")
        st.write(response)

if __name__ == "__main__":
    main()