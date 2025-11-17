# main.py

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import os 

def setup_vector_store():
    print("Step 1: Loading and processing the document...")
    
    # Text File Loading
    loader = TextLoader("speech.txt")
    documents = loader.load()
    
    # Splitting the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    
    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Vector Store
    persist_directory = "db"
    if not os.path.exists(persist_directory):
        print("Creating new vector store...")
        vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=persist_directory)
    else:
        print("Loading existing vector store...")
        vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
        
    print("Document processed and vector store is ready.")
    return vector_store

# LLM and QA Chain
def setup_qa_chain(vector_store):
    print("\nStep 2: Initializing LLM and QA Chain...")
    
    llm = Ollama(model="mistral")
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )
    
    print("QA Chain is ready.")
    return qa_chain

# Run the Q&A
def main():
    vector_store = setup_vector_store()
    qa_chain = setup_qa_chain(vector_store)
    
    print("\n" + "="*50)
    print("AmbedkarGPT is ready! Ask your questions about the speech.")
    print("Type 'quit' to exit.")
    print("="*50 + "\n")
    
    # Loop to ask questions
    while True:
        query = input("Your Question: ")
        if query.lower() == 'quit':
            break
            
        result = qa_chain.invoke({'query': query})
        
        print(f"\nAnswer: {result['result']}")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()