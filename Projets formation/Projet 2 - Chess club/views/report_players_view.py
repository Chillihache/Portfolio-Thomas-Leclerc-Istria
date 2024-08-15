class ReportPlayersView:

    @staticmethod
    def show_data_players(players):
        for player in players:
            print(
                f"Nom de famille : {player.last_name}\n"
                f"Prénom : {player.first_name}\n"
                f"Date de naissance : {player.date_of_birth}\n"
                f"Identifiant national d'échecs : {player.chess_code}\n"
                "")

    @staticmethod
    def empty_data_players():
        print("La liste des joueurs est vide ! \n"
              "")
