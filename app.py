import streamlit as st
import requests

API_URL = "https://ai-code-assistant-yieh.onrender.com/api/v1"

st.set_page_config(page_title="AI Codebase Assistant", layout="wide")

st.title("💻 AI Codebase Assistant")
st.markdown("Analyze any codebase using AI. Upload a repository and ask questions.")

st.markdown("### 🚀 Features")
st.markdown("- Understand large codebases instantly\n- Semantic search using RAG\n- AI-powered explanations")

st.markdown("#### Example questions:")
st.markdown("- What does this project do?\n- Explain the main function\n- How is authentication handled?")

# Upload
uploaded_file = st.file_uploader("Upload Code (ZIP file)", type=["zip"])

if st.button("Ingest Code"):
    if uploaded_file:
        with st.spinner("Indexing codebase... This may take a few seconds."):
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
                response = res.json()
                st.write(response.get("answer", response))
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a question")

# Summarize Repository
st.markdown("""
Click below to generate a high-level summary of the entire codebase including:
- Purpose
- Architecture
- Key modules
""")

if st.button("Summarize Repo"):
    with st.spinner("Analyzing entire codebase..."):
        try:
            res = requests.post(f"{API_URL}/summarize")

            if res.status_code == 200:
                response = res.json()
                st.success("Summary:")
                st.write(response.get("summary", response))
            else:
                st.error(f"Failed with status code: {res.status_code}")

        except Exception as e:
            st.error(f"Error: {e}")