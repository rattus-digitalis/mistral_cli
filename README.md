# mistral_cli

**mistral_cli** is a Python command-line interface (CLI) to interact with the Mistral large language model locally via [Ollama](https://ollama.com).  
No internet connection or API key is required.

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
- Language enforcement (`-lang python|bash|rust`)
- Does not require an OpenAI account

---

## Installation

### 1. Install Ollama and the Mistral model

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run mistral
