def afficher_menu():
    print("\n=== MENU DES BOISSONS ===")
    print("1 - Café")
    print("2 - Thé")
    print("3 - Eau chaude")
    print("4 - Quitter")

def traiter_choix(choix, compteur):
    if choix == "1":
        print("Vous avez choisi : Café ")
        compteur["café"] += 1
    elif choix == "2":
        print("Vous avez choisi : Thé ")
        compteur["thé"] += 1
    elif choix == "3":
        print("Vous avez choisi : Eau chaude ")
        compteur["eau chaude"] += 1
    elif choix == "4":
        print("Merci et à bientôt ")
    else:
        print("Choix invalide ")
    return compteur

def afficher_resume(compteur):
    print("\n=== RÉSUMÉ DES COMMANDES ===")
    for boisson, nombre in compteur.items():
        print(f"{nombre} {boisson}(s)")

# Initialisation du compteur de choix
compteur_choix = {
    "café": 0,
    "thé": 0,
    "eau chaude": 0
}

# Programme principal
while True:
    afficher_menu()
    choix_utilisateur = input("Que souhaitez-vous bois ? : ")
    if choix_utilisateur == "4":
        break
    compteur_choix = traiter_choix(choix_utilisateur, compteur_choix)

afficher_resume(compteur_choix)
