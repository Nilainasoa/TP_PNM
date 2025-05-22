def afficher_menu():
    print("Que souhaitez-vous ?")
    print("1 - Café")
    print("2 - Thé")
    print("3 - Eau chaude")
    print("4 - Quitter")

def traiter_choix(choix):
    if choix == "1":
        print("Vous avez choisi un café .")
    elif choix == "2":
        print("Vous avez choisi un thé .")
    elif choix == "3":
        print("Vous avez choisi de l'eau chaude .")
    elif choix == "4":
        print("Au revoir 👋.")
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

if __name__ == "__main__":
    while True:
        afficher_menu()
        choix_utilisateur = input("Entrez votre choix : ")
        traiter_choix(choix_utilisateur)
        if choix_utilisateur == "4":
            break
