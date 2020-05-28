from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Page1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = ['choice']


class Page2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        payoffs = self.group.get_vars('payoff')
        choices = self.group.get_vars('choice')
        cum_payoff = [sum(self.group.get_vars('payoff')[0]), sum(self.group.get_vars('payoff')[1])]
        choice = self.group.get_choices()
        p1_payoff = payoffs[0]
        p2_payoff = payoffs[1]

        if self.player.id_in_group == 1:
            return {'cum_payoff_1': cum_payoff[0], 'cum_payoff_2': cum_payoff[1],
                    'cumulative_payoff_1': cum_payoff[0],
                    'player_choice_1': choice[0], 'player_choice_2': choice[1],
                    'player_choices_1': choices[0], 'player_choices_2': choices[1],
                    'player_payoff_1': p1_payoff[self.round_number-1],
                    'player_payoff_2': p2_payoff[self.round_number-1],
                    'player_payoffs_1': payoffs[0], 'player_payoffs_2': payoffs[1]}
        else:
            return {'cum_payoff_1': cum_payoff[0], 'cum_payoff_2': cum_payoff[1],
                    'cumulative_payoff_2': cum_payoff[1],
                    'player_choice_1': choice[0], 'player_choice_2': choice[1],
                    'player_choices_1': choices[0], 'player_choices_2': choices[1],
                    'player_payoff_1': p1_payoff[self.round_number-1],
                    'player_payoff_2': p2_payoff[self.round_number-1],
                    'player_payoffs_1': payoffs[0], 'player_payoffs_2': payoffs[1]}


page_sequence = [
    Introduction,
    Page1,
    Page2,
    ResultsWaitPage,
    Results
]
