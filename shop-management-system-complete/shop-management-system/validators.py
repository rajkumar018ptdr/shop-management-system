def text(prompt):
    while True:
        x=input(prompt).strip()
        if x: return x
        print("Value cannot be empty.")

def integer(prompt, minimum=0):
    while True:
        try:
            x=int(input(prompt))
            if x>=minimum: return x
        except ValueError: pass
        print(f"Enter an integer >= {minimum}.")

def number(prompt, minimum=0.0):
    while True:
        try:
            x=float(input(prompt))
            if x>=minimum: return x
        except ValueError: pass
        print(f"Enter a number >= {minimum}.")
