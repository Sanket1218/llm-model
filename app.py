import streamlit as st
import fitz  # PyMuPDF
import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro"

# Streamlit page config
st.set_page_config(page_title="Document Q&A", layout="wide")
st.title("📄 LLM-Powered Document Q&A (Gemini)")
st.markdown("Upload one or more PDF files and ask questions based on their content.")

# PDF reading and chunking
def extract_chunks_from_pdf(file, chunk_size=500, overlap=50):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Chunk text
    chunks = []
    for i in range(0, len(full_text), chunk_size - overlap):
        chunk = full_text[i:i + chunk_size]
        chunks.append({"content": chunk})
    return chunks

# File upload
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
all_chunks = []

if uploaded_files:
    for file in uploaded_files:
        chunks = extract_chunks_from_pdf(file)
        all_chunks.extend(chunks)

    st.success(f"✅ Processed {len(uploaded_files)} PDF(s), got {len(all_chunks)} chunks.")

    # Optionally save chunks
    with open("parsed_chunks.json", "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)
else:
    st.warning("Please upload at least one PDF.")

# Q&A Section
st.subheader("🔍 Ask a question")
question = st.text_input("Enter your question")

if st.button("Get Answer") and question and all_chunks:
    # Take top 10 chunks as context
    top_chunks = "\n".join([chunk["content"] for chunk in all_chunks[:10]])

    prompt = f"""
You are an assistant helping users understand PDF documents.

Context:
{top_chunks}

Question: {question}

Return your answer clearly.
"""

    try:
        response = model.generate_content(prompt)
        answer = response.text

        st.markdown("### 🧠 Answer")
        st.write(answer)

    except Exception as e:
        st.error(f"⚠️ API call failed: {e}")

elif question:
    st.info("Please upload and process PDF documents before asking.")
