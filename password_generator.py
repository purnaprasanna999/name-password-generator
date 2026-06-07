# Name-Based Password Generator
import random
import string

def generate_password(name, length):
    name = name.lower()
    extras = string.digits + "!@#$%^&*"
    remaining = length - len(name)
    extra_chars = "".join(random.choice(extras) for _ in range(remaining))
    password = name + extra_chars
    return password

def main():
    print("===== Name-Based Password Generator =====")
    name = input("Enter your name: ").strip()
    if not name.isalpha():
        print("Please enter letters only.")
        return
    length = int(input("Enter total password length: "))
    if length < len(name):
        length = len(name)
        print(f"Length auto-set to {length}")
    password = generate_password(name, length)
    print(f"\nHello, {name}!")
    print(f"Your Password: {password}")
    print("Keep it safe!")

if __name__ == "__main__":
    main()