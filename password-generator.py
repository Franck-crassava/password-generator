import argparse
import random
import string
import secrets

def generate_password(length=12, exclude_chars="", secure=False):
    # Base character set
    characters = string.ascii_letters + string.digits + string.punctuation

    # Remove excluded characters
    for char in exclude_chars:
        characters = characters.replace(char, "")

    if not characters:
        raise ValueError("Character set is empty after exclusions.")

    if secure:
        password = ''.join(secrets.choice(characters) for _ in range(length))
    else:
        password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    parser = argparse.ArgumentParser(description="Customizable Password Generator")
    parser.add_argument("--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--count", type=int, default=1, help="Number of passwords to generate (default: 1)")
    parser.add_argument("--exclude", type=str, default="", help="Characters to exclude from the password")
    parser.add_argument("--save", type=str, help="Filename to save the passwords")
    parser.add_argument("--secure", action="store_true", help="Use secrets module for secure generation")

    args = parser.parse_args()

    passwords = []

    for _ in range(args.count):
        try:
            pwd = generate_password(args.length, args.exclude, args.secure)
            passwords.append(pwd)
        except ValueError as e:
            print(f"Error: {e}")
            return

    for pwd in passwords:
        print(pwd)

    if args.save:
        try:
            with open(args.save, 'w') as f:
                for pwd in passwords:
                    f.write(pwd + '\n')
            print(f"\nPasswords saved to {args.save}")
        except IOError as e:
            print(f"Failed to save file: {e}")

if __name__ == "__main__":
    main()
