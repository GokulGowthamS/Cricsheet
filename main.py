import streamlit as st
import base64
from PIL import Image
from io import BytesIO

def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        img_data = img_file.read()
        return base64.b64encode(img_data).decode()

image_path = r"C:\Users\ADMIN\Cricsheet\Pages\BG\cartoon-character-playing-cricket-game-field.jpg"

try:
    img_base64 = img_to_base64(image_path)

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('data:image/jpeg;base64,{img_base64}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            padding: 0;
        }}
        .title-container {{
            text-align: center;
            color: white;
            font-size: 4em;
            margin-top: 350px;
            margin-bottom: 20px;
            
        }}
        
        
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="title-container">Cricsheet Match Analysis</div>', unsafe_allow_html=True)

except FileNotFoundError:
    st.error("Image not found at the specified path.")
