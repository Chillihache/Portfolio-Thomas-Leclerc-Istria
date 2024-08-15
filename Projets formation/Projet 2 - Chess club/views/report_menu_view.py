class ReportMenuView:

    @staticmethod
    def input_selection(options):
        while True:
            print(f"Quel rapport souhaitez-vous générer ? \n"
                  f"Tous les joueurs              - {int(options.PLAYERS)} -\n"
                  f"Tous les tournois             - {int(options.TOURNAMENTS)} -\n"
                  f"Nom et date d'un tournoi      - {int(options.TOURNAMENT_NAME_DATES)} -\n"
                  f"Participants d'un tournoi     - {int(options.TOURNAMENT_PLAYERS)} -\n"
                  f"Tours et matchs d'un tournoi  - {int(options.TOURNAMENT_ROUNDS_MATCHES)} -\n"
                  f"Retour au menu principal      - {int(options.EXIT)} -\n"
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
