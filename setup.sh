#!/bin/bash

# Obtenir le chemin absolu du dossier contenant le script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Dossier du projet (dans le même dossier que ce script)
PROJECT_DIR="$SCRIPT_DIR"

# Créer les dossiers
mkdir -p "$PROJECT_DIR/mistral_cli"

# Créer les fichiers dans mistral_cli/
touch "$PROJECT_DIR/mistral_cli/__init__.py"
touch "$PROJECT_DIR/mistral_cli/main.py"
touch "$PROJECT_DIR/mistral_cli/api.py"
touch "$PROJECT_DIR/mistral_cli/prompts.py"
touch "$PROJECT_DIR/mistral_cli/utils.py"
touch "$PROJECT_DIR/mistral_cli/config.py"

# Créer les fichiers à la racine
touch "$PROJECT_DIR/cli.py"
touch "$PROJECT_DIR/requirements.txt"
touch "$PROJECT_DIR/README.md"
touch "$PROJECT_DIR/setup.py"

echo "Structure de projet créée dans $PROJECT_DIR (namespace : mistral_cli)"
