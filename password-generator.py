import random
import string
import sys

# Fonction de génération de mot de passe
def generate_password(length=12, use_digits=True, use_special=True):
    # Caractères possibles pour le mot de passe
    characters = string.ascii_letters  # Lettres majuscules et minuscules
    
    if use_digits:
        characters += string.digits  # Ajoute les chiffres
    
    if use_special:
        characters += string.punctuation  # Ajoute les symboles
    
    # Générer un mot de passe de la longueur demandée
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Fonction principale
def main():
    # Valeurs par défaut
    length = 12
    use_digits = True
    use_special = True

    # Lecture des arguments en ligne de commande
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
            if length < 6:
                print("Warning: Password length should be at least 6.")
        except ValueError:
            print("Invalid length, using default of 12.")
        
        if len(sys.argv) > 2:
            use_digits = sys.argv[2].lower() in ['true', '1', 'yes']
        
        if len(sys.argv) > 3:
            use_special = sys.argv[3].lower() in ['true', '1', 'yes']
    
    # Générer le mot de passe
    password = generate_password(length, use_digits, use_special)
    
    # Afficher ou sauvegarder le mot de passe
    print("Generated password:", password)

    # Option : Sauvegarde dans un fichier
    with open("generated_password.txt", "w") as f:
        f.write(password)

if __name__ == "__main__":
    main()
