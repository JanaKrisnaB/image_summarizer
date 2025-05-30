from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Caching the translation model for Tamil
'''@st.cache_resource
def load_translator():
    return pipeline("translation_en_to_ta", model="Helsinki-NLP/opus-mt-en-ta")'''
    
# Initialize the summarizer and translator
summarizer_pipeline = load_summarizer()
#translator_pipeline = load_translator()

def summarize_text(text, count, max_length=None, min_length=None):
    '''Summarizes input text based on word count or custom length parameters.'''

    # Validate input text
    if not text.strip():
        return "Error: Input text is empty."

    # Check if text is long enough to summarize
    if len(text.split()) < 10:
        return "Error: Input text is too short to summarize."

    # Default dynamic summary length based on word count (if no max/min provided)
    if not max_length or not min_length:
        max_length = count // 2
        min_length = count // 4

    # Ensure max_length is greater than min_length
    max_length = max(max_length, min_length + 50)


    # Perform summarization
    summary = summarizer_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]
    #summary_tamil = translator_pipeline(summary)[0]['translation_text']
    return summary #summary_tamil

