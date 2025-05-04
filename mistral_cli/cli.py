#!/usr/bin/env python3
import argparse
from mistral_cli.main import run

def main():
    parser = argparse.ArgumentParser(description="Interface CLI pour Mistral via Ollama.")
    parser.add_argument("question", nargs="+", help="Votre question à Mistral.")
    parser.add_argument("-cyber", action="store_true", help="Mode cybersécurité.")
    parser.add_argument("-dev", action="store_true", help="Mode développeur.")
    parser.add_argument("-rapide", action="store_true", help="Réponse concise.")
    parser.add_argument("-détail", action="store_true", help="Réponse détaillée.")
    parser.add_argument("-file", action="store_true", help="Sauvegarde dans un fichier.")
    parser.add_argument("-lang", choices=["python", "bash", "rust"], help="Langage imposé.")
    parser.add_argument("-clip", action="store_true", help="Copie dans le presse-papiers.")
    parser.add_argument("-json", action="store_true", help="Format JSON.")
    parser.add_argument("-code", action="store_true", help="Code seulement.")
    parser.add_argument("-shell", action="store_true", help="Exécuter la commande retournée.")
    parser.add_argument("-save", metavar="FILENAME", help="Sauvegarde sous un nom précis.")
    parser.add_argument("-whoami", metavar="ROLE", help="Personnaliser le rôle utilisateur.")

    args = parser.parse_args()
    question = " ".join(args.question)
    run(question, args)

if __name__ == "__main__":
    main()
