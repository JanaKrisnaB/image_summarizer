from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, count):
    '''Summarizes input text based on word count.'''
    return summarizer_pipeline(text, max_length=count // 2, min_length=count // 4, do_sample=False)[0]["summary_text"]
