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


## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/llm-code-assistant.git
cd llm-code-assistant

2️⃣ Create Virtual Environment
python -m venv venv


Activate the environment:

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Ollama

Download and install Ollama from:
👉 https://ollama.com

Pull a model:

ollama pull llama3:8b


For low-RAM systems:

ollama pull mistral

5️⃣ Run the Application
streamlit run app.py


Open your browser at:

http://localhost:8501

🧪 Example Use Cases

Quickly understand unfamiliar code

Debug logical errors during DSA practice

Analyze time and space complexity for interviews

Get improvement hints without full solution dumping

🧠 Design Highlights

Modular LangChain runnable pipelines

Prompt-engineered responses (no hardcoded logic)

Session-based conversation memory

Local inference ensures privacy and zero API cost

📌 Limitations

Does not execute code automatically

Output quality depends on the selected LLM

Optimized for short to medium-length code snippets

🔮 Future Improvements

🚀 Optimization suggestions

🧪 Test case generation

🔀 Model switching (local ↔ cloud)

🧾 Code refactoring suggestions