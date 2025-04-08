# 📝 Password Generator
This script is a simple password generator that allows users to generate strong, customizable passwords based on their preferred settings. You can specify the length, and whether or not to include digits and special characters.

## 🔑 Features
- Generate customizable password length.
- Optionally include digits and special characters.
- Exclude specific characters from the password.
- Use secure cryptographically strong password generation via the `secrets` module.
- Option to generate multiple passwords at once.

## 🖥️ Usage
You can specify the following options:
- `length` (integer): Password length (default: 12).
- `use_digits` (boolean): Include digits (`true` or `false`; default: `true`).
- `use_special` (boolean): Include special characters (`true` or `false`; default: `true`).
- `exclude_chars` (string): Characters to exclude from the password (e.g., "0lI" to exclude `0`, `l`, and `I`).
- `use_secure` (boolean): Use the secure `secrets` module for password generation (`true` or `false`; default: `true`).
- `num_passwords` (integer): Generate multiple passwords at once (optional).

## Command Line Arguments:

### Examples
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
```bash
Generated password: Y5$3Gd1!Kl9P
The password will also be written to the file generated_password.txt.
```
## ⚙️ Customization
The script can be easily modified to:

Change the default password length.

Adjust which character sets are included (e.g., including/excluding specific special characters).

Add more features such as custom character sets or multiple password generation at once.

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
## 🛠️ Dependencies
This script is written in Python and uses the built-in random, string, and sys modules, so no additional dependencies are required.

## 📜 License
This project is licensed under the MIT License.
