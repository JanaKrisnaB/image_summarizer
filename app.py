import streamlit as st
from utils import ocr_text
from summarizer import summarize_text
from PIL import Image
import tempfile
import base64

st.set_page_config(page_title="🖼️ Image-to-Text Summarizer", layout="centered")

st.title("🖼️ Image to Text Summarizer")
st.write("Upload an image and get a summary of the text inside it.")

uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        img_path = tmp.name

    with st.spinner("Extracting and summarizing text..."):
        text, count = ocr_text(img_path)

    st.markdown(f"**Extracted {count} characters**")
    st.text_area("📝 Extracted Text", text, height=200)

    if count < 30:
        st.warning("Text too short to summarize.")
    else:
        summary = summarize_text(text, count)
        st.subheader("📌 Summary")
        st.success(summary)

        # Download summary
        b64 = base64.b64encode(summary.encode()).decode()
        download_link = f'<a href="data:file/txt;base64,{b64}" download="summary.txt">📥 Download Summary</a>'
        st.markdown(download_link, unsafe_allow_html=True)
