#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Install dependencies (run once in terminal or notebook)
# pip install streamlit transformers torch

import streamlit as st
from transformers import BertForSequenceClassification, BertTokenizer
import torch

# -------------------------
# Backend: Load BERT Model
# -------------------------
st.sidebar.info("CyberShield AI: Loading model...")

model_name = 'ElSlay/BERT-Phishing-Email-Model'

@st.cache_resource  # caches model so it doesn't reload every run
def load_model():
    model = BertForSequenceClassification.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model.eval()
    return model, tokenizer

model, tokenizer = load_model()
st.sidebar.success("Model loaded successfully!")

# -------------------------
# Prediction Function
# -------------------------
def predict_email(email_text):
    inputs = tokenizer(email_text, return_tensors="pt", truncation=True, padding='max_length', max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1)
        probs = torch.softmax(logits, dim=-1)
    result = "Phishing" if prediction.item() == 1 else "Legitimate"
    probability = probs[0][1].item() if prediction.item() == 1 else probs[0][0].item()
    return result, probability

# -------------------------
# Frontend: Streamlit Interface
# -------------------------
st.title("🛡️ CyberShield AI - Scam & Phishing Detection")
st.write("Paste any email or message below and click **Predict** to detect if it's phishing or legitimate.")

# Input box
email_input = st.text_area("Paste Email / Message Here:")

# Predict button
if st.button("Predict"):
    if email_input.strip() == "":
        st.warning("Please enter an email or message to predict.")
    else:
        result, prob = predict_email(email_input)
        # Color coding
        if result == "Phishing":
            st.error(f"Prediction: {result} | Confidence: {prob*100:.2f}%")
        else:
            st.success(f"Prediction: {result} | Confidence: {prob*100:.2f}%")

# Optional sidebar instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Paste the email or message in the text area.
2. Click the Predict button.
3. The result will show whether it's Phishing (fake) or Legitimate (real) with confidence.
""")

