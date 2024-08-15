from models.players_manager import PlayersManager
from views.add_player_view import AddPlayerView
from views.report_players_view import ReportPlayersView


class PlayersController:

    def __init__(self):
        self.player_manager = PlayersManager()
        self.add_player_view = AddPlayerView()
        self.report_players_view = ReportPlayersView()

    def add_player(self):
        new_player_information = self.add_player_view.ask_new_player_information()
        new_player = self.player_manager.create_new_player(new_player_information)
        self.player_manager.add_player_in_data(new_player)
        self.add_player_view.player_created()

    def report_players(self):
        players = self.player_manager.load_players()
        if players:
            self.report_players_view.show_data_players(players)
        else:
            self.report_players_view.empty_data_players()
