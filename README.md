Medical Chatbot using RAG (LangChain, Pinecone, Flask)

Overview

This project is an end-to-end Medical Question Answering Chatbot built using Retrieval Augmented Generation (RAG). The chatbot answers medical questions by retrieving relevant information from medical PDF documents and generating responses using a free local language model.

The application combines document retrieval, vector search, and a conversational interface to deliver accurate and context-aware medical responses.

Key Features

PDF-based medical knowledge ingestion

Semantic search using vector embeddings

Retrieval Augmented Generation (RAG) pipeline

Free local LLM using HuggingFace (no OpenAI billing)

Flask-based web interface

Real-time medical question answering

Project Structure

data

Contains medical PDF documents used for knowledge retrieval

src

Contains helper functions and prompt configuration

templates

Contains the HTML frontend for the chatbot

app.py

Main Flask application

storeindex.py

Script to process PDFs and store embeddings in Pinecone

requirements.txt

Project dependencies

Technology Stack

Python 3.10

LangChain

Pinecone Vector Database

HuggingFace Transformers

Sentence Transformers

Flask

HTML and CSS

How the System Works

Medical PDF documents are loaded and processed

Documents are split into smaller chunks

Embeddings are generated using a sentence-transformer model

Embeddings are stored in Pinecone for fast retrieval

User queries are matched against stored vectors

Relevant document chunks are passed to the language model

The chatbot generates a context-aware response

Setup Requirements

Python 3.10 environment

Pinecone account and API key

Internet connection for model downloads

Environment Variables

The application requires environment variables for Pinecone and model configuration.

These variables are stored in a .env file which is excluded from version control.

Running the Application

First, index the medical documents to the vector database.

Then start the Flask application.

Open the application in a browser to interact with the chatbot.

Example Questions

What are the symptoms of diabetes?

What is an abdominal ultrasound?

How are gallstones treated?

What are abdominal wall defects?

Free Usage

This project does not rely on paid OpenAI APIs.

A HuggingFace-based local language model is used, making the chatbot free to run.

Security Notes

Environment variables are excluded from GitHub

API keys are never committed

Virtual environment files are ignored

Future Enhancements

Add source citations in responses

Enable chat memory

Replace Pinecone with FAISS for full offline mode

Deploy the application online

Containerize using Docker
