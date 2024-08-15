class ReportTournamentsView:

    @staticmethod
    def show_tournaments_list(tournaments):
        print("Voici la liste des tournois : \n"
              "")
        for tournament in tournaments:
            print(tournament.name)
        print("")

    @staticmethod
    def tournaments_empty():
        print("La liste des tournois est vide ! \n"
              "")

    @staticmethod
    def ask_tournament_name():
        tournament_name = input("Entrer le nom du tournoi : ")
        print("")
        return tournament_name

    @staticmethod
    def show_tournament_name_dates(tournament):
        if tournament:
            print(f"Nom du tournoi : {tournament.name} \n"
                  f"Date de début : {tournament.start_date} \n"
                  f"Date de fin : {tournament.end_date} \n"
                  "")
        else:
            print("Aucun tournoi n'a été trouvé. \n"
                  "")

    @staticmethod
    def show_tournament_rounds_matches(tournament):
        for i in range(len(tournament.rounds)):
            print(f"{tournament.rounds[i].name} \n"
                  f"Date de début : {tournament.rounds[i].start_date} \n"
                  f"Date de fin : {tournament.rounds[i].end_date}"
                  )
            for match in tournament.rounds[i].matches:
                print(match)
            print("")
