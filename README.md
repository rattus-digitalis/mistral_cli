# mistral_cli

**mistral_cli** is a Python command-line interface (CLI) to interact with the Mistral large language model locally via [Ollama](https://ollama.com). No internet connection or API key is required.

---

## Features

- Fully offline: works without any internet access
- Specialized response modes:
  - `-cyber` for cybersecurity and penetration testing
  - `-dev` for developer-oriented answers with clear, commented code
  - `-rapide` for short, concise answers
  - `-détail` for complete, educational responses
- Automatic saving:
  - `-file` to save with a name based on the question
  - `-save name` to save with a custom filename
- Copy response to clipboard (`-clip`)
- Execute shell commands (`-shell`)
- Language enforcement (`-lang python bash|rust`)
- Does not require an OpenAI account

---

## Installation

### 1. Install Ollama and the Mistral model

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run mistral

2. Clone the mistral_cli repository and set up the environment

git clone git@github.com\:rattus-digitalis/mistral_cli.git
cd mistral_cli
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

Usage

mistral -dev "write a Python function to add two numbers"
mistral -cyber -détail "nmap command to scan for vulnerabilities"
mistral -cyber -save scan_nmap "nmap command to scan a target network"

Available Options
Option	Description
-cyber	Cybersecurity expert mode
-dev	Developer mode with code examples
-rapide	Short, concise response
-détail	Detailed and educational response
-lang	Force output language: python, bash, rust
-clip	Copy output to clipboard
-file	Save response with an auto-generated filename
-save	Save response with a custom filename
-shell	Execute the returned command as a shell command
-whoami	Set a custom user role (for future extensions)
Project Structure

mistral_cli/
├── mistral_cli/
│   ├── api.py
│   ├── cli.py
│   ├── config.py
│   ├── main.py
│   ├── prompts.py
│   └── utils.py
├── README.md
├── requirements.txt
├── setup.py
└── .venv/

License

This project is licensed under the MIT License.