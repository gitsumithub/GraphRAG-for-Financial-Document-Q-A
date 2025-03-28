import os
import fitz  # PyMuPDF
import openai
import networkx as nx
from langchain.text_splitter import CharacterTextSplitter

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def build_graph(text_chunks):
    G = nx.Graph()
    for idx, chunk in enumerate(text_chunks):
        G.add_node(idx, content=chunk)
        if idx > 0:
            G.add_edge(idx, idx - 1)
    return G

def graph_rag_query(pdf_file, question):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    full_text = extract_text_from_pdf(pdf_file)
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(full_text)

    graph = build_graph(chunks)
    selected_nodes = list(graph.nodes())[:5]
    context = "

".join([graph.nodes[i]['content'] for i in selected_nodes])

    prompt = f"Context:
{context}

Question: {question}

Answer concisely with citations."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial assistant that extracts accurate answers from documents."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response['choices'][0]['message']['content']
