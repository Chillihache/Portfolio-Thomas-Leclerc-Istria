from models.player import Player
from helpers.json_helper import JsonHelper


class PlayersManager:
    def __init__(self):
        self.json_helper = JsonHelper("data/data_players.json")

    @staticmethod
    def create_new_player(new_player_information):
        new_player_information[0] = new_player_information[0].replace(" ", "")
        new_player_information[1] = new_player_information[1].replace(" ", "")
        new_player = Player(last_name=new_player_information[0], first_name=new_player_information[1],
                            date_of_birth=new_player_information[2], chess_code=new_player_information[3])
        return new_player

    def add_player_in_data(self, new_player):
        data_player = {
            "Last name": new_player.last_name.upper(),
            "First name": new_player.first_name.capitalize(),
            "Date of birth": new_player.date_of_birth,
            "Chess code": new_player.chess_code
        }
        self.json_helper.add_in_data(data=data_player)

    def load_players(self):
        data_players = self.get_data_players()
        players = []
        if data_players:
            for player in data_players:
                players.append(Player(player["Last name"], player["First name"], player["Date of birth"],
                                      player["Chess code"]))
        return players

    def get_data_players(self):
        data_players = self.json_helper.get_data()
        if data_players:
            data_players.sort(key=lambda player: (player["Last name"].lower(), player["First name"].lower()))
        return data_players

    def find_players(self, players_to_find):
        players_found = []
        players = self.load_players()
        for player_to_find in players_to_find:
            for player in players:
                if (player.last_name.lower() == player_to_find[0].lower() and
                        player.first_name.lower() == player_to_find[1].lower()):
                    players_found.append(player)
        if len(players_to_find) == len(players_found):
            return players_found
        else:
            return None
