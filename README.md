
## 🚀 PDF Policy Interpreter

*Tagline:* An LLM-powered application for querying insurance policy documents.

-----

## 📖 Description

The PDF Policy Interpreter is a Python project that leverages the power of Large Language Models (LLMs) to answer specific questions about insurance policy documents. This application is designed to provide a flexible and scalable solution for quickly extracting and interpreting information from complex PDF files, which is particularly useful for tasks like claim processing, policy analysis, and customer support.

The project combines several key technologies to create a seamless question-answering system:

  * *PDF Processing:* It uses the *PyMuPDF* library to efficiently extract raw text from PDF files.
  * *Text Preprocessing:* The extracted text is then divided into manageable "chunks" to prepare it for embedding.
  * *Vector Embeddings:* A *Sentence Transformer* model transforms these text chunks into numerical vectors (embeddings), which capture the semantic meaning of the text.
  * *Vector Search:* The *FAISS* library is used to build a highly efficient vector index. This allows the application to quickly find the most relevant text chunks from the policy document that relate to a user's question.
  * *Generative AI:* The *Gemini 1.5 Flash* model is used to generate a concise and accurate answer based on the retrieved context, ensuring the response is directly relevant to the policy clauses.

The application is built with *Streamlit*, providing an intuitive and user-friendly web interface where users can upload PDF files, ask questions, and receive instant answers.

-----

## ✨ Features

1.  *Multi-PDF Support:* Process one or multiple PDF documents simultaneously.
2.  *Context-Aware Q\&A:* Answers are generated based only on the content of the uploaded PDF, preventing hallucination.
3.  *Efficient Search:* The use of *FAISS* ensures quick retrieval of relevant information, even from large documents.
4.  *User-Friendly Interface:* A *Streamlit* web app makes the application accessible to non-technical users.
5.  *Configurable:* The chunking and search parameters can be easily adjusted to optimize performance.
6.  *Scalable:* The architecture is designed to handle large documents and can be scaled for more extensive datasets.

-----

## 🧰 Tech Stack

The project uses the following key technologies and libraries:

| Technology | Version | Purpose |
| :--- | :--- | :--- |
| *Python* | 3.9+ | The core programming language. |
| *streamlit* | 1.12.0+ | Creates the interactive web UI. |
| *PyMuPDF* | 1.19.0+ | Extracts text from PDF files. |
| *google-generativeai* | 1.0.0+ | Interfaces with the Google Gemini API for Q\&A. |
| *sentence-transformers* | 2.3.0+ | Generates vector embeddings for text chunks. |
| *faiss-cpu* | latest | Manages the vector index for efficient similarity search. |
| *python-dotenv* | latest | Manages environment variables for API keys. |
| *numpy* | 1.21.2+ | Provides numerical operations for embedding and FAISS. |

-----

## 📁 Project Structure

The project is organized into a clean and logical structure to ensure maintainability and readability.


├── .env                  # Environment variables (e.g., API keys)
├── app.py                # Main Streamlit application and Q&A logic
├── main.py               # Standalone command-line example script
├── parsed_chunks.json    # Cached chunks of processed PDF text
├── preprocess_pdf.py     # Script for text extraction and chunking (future enhancement)
├── requirements.txt      # List of project dependencies
├── sample.pdf            # A sample PDF file for testing
└── utils.py              # Utility functions (future enhancement)


-----

## ⚙ How to Set Up and Run

Follow these steps to get the project up and running on your local machine.

### *1. Prerequisites*

  * *Python 3.9+* installed on your system.
  * A *Google Gemini API Key*. You can obtain one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

### *2. Installation*

1.  *Clone the repository:*

    bash
    git clone https://github.com/Sanket1218/llm-model.git
    cd llm-model
    

2.  *Create a virtual environment* (recommended):

    bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate      # On Windows
    

3.  *Install dependencies:*

    bash
    pip install -r requirements.txt
    

4.  *Set up the API key:*
    Create a file named .env in the project root and add your Gemini API key:

    ini
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    

### *3. Running the Application*

This project offers two ways to interact with the model: a web-based interface and a command-line script.

#### *Using the Streamlit Web App*

This is the recommended way to use the application.

bash
streamlit run app.py


This command will start a local web server and open the application in your browser. You can then upload a PDF and ask questions directly in the UI.

#### *Using the Command-Line Script*

To test the core logic with a predefined query, you can run main.py.

bash
python main.py


This script will use the parsed_chunks.json file (generated by the Streamlit app) and a hardcoded query to demonstrate the Q\&A functionality. It will print the answer directly to the console.

-----

## 🧪 Testing

The best way to test the application is through the Streamlit interface.

1.  Start the application with streamlit run app.py.
2.  Upload the sample.pdf file provided in the repository.
3.  Enter a question in the text box related to the content of the PDF (e.g., "What are the eligibility criteria for this policy?").
4.  Click "Get Answer" and verify that the response is accurate and based on the document's content.

-----

## 📸 Screenshot)


<img width="1919" height="909" alt="Screenshot 2025-08-13 114841" src="https://github.com/user-attachments/assets/2122caeb-d5f4-42d5-957c-28bc7974f0eb" />


