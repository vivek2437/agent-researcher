import sys
import os

# 🔥 Add project root to Python path FIRST
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from pipelines.research_pipeline import run_research


st.set_page_config(page_title="AI Research Agent", layout="wide")

st.title("🧠 AI Research Agent")

topic = st.text_input("Enter Research Topic:")

if st.button("Run Research"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Researching..."):
            result = run_research(topic)
            st.success("Research Completed")
            st.markdown(result)
