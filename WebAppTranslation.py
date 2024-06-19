<<<<<<< HEAD
import gradio as gr         #UI library
from transformers import pipeline      #transformer pipeline

translation_pipeline= pipeline('translation', model='Helsinki-NLP/opus-mt-en-es')
result=translation_pipeline("My name is Sakshi")
=======
import gradio as gr         #UI library
from transformers import pipeline      #transformer pipeline

translation_pipeline= pipeline('translation', model='Helsinki-NLP/opus-mt-en-es')
result=translation_pipeline("My name is Sakshi")
>>>>>>> 13abc0eefe707739571d301d935e89fc6ae41d87
print(result[0]['translation_text'])