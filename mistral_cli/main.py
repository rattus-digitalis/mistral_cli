from .utils import (
    save_with_collision_handling,
    copy_to_clipboard,
    run_shell,
    clean_filename
)

def run(question, args):
    role = args.whoami or "default"
    prompt = build_prompt(question, args, role)
    response = ask_mistral(prompt)

    print(response)

    if args.clip:
        copy_to_clipboard(response)

    if args.save:
        save_with_collision_handling(args.save, response)
    elif args.file:
        filename = clean_filename(question)
        save_with_collision_handling(filename, response)

    if args.shell:
        run_shell(response)
