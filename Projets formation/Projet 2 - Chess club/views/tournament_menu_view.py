class TournamentMenuView:
    @staticmethod
    def input_selection(options):
        while True:
            print(f"Créer un nouveau tournoi    - {int(options.CREATE)} -\n"
                  f"Gérer un tournoi            - {int(options.MANAGE)} -\n"
                  f"Retour au menu principal    - {int(options.EXIT)} -\n"
                  "")
            try:
                choice = int(input("Votre choix : "))
                print("")
                if (choice in [item.value for item in options]) and (choice != 0):
                    return options(choice)
                else:
                    print("Choix invalide. Veuillez sélectionner une option valide. \n"
                          "")
            except ValueError:
                print("Veuillez entrer un nombre valide. \n"
                      "")
