import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

def generate_tf_question(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    
    label = "True" if probs.argmax().item() == 1 else "False"
    
    question = f"{text}\n\nTrue or False? The statement above is {label}."
    return question


st.title("True/False Question Generator")
text = st.text_area("Enter some text:")
if st.button("Generate"):
    question = generate_tf_question(text)
    st.text(question)
