import streamlit as st
from Chains.explain_chain import get_explain_chain
from Chains.complexity_chain import get_complexity_chain
from Chains.debug_chain import get_debug_chain
from Memory.chat_memory import get_memory

st.set_page_config(page_title="LLM Code Assistant", 
                   layout="wide")
st.title("🧠 AI Code Assistant")
st.caption("Explain, debug, and analyze code using LLMs")

if "memory" not in st.session_state:
    st.session_state.memory = get_memory()

code_input = st.text_area(
    "Paste your code here",
    height=300,
    placeholder="Paste C++ / Python / Java code here..."
)
tab1, tab2, tab3 = st.tabs(
    ["📖 Explain", "📊 Complexity","🐞 Bug Detection"]
)

with tab1:
    if st.button("Explain Code"):
        if code_input.strip():
            chain = get_explain_chain(st.session_state.memory)
            response = chain.invoke({
                "code":code_input,
                "chat_history":st.session_state.memory.buffer
                })
            st.session_state.memory.save_context(
                {"input":code_input},
                {"output":response}
            )

            st.subheader("Explaination")
            st.write(response)
        else:
            st.write("Warning write a code here")

with tab2:
    
    if st.button("Complexity Analysis"):
        if code_input.strip():
            chain = get_complexity_chain(st.session_state.memory)
            response = chain.invoke({
                "code":code_input,
                "chat_history":st.session_state.memory.buffer
                })
            
            st.session_state.memory.save_context(
                {"input":code_input},
                {"output":response}
            )

            st.subheader("Explaination")
            st.write(response)
        else:
            st.write("Warning write a code here")

with tab3:
    if st.button("Bug Debug"):
        if code_input.strip():
            chain = get_debug_chain(st.session_state.memory)
            response = chain.invoke({
                "code":code_input,
                "chat_history":st.session_state.memory.buffer
                })
            
            st.session_state.memory.save_context(
                {"input":code_input},
                {"output":response}
            )

            st.subheader("Debugging")
            st.write(response)
        else:
            st.write("Warning write a code here")

st.divider()

if st.button("Clear Memory"):
    st.session_state.memory.clear()
    st.success("Conversation memory cleared.")
