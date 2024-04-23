from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.session.config['language'] == 'mx':
        from .lexicon_mx import Lexicon
        subsession.session.myLangCode = "_mx"
    elif subsession.session.config['language'] == 'za':
        from .lexicon_za import Lexicon
        subsession.session.myLangCode = "_za"
    elif subsession.session.config['language'] == 'uk':
        from .lexicon_uk import Lexicon
        subsession.session.myLangCode = "_uk"
    else:
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_en"
    subsession.session.introLexi = Lexicon


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Consent fields
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)

    is_mobile = models.BooleanField()


class introduction_consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'Lexicon': player.session.introLexi,
            "participantlabel": player.participant.label,
        }  # add ?participant_label={{%PROLIFIC_PID%}} to link on prolific


class MobileCheck(Page):
    form_model = 'player'
    form_fields = ['is_mobile']

    def vars_for_template(player: Player):
        return {
            'Lexicon': player.session.introLexi,
        }

    def error_message(player: Player, values):
        if values['is_mobile']:
            return player.session.introLexi.mobile


page_sequence = [
    MobileCheck,
    introduction_consent
]
