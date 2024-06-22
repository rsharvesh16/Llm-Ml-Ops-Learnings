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
    st.title("Text-2-Translation Model")

    st.header("Google Gemini AI Model")

    # Get user input
    input_text = st.text_input("Enter your text:", key="input")

    target_language = st.selectbox("Select target language for translation", ["English", "Spanish", "Chinese", "Hindi", "Arabic", "Portuguese", "Bengali", "Russian", "Japanese", "German", "Wu (Shanghainese)", "Vietnamese", "Korean", "French", "Turkish", "Italian", "Yue (Cantonese)", "Thai", "Jin", "Southern Min", "Polish"])
    prompt = f"Translate the following text to {target_language}: {input_text}"
    

    if st.button("Generate Output"):
        # Generate and display the output
        response = generate_response(prompt, input_text)
        st.subheader("The Response Is")
        st.write(response)

if __name__ == "__main__":
    main()