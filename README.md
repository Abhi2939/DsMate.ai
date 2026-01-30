# 🧠 AI Code Assistant

AI Code Assistant is an **LLM-powered tool** that helps developers **understand, debug, and analyze code** using Large Language Models.  
It is built with **LangChain, Streamlit, and Ollama (local LLMs)** to enable fast, private, and cost-free inference.

---

## 🚀 Features

- 📖 **Code Explanation**  
  Step-by-step explanations of C++, Python, and Java code.

- 🐞 **Bug Detection & Suggestions**  
  Detects syntax errors, logical bugs, and edge cases with improvement suggestions.

- 📊 **Time & Space Complexity Analysis**  
  Analyzes algorithmic complexity with clear reasoning.

- 🧠 **Conversation Memory**  
  Supports multi-turn interactions such as follow-up questions and refinements.

- ⚡ **Local LLM Inference**  
  Runs entirely on your machine using Ollama (no API keys required).

- 🎨 **Clean UI with Tabs**  
  Simple and intuitive interface built using Streamlit.

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Ollama (local LLM runtime)  
- Streamlit  
- LLaMA 3 / Mistral (via Ollama)

---

## 📂 Project Structure

```text
DS/
├── app.py                  # Streamlit app
├── requirements.txt
├── README.md
│
├── chains/
│   ├── explain_chain.py
│   ├── debug_chain.py
│   └── complexity_chain.py
│
├── prompts/
│   ├── explain.txt
│   ├── debug.txt
│   └── complexity.txt
│
├── memory/
│   └── chat_memory.py
│
└── venv/                   # Ignored in Git
