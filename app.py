import streamlit as st
import requests

API_URL = "https://ai-code-assistant-yieh.onrender.com"

st.set_page_config(page_title="AI Code Assistant", layout="wide")

st.title("💻 AI Code Assistant (RAG)")
st.write("Upload a codebase and ask questions about it.")

# Upload
uploaded_file = st.file_uploader("Upload Code (ZIP file)", type=["zip"])

if st.button("Ingest Code"):
    if uploaded_file:
        with st.spinner("Processing..."):
            files = {"file": uploaded_file}
            try:
                res = requests.post(f"{API_URL}/ingest", files=files)
                st.success("Code ingested successfully!")
                st.json(res.json())
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please upload a ZIP file")

# Query
query = st.text_input("Ask a question about the code")

if st.button("Ask AI"):
    if query:
        with st.spinner("Thinking..."):
            try:
                res = requests.post(
                    f"{API_URL}/query",
                    json={"query": query}
                )
                st.success("Answer:")
                st.write(res.json())
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a question")