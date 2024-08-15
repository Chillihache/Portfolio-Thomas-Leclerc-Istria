from helpers.input_helper import InputHelper


class AddPlayerView:

    def __init__(self):
        self.input_helper = InputHelper()

    def ask_new_player_information(self):
        last_name = input("Entrer le nom de famille du nouveau joueur : ")
        first_name = input("Entrer le prénom du nouveau joueur : ")
        date_of_birth = input("Entrer la date de naissance du nouveau joueur au format JJ/MM/AAAA : ")
        date_of_birth = self.input_helper.check_date(date_of_birth)
        chess_code = input("Entrer l'identifiant national d'échecs (deux lettres suivies de cinq chiffres) : ")
        chess_code = self.input_helper.check_chess_code(chess_code)
        print("")
        return [last_name, first_name, date_of_birth, chess_code]

    @staticmethod
    def player_created():
        print(
            "Le joueur a été créé !\n"
            ""
            )
