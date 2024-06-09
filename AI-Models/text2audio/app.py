# app.py

import streamlit as st
from audiocraft.models import musicgen
from audiocraft.utils.notebook import display_audio
import torch
import numpy as np
import soundfile as sf
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

# Title
st.title("MusicGen Demo")

# Description
st.write("Generate music using the MusicGen model by Facebook Research.")

# Input for text prompt
prompt = st.text_input("Enter a text prompt for the music generation:")

# Button to generate music
if st.button("Generate Music"):
    # Load the pre-trained model
    model = musicgen.MusicGen.get_pretrained('medium', device='cuda' if torch.cuda.is_available() else 'cpu')
    model.set_generation_params(duration=8)

    # Generate the music
    res = model.generate([prompt], progress=True)

    # Extract the generated audio
    audio = res[0][0].cpu().numpy()
    
    # Save the audio to a buffer
    buffer = BytesIO()
    sf.write(buffer, audio, 32000, format="wav")
    buffer.seek(0)
    
    # Display the audio
    st.audio(buffer, format='audio/wav')

    st.success("Music generation completed!")


