from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'task_intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.session.config['language'] == 'mx':
        from .lexicon_mx import Lexicon
        subsession.session.myLangCode = "_mx"
    else:
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_en"
    subsession.session.tracking_introLexi = Lexicon


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    teacher = models.StringField(widget=widgets.RadioSelectHorizontal)

def teacher_choices(player):
    Lexicon = player.session.tracking_introLexi
    teacher_choices = [
        ["marketing", Lexicon.marketing],
        ["philosophy", Lexicon.philosophy],
        ["spanish", Lexicon.spanish]
    ]
    return teacher_choices

    # teacher = models.StringField(
    #    choices=["Marketing", "Philosophy", "Spanish"],
    #    widget=widgets.RadioSelectHorizontal,
    # )


class HoverEvent(models.ExtraModel):
    player = models.Link(Player)
    element_id = models.StringField()
    enter_time = models.FloatField()
    leave_time = models.FloatField()
    duration = models.IntegerField()
    attributeType = models.StringField()
    attributeValue = models.StringField()


def custom_export(players):
    yield ["session", "participant_code", "round_number", "id_in_group", "element_id", "enter_time", "leave_time",
           "duration", "attributeType", "attributeValue", "buyEV"]
    for player in players:
        for e in HoverEvent.filter(player=player):
            yield [
                player.session.code,
                player.participant.code,
                player.round_number,
                player.id_in_group,
                e.element_id,
                e.enter_time,
                e.leave_time,
                e.duration,
                e.attributeType,
                e.attributeValue,
                player.teacher,
            ]


class instructions(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.tracking_introLexi)


class Tracker_demo(Page):
    form_model = 'player'
    form_fields = ['teacher']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.tracking_introLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.tracking_introLexi
        return dict(
            form_fields=['teacher'],
            form_field_labels=[Lexicon.teacher_label]
        )


class practice_completed_template(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.tracking_introLexi)


# Page sequence
page_sequence = [
    instructions,
    Tracker_demo,
    practice_completed_template
]
