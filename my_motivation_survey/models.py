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
    name_in_url = 'my_motivation_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        player = self.get_players()

        data = []

        social_you = [p.social_impact_you for p in player if p.social_impact_you is not None]
        if len(social_you) == 0:
            avg_social_you = 0
        else:
            avg_social_you = sum(social_you) / len(social_you)
        data.append(avg_social_you)

        social_others = [p.social_impact_others for p in player if p.social_impact_others is not None]
        if len(social_others) == 0:
            avg_social_others = 0
        else:
            avg_social_others = sum(social_others) / len(social_others)
        data.append(avg_social_others)

        money_you = [p.money_you for p in player if p.money_you is not None]
        if len(money_you) == 0:
            avg_money_you = 0
        else:
            avg_money_you = sum(money_you) / len(money_you)
        data.append(avg_money_you)

        money_others = [p.money_others for p in player if p.money_others is not None]
        if len(money_others) == 0:
            avg_money_others = 0
        else:
            avg_money_others = sum(money_others) / len(money_others)
        data.append(avg_money_others)

        recognition_you = [p.recognition_you for p in player if p.recognition_you is not None]
        if len(recognition_you) == 0:
            avg_recognition_you = 0
        else:
            avg_recognition_you = sum(recognition_you) / len(recognition_you)
        data.append(avg_recognition_you)

        recognition_others = [p.recognition_others for p in player if p.recognition_others is not None]
        if len(recognition_others) == 0:
            avg_recognition_others = 0
        else:
            avg_recognition_others = sum(recognition_others) / len(recognition_others)
        data.append(avg_recognition_others)

        autonomy_you = [p.autonomy_you for p in player if p.autonomy_you is not None]
        if len(autonomy_you) == 0:
            avg_autonomy_you = 0
        else:
            avg_autonomy_you = sum(autonomy_you) / len(autonomy_you)
        data.append(avg_autonomy_you)

        autonomy_others = [p.autonomy_others for p in player if p.autonomy_others is not None]
        if len(autonomy_others) == 0:
            avg_autonomy_others = 0
        else:
            avg_autonomy_others = sum(autonomy_others) / len(autonomy_others)
        data.append(avg_autonomy_others)

        environment_you = [p.working_env_you for p in player if p.working_env_you is not None]
        if len(environment_you) == 0:
            avg_environment_you = 0
        else:
            avg_environment_you = sum(environment_you) / len(environment_you)
        data.append(avg_environment_you)

        environment_others = [p.working_env_others for p in player if p.working_env_others is not None]
        if len(environment_others) == 0:
            avg_environment_others = 0
        else:
            avg_environment_others = sum(environment_others) / len(environment_others)
        data.append(avg_environment_others)

        return {'highchart_data': data}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    c_range = range(0, 11, 1)
    labels = ["Social impact (e.g., want to make a difference for the world):",
              "Money and prestige (e.g., reach high socio-economic status):",
              """Intellectual challenge & recognition (e.g., apply your skills and talent to solve a problem, 
              being recognized for your competence):""", """Autonomy (e.g., being able of making decisions, taking 
              initiatives, being independent, organize your work as you like):""", """Nice working environment (e.g., 
              being treated fairly, getting along well with boss and colleagues, non-monetary perks like good mensa):
              """]
    
    social_impact_you = models.IntegerField(label=labels[0], choices=c_range, widget=widgets.RadioSelectHorizontal)
    social_impact_others = models.IntegerField(label=labels[0], choices=c_range, widget=widgets.RadioSelectHorizontal)
    money_you = models.IntegerField(label=labels[1], choices=c_range, widget=widgets.RadioSelectHorizontal)
    money_others = models.IntegerField(label=labels[1], choices=c_range, widget=widgets.RadioSelectHorizontal)
    recognition_you = models.IntegerField(label=labels[2], choices=c_range, widget=widgets.RadioSelectHorizontal)
    recognition_others = models.IntegerField(label=labels[2], choices=c_range, widget=widgets.RadioSelectHorizontal)
    autonomy_you = models.IntegerField(label=labels[3], choices=c_range, widget=widgets.RadioSelectHorizontal)
    autonomy_others = models.IntegerField(label=labels[3], choices=c_range, widget=widgets.RadioSelectHorizontal)
    working_env_you = models.IntegerField(label=labels[4], choices=c_range, widget=widgets.RadioSelectHorizontal)
    working_env_others = models.IntegerField(label=labels[4], choices=c_range, widget=widgets.RadioSelectHorizontal)

    difference_social_impact = models.IntegerField()
    difference_money = models.IntegerField()
    difference_recognition = models.IntegerField()
    difference_autonomy = models.IntegerField()
    difference_working_env = models.IntegerField()

    def calc_difference(self):
        self.difference_social_impact = abs(self.social_impact_you - self.social_impact_others)
        self.difference_money = abs(self.money_you - self.money_others)
        self.difference_recognition = abs(self.recognition_you - self.recognition_others)
        self.difference_autonomy = abs(self.autonomy_you - self.autonomy_others)
        self.difference_working_env = abs(self.working_env_you - self.working_env_others)
        
