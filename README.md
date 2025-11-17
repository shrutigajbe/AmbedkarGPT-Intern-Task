# AmbedkarGPT: A RAG-Powered Q&A System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-yellow.svg)
![Ollama](https://img.shields.io/badge/Ollama-Mistral%207B-blueviolet.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A functional prototype of a command-line Q&A system built for the **Kalpit Pvt Ltd AI Intern Assignment**. This system leverages a Retrieval-Augmented Generation (RAG) pipeline to answer questions based solely on a provided speech by Dr. B.R. Ambedkar.

---

## 🌟 Features

- **Context-Aware Answers**: Answers questions based *only* on the provided speech text.
- **Local & Free**: Runs entirely on your local machine using free, open-source models.
- **Efficient Retrieval**: Uses ChromaDB for fast and accurate retrieval of relevant information.
- **Simple CLI**: Clean and easy-to-use command-line interface.

---

## 🛠️ Tech Stack

This project is built with the following technologies:

| Component | Technology |
| :--- | :--- |
| **Framework** | [LangChain](https://www.langchain.com/) |
| **Vector Store** | [ChromaDB](https://www.trychroma.com/) |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` |
| **LLM** | [Ollama](https://ollama.ai/) with `Mistral 7B` |
| **Language** | Python 3.8+ |

---

## 🚀 Setup and Installation

To get this project running on your local machine, follow these steps.

### Prerequisites

1.  **Python 3.8+**: Ensure you have Python installed.
2.  **Ollama**: You must have Ollama installed and running.
    *   **Install Ollama**: Follow the instructions at [https://ollama.ai/](https://ollama.ai/).
    *   **Pull the Mistral Model**: Open your terminal and run:
        ```bash
        ollama pull mistral
        ```

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/shrutigajbe/AmbedkarGPT-Intern-Task.git
    cd AmbedkarGPT-Intern-Task
    ```

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\Activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## 💻 Usage

Once the setup is complete, you can run the application.

1.  **Start Ollama**: In a separate terminal, run:
    ```bash
    ollama serve
    ```

2.  **Run the Q&A System**: In the terminal where you set up the virtual environment, run:
    ```bash
    python main.py
    ```

3.  **Ask Questions**: The system will prompt you to ask a question. Type your query and press Enter.

#### Example Interaction
==================================================
AmbedkarGPT is ready! Ask your questions about the speech.
Type 'quit' to exit.
Your Question: What is the real remedy according to the speech?

Answer: According to the given context, the real remedy for the problem of caste, as suggested by the speaker, is to destroy the belief in the sanctity of the shastras.


Your Question: quit
---

## 📁 Project Structure

AmbedkarGPT-Intern-Task/
├── main.py # Main application script
├── requirements.txt # Project dependencies
├── README.md # This file
├── speech.txt # Source text for the Q&A system
└── db/ # Local ChromaDB vector store


---

## 📝 Assignment Details

This project was created to fulfill the requirements for the Kalpit Pvt Ltd AI Intern Assignment (Phase 1). It demonstrates the implementation of a core RAG pipeline with the specified technical constraints.

---


