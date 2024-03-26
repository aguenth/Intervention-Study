import random
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'end'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.session.config['language'] == 'mx':
        from .lexicon_mx import Lexicon
        subsession.session.myLangCode = "_mx"
    elif subsession.session.config['language'] == 'za':
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_za"
    elif subsession.session.config['language'] == 'uk':
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_uk"
    else:
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_en"
    subsession.session.endLexi = Lexicon


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class end(Page):
    form_model = 'player'
    form_fields = []

    @staticmethod
    def vars_for_template(player: Player):
        lang = player.subsession.session.config['language']
        if lang == 'za':
            redirect_url = "https://app.prolific.com/submissions/complete?cc=AAAAAAA"
        elif lang == 'mx':
            redirect_url = "https://app.prolific.com/submissions/complete?cc=XXXXXXX"
        elif lang == 'uk':
            redirect_url = "https://app.prolific.com/submissions/complete?cc=YYYYYYY"
        else:
            redirect_url = "https://app.prolific.com/submissions/complete?cc=CJOS4RKJ"

        return {
            'redirect_url': redirect_url,
            'Lexicon': player.session.endLexi,
        }


# Page sequence
page_sequence = [
    end
]
