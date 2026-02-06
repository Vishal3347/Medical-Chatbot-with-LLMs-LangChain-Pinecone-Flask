import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request
from dotenv import load_dotenv

from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from transformers import pipeline
from langchain.llms import HuggingFacePipeline


print("🔥 app.py started")

# -------------------- ENV SETUP --------------------
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

INDEX_NAME = "medical-chatbot"

# -------------------- FLASK APP --------------------
app = Flask(__name__)

# -------------------- EMBEDDINGS --------------------
embeddings = download_hugging_face_embeddings()

# -------------------- PINECONE VECTOR STORE --------------------
docsearch = PineconeVectorStore.from_existing_index(
    index_name=INDEX_NAME,
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# -------------------- LOCAL LLM (SMALL MODEL) --------------------
hf_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",   # ~990MB
    max_new_tokens=256,
    temperature=0.3
)

chatModel = HuggingFacePipeline(pipeline=hf_pipeline)

# -------------------- PROMPT --------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# -------------------- ROUTES --------------------
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    print("User:", msg)

    response = rag_chain.invoke({"input": msg})
    answer = response["answer"]

    print("Bot:", answer)
    return str(answer)

# -------------------- RUN --------------------
if __name__ == "__main__":
    print("🚀 Starting Flask app on port 8080")
    app.run(host="0.0.0.0", port=8080, debug=True)
