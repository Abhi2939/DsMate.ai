import streamlit as st
from Chains.explain_chain import get_explain_chain

st.set_page_config(page_title="LLM Code Assistant", layout="wide")
st.title("Ai Assistant")

code_input = st.text_area("Paste your code here",
                           height = 300)

if st.button("Explain Code"):
    if code_input.strip():
        chain = get_explain_chain()
        response = chain.invoke({"code":code_input})

        st.subheader("Explaination")
        st.write(response)
    else:
        st.write("Warning write a code here")