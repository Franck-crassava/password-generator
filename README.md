# Password Generator

This is a simple password generator that allows you to create strong passwords with customizable options.

## Usage

You can specify the following options:
- Length of the password (default: 12)
- Whether to include digits (default: yes)
- Whether to include special characters (default: yes)

### Command Line Arguments:
- `length` (integer): Password length (default: 12)
- `use_digits` (boolean): Include digits (`true`/`false`, default: true)
- `use_special` (boolean): Include special characters (`true`/`false`, default: true)

## Example:
```bash
python password-generator.py 16 true true
This will generate a 16-character password with digits and special characters.
```

The generated password will be printed on the screen and saved in generated_password.txt.

## License
This project is licensed under the MIT License.

