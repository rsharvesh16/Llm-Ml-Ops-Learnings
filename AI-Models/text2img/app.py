import streamlit as st
from PIL import Image
from authtoken import auth_token

import torch
from diffusers import StableDiffusionPipeline

# Set up the Streamlit interface
st.title("Stable Bud")

# Text input for the prompt
prompt = st.text_input("Enter your prompt:", "")

# Button to generate the image
generate_button = st.button("Generate")

# Initialize the Stable Diffusion model
modelid = "CompVis/stable-diffusion-v1-4"
device = "cpu"
pipe = StableDiffusionPipeline.from_pretrained(modelid, torch_dtype=torch.float32, use_auth_token=auth_token)
pipe.to(device)

if generate_button:
    if prompt:
        with st.spinner("Generating image..."):
            image = pipe(prompt, guidance_scale=8.5)["images"][0]
        
        # Save and display the generated image
        image.save('generatedimage.png')
        st.image(image, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a prompt.")
