from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

html_code = """
<div style="background-color: #f0f0f0; padding: 20px; border-radius: 10px;">
    <h1 style="color: #333;">Image-2-Text Model</h1>
    <p style="color: #555;">Gemini Pro Vision Model</p>
</div>
"""

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

st.markdown(html_code, unsafe_allow_html=True)
# st.set_page_config(page_title="Gemini Image Demo")

input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Generate Response")

## If ask button is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)