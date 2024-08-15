from datetime import datetime


class InputHelper:

    def check_date(self, date):

        while not self.valid_date(date):
            print("Cette date n'est pas valable.")
            date = input("Veuillez entrer une date au format JJ/MM/AAAA : ")
        return date

    @staticmethod
    def valid_date(date):
        try:
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def check_chess_code(chess_code):
        while len(chess_code) != 7 or not (chess_code[:2].isalpha() and chess_code[2:].isdigit()):
            print("Ce code n'est pas valide.")
            chess_code = input("Veuillez entrer un code au format AB12345 : ")
        return chess_code.upper()

    @staticmethod
    def check_int(number):
        while not number.isdigit():
            number = input("Veuillez entrer un nombre entier : ")
        return int(number)

    @staticmethod
    def check_even_int(number):
        while not number.isdigit() or not int(number) % 2 == 0 or int(number) == 0:
            number = input("Veuillez entrer un nombre pair : ")
        return int(number)
