from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Offer(Page):
    def is_displayed(self):
        return self.player.role() == 'principal'

    form_model = 'group'
    form_fields = ['principal_wage_offer']


class WorkEffort(Page):
    def is_displayed(self):
        return self.player.role() == 'agent'

    form_model = 'group'

    def get_form_fields(self):
        return ['agent_effort_{}'.format(i) for i in range(0, 9+1, 1)]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Offer,
    WorkEffort,
    ResultsWaitPage,
    Results
]
