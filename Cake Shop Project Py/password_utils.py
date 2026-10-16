import sys
import msvcrt   # Windows-only module

def input_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""

    while True:
        ch = msvcrt.getch()

        # ENTER key
        if ch == b'\r':
            print()
            break

        # BACKSPACE key
        elif ch == b'\x08':
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()

        # NORMAL character
        else:
            password += ch.decode()
            sys.stdout.write("*")
            sys.stdout.flush()

    return password
