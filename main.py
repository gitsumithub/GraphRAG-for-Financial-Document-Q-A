import streamlit as st
from modules.graphrag import graph_rag_query

st.set_page_config(page_title="GraphRAG Q&A for Financial Docs", layout="wide")
st.title("GraphRAG: Financial Document Question Answering")

uploaded_file = st.file_uploader("Upload a Quarterly or Annual Financial Report (PDF)", type=["pdf"])
question = st.text_input("Ask a question about the report:")

if uploaded_file and question:
    with st.spinner("Analyzing document..."):
        response = graph_rag_query(uploaded_file, question)
        st.subheader("Answer")
        st.success(response)
