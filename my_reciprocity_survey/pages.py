from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):

    form_model = 'player'
    form_fields = ['submitted_answer']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds
        return {'player_in_all_rounds': player_in_all_rounds}


page_sequence = [Question, Results]
