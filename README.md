# 🔐 Password Generator

A flexible and customizable command-line password generator written in Python.  
Perfect for creating strong passwords with options for security, character exclusions, saving to file, and more.

---

## 🚀 Features

- Generate one or multiple passwords at once
- Customize password length
- Exclude specific characters (e.g., symbols or similar characters)
- Optional use of the `secrets` module for cryptographic-grade security
- Save passwords to a file of your choice
- Easy CLI interface with argparse

---

## ⚙️ Usage

```bash
python password-generator.py [OPTIONS]
```
Available Options : 
Argument	Description
--length	Length of the password(s) (default: 12)
--count	Number of passwords to generate (default: 1)
--exclude	Characters to exclude (e.g. @#%lIO0)
--secure	Use the secrets module for strong cryptographic randomness
--save	Save generated passwords to a file (e.g., output.txt)
-h, --help	Display the help message

## Examples
Default (12 characters, with digits and special characters):

```bash
python password-generator.py
Custom length (16 characters, with digits but no special characters):
```
```bash
python password-generator.py 16 true false
Custom length (8 characters, no digits and no special characters):
```
```bash
python password-generator.py 8 false false
💾 Output
Console: The generated password will be displayed in the terminal.

File: The generated password will be saved in generated_password.txt.
```

## Example Output:
Generate a single 12-character password:

```bash
python password-generator.py
Generate 5 passwords of length 20:
```

```bash
python password-generator.py --length 20 --count 5
Generate secure passwords and save them to a file:
```
```bash
python password-generator.py --secure --count 3 --save passwords.txt
Exclude confusing characters like O, 0, l, and 1:
```

```bash
python password-generator.py --exclude "O0l1" --count 2
```

## 🚀 Installation
Clone this repository:

```bash
git clone https://github.com/yourusername/password-generator.git
Navigate to the project directory:
```
```bash
cd password-generator
Run the script using Python:
```
```bash
python password-generator.py
```

## 🔒 Security Considerations
Using the --secure flag activates the secrets module, which provides cryptographically secure random generation.

If you're generating passwords for real users or production systems, it's highly recommended to use --secure.

## 📁 Requirements
Python 3.6 or higher

No external libraries required (only built-in modules)

## 🛠️ Dependencies
This script is written in Python and uses the built-in random, string, and sys modules, so no additional dependencies are required.

## 📜 License
This project is licensed under the MIT License.

## ✨ Author
Franck CRASSAVA – Cybersecurity & Network Architecture Student
