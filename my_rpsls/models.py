from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'David Stommel'

doc = ""


class Constants(BaseConstants):
    name_in_url = 'my_rpsls'
    players_per_group = 2
    num_rounds = 3
    instructions_template = 'my_rpsls/Instructions.html'
    last_round_table = 'my_rpsls/last_round_table.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def get_choices(self):
        choices = []
        for p in self.get_players():
            choices.append(p.choice)
        return choices

    def set_payoffs(self):
        choices = self.get_choices()
        player1 = self.get_player_by_id(1)
        player2 = self.get_player_by_id(2)

        if rules(choices) == 'draw':
            player1.payoff = 0
            player2.payoff = 0
        if player1.choice == rules(choices):
            player1.payoff = 1
            player2.payoff = -1
        if player2.choice == rules(choices):
            player1.payoff = -1
            player2.payoff = 1

    def get_vars(self, var_name):
        var_list = []
        for p in self.get_players():
            var_list_player = []
            for i in p.in_all_rounds():
                var_list_player.append(getattr(i, var_name))
            var_list.append(var_list_player)
        return var_list


def rules(choices):
    choice_a = choices[0]
    choice_b = choices[1]
    alt_a = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
    alt_b = ['Scissors', 'Spock', 'Lizard', 'Rock', 'Paper', 'Scissors', 'Spock']
    i = alt_a.index(choice_a)
    if choice_b == alt_b[i] or choice_b == alt_b[i + 2]:
        return choice_a
    else:
        if choice_a == choice_b:
            return 'draw'
        else:
            return choice_b


class Player(BasePlayer):
    choice = models.StringField(label='Make your choice:', choices=['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'],
                                widget=widgets.RadioSelect)
