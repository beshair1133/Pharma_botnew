import streamlit as st
import random
import json

# Load pharmacology data
with open("pharma_data.json", "r") as f:
    pharma_data = json.load(f)

st.set_page_config(page_title="Pharma Mnemonic Bot", layout="centered")
st.title("💊 Pharmacology Mnemonic & Quiz Bot")

# User selects a drug class
all_classes = list(pharma_data.keys())
drug_class = st.selectbox("📘 Choose a drug class to learn:", all_classes)

if drug_class:
    st.subheader("📚 Classification")
    for item in pharma_data[drug_class]["classification"]:
        st.markdown(f"- {item}")

    st.subheader("💡 Mnemonic")
    st.markdown(f"**Mnemonic:** {pharma_data[drug_class]['mnemonic']}")

    st.subheader("📝 Quick Quiz")
    quiz = random.choice(pharma_data[drug_class]["quiz"])
    user_answer = st.text_input(f"Q: {quiz['question']}")
    
    if user_answer:
        if user_answer.strip().lower() == quiz['answer'].strip().lower():
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. Correct answer: {quiz['answer']}")
