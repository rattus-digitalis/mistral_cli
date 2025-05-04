from .api import ask_mistral
from .prompts import build_prompt
from .utils import save_to_file, copy_to_clipboard, run_shell, clean_filename

def run(question, args):
    role = args.whoami or "default"
    prompt = build_prompt(question, args, role)
    response = ask_mistral(prompt)

    print(response)

    if args.clip:
        copy_to_clipboard(response)
    if args.file or args.save:
        filename = args.save or clean_filename(question)
        save_to_file(filename + ".txt", response)
    if args.shell:
        run_shell(response)
