import gradio as gr         #UI library
from transformers import pipeline      #transformer pipeline

translation_pipeline= pipeline('translation', model='Helsinki-NLP/opus-mt-en-es')
result=translation_pipeline("My name is Sakshi")
print(result[0]['translation_text'])

def translate_transformer(from_text):
    results = translation_pipeline(from_text)
    return result[0]['translation_text']