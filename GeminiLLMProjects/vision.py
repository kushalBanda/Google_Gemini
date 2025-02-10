from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

## Function to load Gemini Pro model and get responses
model = genai.GenerativeModel('')
def get_gemini_response(input, image):
    if input!= "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

## Initialize our Streamlit app
st.set_page_config(page_title = 'Gemini Image Demo')
st.header('Gemini LLM Application')

input = st.text_input('Input: ', key = "input")
uploaded_file = st.file_uploader('Choose an image', type = ['jpg', 'png', 'jpeg'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded image', use_column_width = True)


submit = st.button("Tell me about the image")

# If submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is: ")
    st.write(response)