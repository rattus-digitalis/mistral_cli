def build_prompt(question, args, role):
    context = ""
    if args.dev:
        context += "Tu es un développeur expérimenté. Explique avec du code clair et commenté. "
    if args.cyber:
        context += "Tu es un expert en cybersécurité. Sois technique et précis. "
    if args.rapide:
        context += "Réponds de façon concise. "
    if args.détail:
        context += "Fais une réponse complète et pédagogique. "
    if args.lang:
        context += f"Utilise uniquement le langage {args.lang}. "
    if args.json:
        context += "Réponds au format JSON. "
    if args.code:
        context += "Ne donne que du code, sans explication. "
    return context + "\n" + question
