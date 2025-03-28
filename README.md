# GraphRAG for Financial Document Q&A

An experimental app that uses a simple graph-based Retrieval-Augmented Generation (GraphRAG) pipeline
to answer questions from uploaded financial PDFs like 10-Qs or annual reports.

## Features

- Upload PDF-based financial reports
- Parse and chunk the content into graph-linked nodes
- Use GPT to answer financial questions with real context and citation

## Setup

```bash
pip install -r requirements.txt
streamlit run main.py
```

## Environment Variables

```bash
export OPENAI_API_KEY="your-api-key-here"
```
