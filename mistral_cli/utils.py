import os
import subprocess

def clean_filename(text):
    return "_".join(text.lower().strip().split())[:50]

def save_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def save_with_collision_handling(base_name: str, content: str, extension: str = ".txt"):
    # Évite le double .txt si l'utilisateur fournit déjà une extension
    if base_name.endswith(extension):
        base_name = base_name[:-len(extension)]

    filename = f"{base_name}{extension}"
    counter = 1

    # Incrémente jusqu'à ce que le fichier soit unique
    while os.path.exists(filename):
        filename = f"{base_name}_{counter}{extension}"
        counter += 1

    with open(filename, "w") as f:
        f.write(content)

    print(f"Response saved to: {filename}")

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
