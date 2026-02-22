<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="Bindu Logo" width="200">
</p>

<h1 align="center">Research Assistant Agent</h1>

<p align="center">
  <strong>A research assistant that finds and summarizes information using OpenRouter models.</strong>
</p>

---

## 📖 Overview

This project implements a Research Assistant Agent built using the Bindu Agent Framework.

The agent accepts user messages and generates research-based responses using OpenRouter models. It is designed to be simple, testable, and production-ready.

This submission includes:
- Fully working async handler
- Proper agent initialization
- Passing pytest test cases
- Secure environment variable handling
- Clean project structure

---

## 🚀 Key Capabilities

- 🔍 Searches and summarizes information using OpenRouter models
- 🧠 Accepts structured message input format
- ⚡ Async handler implementation
- ✅ Fully tested with pytest
- 🔧 Compatible with Bindu's `bindufy` framework

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenRouter API
- Bindu Agent Framework
- pytest (for testing)

---

## 📂 Project Structure
research-assistant-agent/
├── research_assistant_agent/
│ ├── init.py
│ ├── main.py
│ └── agent_config.json
├── tests/
│ └── test_main.py
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/estherdcruz04-hub/research-assistant-agent.git
cd research-assistant-agent

#virtual environment 
python -m venv .venv
.venv\Scripts\activate   # On Windows

# install dependencies 
pip install -r requirements.txt

#create.env 
OPENROUTER_API_KEY=your_openrouter_api_key_here

Run the Agent
python -m research_assistant_agent.main

The agent runs as a backend service using bindufy.

Note:
This agent does not provide a browser UI by default. It runs as a backend service and listens for API-based interactions.

🧪 Running Tests
pytest tests/test_main.py -v

All tests pass successfully.

💬 Example Usage

Example input message:

[
  {"role": "user", "content": "Explain quantum computing in simple terms."}
]

The handler processes the message and returns a structured response from the model.

🔐 Security

.env is excluded using .gitignore

API keys are not committed to the repository

Virtual environment files are ignored

📄 License

This project is licensed under the MIT License.

🙏 Powered by Bindu

Built using the Bindu Agent Framework for building modular AI agents.


---

# ✅ That’s It

After pasting:

1. Click **Commit changes**
2. Make sure repo is Public
3. Confirm `.env` is NOT visible
4. Submit your GitHub link

You are ready.  
No more changes needed.

If you want, I can now do a final “submission readiness” check with you in 60 seconds.