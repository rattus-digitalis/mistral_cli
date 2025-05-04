from openai import OpenAI

def ask_mistral(prompt):
    client = OpenAI(
        base_url="http://localhost:11434/v1",  # API Ollama
        api_key="ollama"  # clé factice, requise mais ignorée
    )
    response = client.chat.completions.create(
        model="mistral",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )
    return response.choices[0].message.content.strip()
