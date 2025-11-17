AmbedkarGPT – Intern Task (Kalpit Pvt Ltd, UK)

A simple command-line Q&A system built using:
LangChain
ChromaDB
HuggingFace Embeddings (all-MiniLM-L6-v2)
Ollama (Mistral 7B)
Python 3.8+
This system answers questions only from the provided Ambedkar speech using a custom RAG pipeline.

Features

✓ Loads and processes speech.txt
✓ Splits text into chunks
✓ Creates embeddings using HuggingFace
✓ Stores vectors locally using ChromaDB
✓ Retrieves relevant chunks
✓ Sends context + question to Mistral LLM
✓ Fully local, no API keys, no internet needed

Project Structure
AmbedkarGPT-Intern-Task/
│
├── main.py
├── requirements.txt
├── README.md
└── speech.txt

Installation Instructions
1. Install Ollama (Required)

Download for Windows:
https://ollama.com/download

Then pull the model:

ollama pull mistral

2. Create Virtual Environment (Optional but recommended)
python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

Running the Program

Run in the terminal:
python main.py


You will see:

AmbedkarGPT Q&A System
Ask a question:


Example:

Ask a question: What is the real enemy according to Ambedkar?

Notes

Everything runs locally, no API keys required.

Works on CPU (GPU not required).

Only answers from the provided speech text.

Submitted By

Shruti Gajbe
AI Intern Task – Kalpit Pvt Ltd (Phase 1)