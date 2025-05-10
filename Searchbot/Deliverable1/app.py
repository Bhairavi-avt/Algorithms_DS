import streamlit as st
from deliverable1 import rate_url_validity

st.set_page_config(layout="wide")
st.title("🧠 URL Credibility Evaluator")

query = st.text_input("🔍 Your Search Query", "Nvidia Stock price")
url = st.text_input("🔗 URL to Analyze", "https://leapscholar.com")

if st.button("Evaluate Credibility"):
    with st.spinner("Analyzing..."):
        result = rate_url_validity(query, url)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("✅ Analysis Complete!")
        st.markdown("### 📊 Credibility Scores")
        st.table(result)
