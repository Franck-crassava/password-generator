import string
import sys
import secrets  # Utilisation du module secrets pour une génération plus sécurisée

# Fonction de génération de mot de passe
def generate_password(length=12, use_digits=True, use_special=True, exclude_chars="", use_secure=True):
    # Caractères possibles pour le mot de passe
    characters = string.ascii_letters  # Lettres majuscules et minuscules
    
    if use_digits:
        characters += string.digits  # Ajoute les chiffres
    
    if use_special:
        characters += string.punctuation  # Ajoute les symboles
    
    # Exclure des caractères spécifiques
    characters = ''.join(c for c in characters if c not in exclude_chars)
    
    # Générer un mot de passe de la longueur demandée
    if use_secure:
        password = ''.join(secrets.choice(characters) for _ in range(length))  # Utilisation de secrets pour plus de sécurité
    else:
        password = ''.join(random.choice(characters) for _ in range(length))  # Utilisation de random si non sécurisé
    
    return password

# Fonction principale
def main():
    # Valeurs par défaut
    length = 12
    use_digits = True
    use_special = True
    exclude_chars = ""  # Liste des caractères à exclure
    use_secure = True  # Par défaut, utilisation de secrets
    
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
        
        if len(sys.argv) > 4:
            exclude_chars = sys.argv[4]  # Les caractères à exclure

        if len(sys.argv) > 5:
            use_secure = sys.argv[5].lower() in ['true', '1', 'yes']
    
    # Générer le mot de passe
    password = generate_password(length, use_digits, use_special, exclude_chars, use_secure)
    
    # Afficher ou sauvegarder le mot de passe
    print("Generated password:", password)

    # Option : Sauvegarde dans un fichier
    with open("generated_password.txt", "w") as f:
        f.write(password)

if __name__ == "__main__":
    main()
