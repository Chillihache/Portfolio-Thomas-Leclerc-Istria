import random


class ManageTournamentView:

    @staticmethod
    def tournament_not_found():
        print("Aucun tournoi correspondant n'a été trouvé, veuillez vérifier dans la liste des tournois. \n"
              "")

    @staticmethod
    def generate_round(current_round):
        input(f"Appuyez sur entrer pour générer le round {current_round}")
        print("")

    @staticmethod
    def round_generated(tournament):
        print(f"Le tour {tournament.current_round} a été généré. \n"
              "Voici les matchs pour ce tour : \n"
              "")
        for match in tournament.rounds[tournament.current_round - 1].matches:
            print(match)
            print(f"{random.choice([match[0][0], match[1][0]])} jouera les blancs. \n"
                  "")

    @staticmethod
    def ask_winner(match):
        max_len = max(len(match[0][0]), len(match[1][0]), len("Egalité"))
        print(f"Sélectionnez le vainqueur du match {match} \n"
              f"{match[0][0]:<{max_len}} - 1 - \n"
              f"{match[1][0]:<{max_len}} - 2 - \n"
              f"{'Egalité':<{max_len}} - 3 - \n"
              "")
        choice = int(input("Votre choix : "))
        print("")
        return choice

    @staticmethod
    def show_winners(tournament):
        print(f"Voici les scores du tour {tournament.current_round} \n"
              "")
        for match in tournament.rounds[tournament.current_round-1].matches:
            print(match)
        print("")

    @staticmethod
    def tournament_closed():
        print("Le tournoi est terminé ! \n"
              "")
