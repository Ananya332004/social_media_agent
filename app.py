import streamlit as st
from transformers import pipeline

# Load DistilGPT-2 locally
generator = pipeline("text-generation", model="distilgpt2")

st.title("Social Media Agent 🎯")

platform = st.selectbox("Choose platform", ["Instagram", "Twitter", "LinkedIn"])
topic = st.text_input("Enter your brand/topic")
tone = st.selectbox("Tone", ["Casual", "Professional", "Funny", "Inspirational"])
days = st.slider("How many days of content?", 1, 7, 3)

if st.button("Generate"):
    prompt = f"""
    Write {days} {tone} {platform} captions specifically about {topic}.
    Each caption should:
    - Mention {topic} directly
    - Be short and catchy
    - Include 2–3 relevant hashtags
    - Suggest a simple image idea
    """
    outputs = generator(prompt, max_length=200, num_return_sequences=1)
    generated_text = outputs[0]["generated_text"]

    # Clean and format captions
    cleaned = generated_text.replace(prompt, "").strip()
    captions = cleaned.split("\n")
    formatted = "\n\n".join([f"{i+1}. {c.strip()}" for i, c in enumerate(captions) if c.strip()])

    st.markdown(formatted)
    st.download_button("Download captions", formatted, file_name="captions.txt")