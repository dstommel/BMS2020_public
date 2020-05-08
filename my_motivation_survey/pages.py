from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page_One(Page):
    form_model = 'player'
    form_fields = ['social_impact_you', 'money_you', 'recognition_you', 'autonomy_you', 'working_env_you']


class Page_Two(Page):
    form_model = 'player'
    form_fields = ['social_impact_others', 'money_others', 'recognition_others', 'autonomy_others', 'working_env_others']

    def before_next_page(self):
        self.player.calc_difference()


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [Page_One, Page_Two, Results]
