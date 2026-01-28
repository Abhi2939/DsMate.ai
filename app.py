import streamlit as st
from Chains.explain_chain import get_explain_chain
from Chains.complexity_chain import get_complexity_chain

st.set_page_config(page_title="LLM Code Assistant", layout="wide")
st.title("Ai Assistant")

code_input = st.text_area("Paste your code here",
                           height = 300)

col1, col2 = st.columns(2)

with col1:
    if st.button("Explain Code"):
        if code_input.strip():
            chain = get_explain_chain()
            response = chain.invoke({"code":code_input})

            st.subheader("Explaination")
            st.write(response)
        else:
            st.write("Warning write a code here")

with col2:
    
    if st.button("Complexity Analysis"):
        if code_input.strip():
            chain = get_complexity_chain()
            response = chain.invoke({"code":code_input})

            st.subheader("Explaination")
            st.write(response)
        else:
            st.write("Warning write a code here")