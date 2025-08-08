import streamlit as st
import fitz  # PyMuPDF
import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Streamlit setup
st.set_page_config(page_title="Document Q&A", layout="wide")
st.title("📄 LLM-Powered Document Q&A (Gemini)")
st.markdown("Upload one or more PDF files and ask questions based on their content.")

# PDF parsing
def extract_chunks_from_pdf(file, chunk_size=500, overlap=50):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    chunks = []
    for i in range(0, len(full_text), chunk_size - overlap):
        chunk = full_text[i:i + chunk_size]
        chunks.append({"content": chunk})
    return chunks

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
all_chunks = []

if uploaded_files:
    for file in uploaded_files:
        chunks = extract_chunks_from_pdf(file)
        all_chunks.extend(chunks)

    st.success(f"✅ Processed {len(uploaded_files)} PDF(s), got {len(all_chunks)} chunks.")

    # Save chunks
    with open("parsed_chunks.json", "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    # Create FAISS index
    chunk_texts = [c["content"] for c in all_chunks]
    embeddings = embed_model.encode(chunk_texts)
    dimension = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
else:
    st.warning("Please upload at least one PDF.")

# Q&A Section
st.subheader("🔍 Ask a question")
question = st.text_input("Enter your question")

if st.button("Get Answer") and question and all_chunks:
    # Retrieve top chunks
    query_embedding = embed_model.encode([question])
    scores, indices = index.search(np.array(query_embedding), 3)
    top_chunks = "\n".join([chunk_texts[i] for i in indices[0]])

    prompt = f"""
You are an assistant for insurance policy interpretation.

Based on the following clauses:
{top_chunks}

Question: "{question}"

Respond STRICTLY in one short sentence, starting with 'Yes,' or 'No,' followed by the reason.
Do not include anything else.
"""

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip()
        st.markdown("### 🧠 Answer")
        st.write(answer)

    except Exception as e:
        st.error(f"⚠️ API call failed: {e}")

elif question:
    st.info("Please upload and process PDF documents before asking.")
