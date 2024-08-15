class MainMenuView:
    @staticmethod
    def input_selection(options):
        while True:
            print(f"Ajouter un nouveau joueur    - {int(options.ADD_PLAYER)} -\n"
                  f"Gérer les tournois           - {int(options.TOURNAMENTS)} -\n"
                  f"Générer un rapport           - {int(options.REPORTS)} -\n"
                  f"Quitter le programme         - {int(options.EXIT)} -\n"
                  "")
            try:
                choice = int(input("Votre choix : "))
                print("")
                if (choice in [item.value for item in options]) and (choice != 0):
                    return options(choice)
                else:
                    print("Choix invalide. Veuillez sélectionner une option valide.\n"
                          "")
            except ValueError:
                print("Veuillez entrer un nombre valide.\n"
                      "")
