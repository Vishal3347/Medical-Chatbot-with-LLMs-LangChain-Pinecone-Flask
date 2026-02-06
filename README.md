🩺 Medical Chatbot using RAG (LangChain + Pinecone + Flask)

An end-to-end Medical Question Answering Chatbot built using Retrieval Augmented Generation (RAG).

The chatbot answers medical questions based on uploaded PDF documents using vector search and a free local LLM (HuggingFace).

🚀 Features

📄 PDF ingestion & processing

🔍 Semantic search using Pinecone

🧠 RAG pipeline with LangChain

🤖 Free local LLM (no OpenAI billing required)

🌐 Flask web interface

⚡ Real-time question answering

🏗️ Project Architecture

Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask/
│
├── data/
│   └── Medical_book.pdf
│
├── src/
│   ├── helper.py          # PDF loading, chunking, embeddings
│   ├── prompt.py          # System prompt for the chatbot
│
├── templates/
│   └── chat.html          # Frontend UI
│
├── app.py                 # Flask application
├── storeindex.py          # Indexing PDFs into Pinecone
├── requirements.txt
├── .gitignore
├── README.md

🧠 Tech Stack

Python 3.10

LangChain

Pinecone (Vector Database)

HuggingFace Transformers

Sentence Transformers

Flask

HTML/CSS

⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/your-username/Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask.git
cd Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask

2️⃣ Create & Activate Conda Environment

conda create -n medibot310 python=3.10 -y

conda activate medibot310

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file in the project root:

PINECONE_API_KEY=your_pinecone_key_here

OPENAI_API_KEY=dummy_value_not_used

PINECONE_ENVIRONMENT=us-east-1

PINECONE_INDEX_NAME=medical-chatbot


⚠️ Do NOT push .env to GitHub

📥 Index Medical PDFs

Make sure your PDFs are inside the data/ folder.

Run:

python storeindex.py


This will:

Load PDFs

Split into chunks

Generate embeddings

Store vectors in Pinecone

▶️ Run the Application

python app.py


Open browser:

http://127.0.0.1:8080

💬 Example Questions

What are the symptoms of diabetes?

What is abdominal ultrasound?

How are gallstones treated?

What are abdominal wall defects?

🆓 Free Usage (No OpenAI Billing)

Uses HuggingFace local LLM

No OpenAI quota required

No paid API calls

⚠️ Notes

Pinecone is used only for vector storage

Flask runs in development mode

Warnings about deprecations are safe to ignore

🔒 Security

.env is ignored

API keys are never committed

Virtual environment files are excluded

📌 Future Improvements

Add source citations

Add chat history memory

Switch Pinecone → FAISS (fully offline)

Deploy to Render / Railway

Dockerize the project

🙌 Acknowledgements

Inspired by real-world RAG architectures using LangChain and vector databases.
