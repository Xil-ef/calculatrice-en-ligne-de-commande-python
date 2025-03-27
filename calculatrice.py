def calculer(numb1, numb2, operation):
    """Effectue les opérations arithmétiques de base
    Args :
        numb1 (float) : Le premier nombre.
        numb2 (float) : Le deuxième nombre.
        operation (str) : L'opération à effectuer (+, -, *, /).

    Returns :
        float ou str : Le résultat du calcul ou un message d'erreur."""
    if operation == '+':
        return numb1 + numb2
    elif operation == '-':
        return numb1 - numb2
    elif operation == '*':
        return numb1 * numb2
    elif operation == '/':
        if numb2 == 0:
            return "Erreur : Division par zéro."
        return numb1 / numb2
    else:
        return "Erreur : Opération invalide."

def calculatrice():
    """Fonction principale de la calculatrice."""
    while True:
        try:
            numb1 = float(input("Entrez le premier nombre : "))
            numb2 = float(input("Entrez le deuxième nombre : "))
            operation = input("Choisissez l'opération (+, -, *, /) : ")

            resultat = calculer(numb1, numb2, operation)
            print(f"{numb1} {operation} {numb2} = {resultat}")

            choix = input("Voulez-vous continuer ? (O/N) : ").upper()
            if choix != 'O':
                print("Au revoir !")
                break

        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")

calculatrice()
