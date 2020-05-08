from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_reciprocity_survey'
    players_per_group = None
    questions = [{'id': 1, 'question': """If someone does me a favor, I am prepared to return it:"""},
                 {'id': 2, 'question': """If I suffer a serious wrong, I will take revenge as soon as possible, no 
                     matter what the cost:"""},
                 {'id': 3, 'question': """If somebody puts me in a difficult position, I will do the same to him/her:"""
                  }, {'id': 4, 'question': """I go out of my way to help somebody who has been kind to me before:"""},
                 {'id': 5, 'question': """If somebody insults me, I will insult him/her back:"""},
                 {'id': 6, 'question': """I am ready to undergo personal costs to help somebody who helped me before:"""
                  }]
    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    submitted_answer = models.IntegerField(choices=range(1, 8, 1), widget=widgets.RadioSelectHorizontal)

    def current_question(self):
        return Constants.questions[self.round_number - 1]
