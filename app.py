import streamlit as st
from utils import ocr_text
from summarizer import summarize_text
from PIL import Image
import tempfile

st.set_page_config(page_title="🖼️ Image-to-Text Summarizer", layout="centered")

st.title("🖼️ Image to Text Summarizer")
st.write("Upload an image and get a summary of its extracted text.")

uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        img_path = tmp.name

    with st.spinner("Extracting and summarizing..."):
        text, count = ocr_text(img_path)

        if count < 30:
            st.warning("Text too short to summarize.")
            st.text(text)
        else:
            summary = summarize_text(text, count)
            st.subheader("📝 Extracted Text")
            st.text(text)
            st.subheader("📌 Summary")
            st.success(summary)
