from views.report_menu_view import ReportMenuView
from enum import IntEnum
from controllers.players_controller import PlayersController
from controllers.tournaments_controller import TournamentsController


class ReportMenu:
    class Options(IntEnum):
        DEFAULT = 0
        PLAYERS = 1
        TOURNAMENTS = 2
        TOURNAMENT_NAME_DATES = 3
        TOURNAMENT_PLAYERS = 4
        TOURNAMENT_ROUNDS_MATCHES = 5
        EXIT = 6

    def __init__(self):
        self.report_menu_view = ReportMenuView()
        self.player_controller = PlayersController()
        self.tournaments_controller = TournamentsController()

    def loop(self):
        value = ReportMenu.Options.DEFAULT
        while value != ReportMenu.Options.EXIT:
            match value:
                case ReportMenu.Options.PLAYERS:
                    self.player_controller.report_players()
                case ReportMenu.Options.TOURNAMENTS:
                    self.tournaments_controller.report_tournaments()
                case ReportMenu.Options.TOURNAMENT_NAME_DATES:
                    self.tournaments_controller.report_tournament_name_and_dates()
                case ReportMenu.Options.TOURNAMENT_PLAYERS:
                    self.tournaments_controller.report_tournament_players()
                case ReportMenu.Options.TOURNAMENT_ROUNDS_MATCHES:
                    self.tournaments_controller.report_rounds_matches()

            value = ReportMenu.Options(int(ReportMenuView.input_selection(ReportMenu.Options)))
