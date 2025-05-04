import os
import subprocess

def clean_filename(text):
    return "_".join(text.lower().strip().split())[:50]

def save_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def copy_to_clipboard(text):
    try:
        subprocess.run("xclip", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        p = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
        p.communicate(input=text.encode())
    except FileNotFoundError:
        print("xclip non trouvé : impossible de copier dans le presse-papier.")

def run_shell(command):
    try:
        os.system(command)
    except Exception as e:
        print(f"Erreur d'exécution : {e}")
