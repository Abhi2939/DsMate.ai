🧠 AI Code Assistant

An LLM-powered code assistant that helps developers understand, debug, and analyze code using Large Language Models.
Built with LangChain, Streamlit, and Ollama (local LLMs) to enable fast, private, and cost-free inference.

🚀 Features

📖 Code Explanation
Get step-by-step explanations of C++, Python, or Java code.

🐞 Bug Detection & Suggestions
Detect syntax errors, logical bugs, and edge cases with improvement suggestions.

📊 Time & Space Complexity Analysis
Analyze algorithmic complexity with clear reasoning.

🧠 Conversation Memory
Supports multi-turn interactions (follow-up questions, refinements).

⚡ Local LLM Inference
Runs entirely on your machine using Ollama (no API keys required).

🎨 Clean UI with Tabs
Built using Streamlit for a simple and intuitive user experience.

🛠️ Tech Stack

Python

LangChain

Ollama (local LLM runtime)

Streamlit

LLaMA 3 / Mistral (via Ollama)

📂 Project Structure
DSAss/
│
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
└── venv/                   # (ignored in Git)

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/llm-code-assistant.git
cd llm-code-assistant

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Ollama

Download and install from:
👉 https://ollama.com

Pull a model:

ollama pull llama3:8b


(For low-RAM systems, use mistral)

5️⃣ Run the App
streamlit run app.py


Open browser at:

http://localhost:8501

🧪 Example Use Cases

Understand unfamiliar code quickly

Debug logic errors during DSA practice

Analyze algorithm complexity for interviews

Get optimization hints without full solutions

🧠 Design Highlights

Modular LangChain Runnable pipelines

Prompt-engineered responses (no hardcoding)

Stateless UI with session-based memory

Local inference → privacy + zero API cost

📌 Limitations

No automatic code execution

Depends on LLM reasoning (may vary by model)

Optimized for short to medium-length code snippets

🔮 Future Improvements

🚀 Optimization Suggestions Tab

🧪 Test Case Generator

🔀 Model switch (Local ↔ OpenAI)

🧾 Code refactoring suggestions