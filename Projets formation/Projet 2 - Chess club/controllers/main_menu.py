from views.main_menu_view import MainMenuView
from enum import IntEnum
from controllers.tournament_menu import TournamentMenu
from controllers.report_menu import ReportMenu
from controllers.players_controller import PlayersController


class MainMenu:
    class Options(IntEnum):
        DEFAULT = 0
        ADD_PLAYER = 1
        TOURNAMENTS = 2
        REPORTS = 3
        EXIT = 4

    def __init__(self):
        self.player_controller = PlayersController()
        self.tournament_menu = TournamentMenu()
        self.report_menu = ReportMenu()

    def main_loop(self):
        value = MainMenu.Options.DEFAULT
        while value != MainMenu.Options.EXIT:
            match value:
                case MainMenu.Options.ADD_PLAYER:
                    self.player_controller.add_player()
                case MainMenu.Options.TOURNAMENTS:
                    self.tournament_menu.loop()
                case MainMenu.Options.REPORTS:
                    self.report_menu.loop()

            value = MainMenu.Options(int(MainMenuView.input_selection(MainMenu.Options)))
