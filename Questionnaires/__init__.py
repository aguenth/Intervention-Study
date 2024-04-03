import random
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
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
    subsession.session.questionnairesLexi = Lexicon


def make_likert6():
    return models.IntegerField(
        choices=[1,2,3,4,5,6],
            widget=widgets.RadioSelect,
    )


def make_likert10():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            widget=widgets.RadioSelect,
        )


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # questionnaire
    conservative_liberal = make_likert10()

    cc_concern1 = make_likert6()
    cc_concern2 = make_likert6()
    cc_concern3 = make_likert6()
    cc_concern4 = make_likert6()

    ev_prob_benefits1 = make_likert6()
    ev_prob_benefits2 = make_likert6()
    ev_prob_benefits3 = make_likert6()
    ev_prob_benefits4 = make_likert6()

    ev_prob_risks1 = make_likert6()
    ev_prob_risks2 = make_likert6()

    ev_perceived_benefit1 = make_likert6()
    ev_perceived_benefit2 = make_likert6()

    ev_perceived_risk1 = make_likert6()
    ev_perceived_risk2 = make_likert6()

    neighborhood1 = make_likert6()
    neighborhood2 = make_likert6()
    neighborhood3 = make_likert6()
    neighborhood4 = make_likert6()

    attention = make_likert6()

    homophily1 = make_likert6()
    homophily2 = make_likert6()
    homophily3 = make_likert6()

    comment = models.StringField(
        blank=True,
    )


# FUNCTIONS
# PAGES

class cc_concern(Page):
    form_model = 'player'
    form_fields = ['cc_concern1', 'cc_concern2', 'cc_concern3', 'cc_concern4']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['cc_concern1', 'cc_concern2', 'cc_concern3', 'cc_concern4'],
            form_field_labels=[Lexicon.cc_concern1_label, Lexicon.cc_concern2_label, Lexicon.cc_concern3_label,
                               Lexicon.cc_concern4_label]
    )


class pol_orientation(Page):
    form_model = 'player'
    form_fields = ['conservative_liberal']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)


class probability(Page):
    form_model = 'player'
    form_fields = ['ev_prob_benefits1', 'ev_prob_benefits2', 'ev_prob_benefits3', 'ev_prob_benefits4',
                   'ev_prob_risks1', 'ev_prob_risks2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['ev_prob_benefits1', 'ev_prob_benefits2', 'ev_prob_benefits3', 'ev_prob_benefits4',
                         'ev_prob_risks1', 'ev_prob_risks2'],
            form_field_labels=[Lexicon.ev_prob_benefits1_label, Lexicon.ev_prob_benefits2_label,
                               Lexicon.ev_prob_benefits3_label, Lexicon.ev_prob_benefits4_label]
        )


class risks(Page):
    form_model = 'player'
    form_fields = ['ev_perceived_risk1', 'ev_perceived_risk2', 'ev_perceived_benefit1', 'ev_perceived_benefit2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['ev_perceived_risk1', 'ev_perceived_risk2', 'ev_perceived_benefit1', 'ev_perceived_benefit2'],
            form_field_labels=[Lexicon.ev_perceived_risk1_label, Lexicon.ev_perceived_risk2_label,
                               Lexicon.ev_perceived_benefit1_label, Lexicon.ev_perceived_benefit2_label]
        )

class neighbors(Page):
    form_model = 'player'
    form_fields = ['neighborhood1', 'neighborhood2', 'neighborhood3', 'attention', 'neighborhood4', 'homophily1',
                   'homophily2', 'homophily3']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['neighborhood1', 'neighborhood2', 'neighborhood3', 'attention', 'neighborhood4', 'homophily1',
                         'homophily2', 'homophily3'],
            form_field_labels=[Lexicon.neighborhood1_label, Lexicon.neighborhood2_label,
                               Lexicon.neighborhood3_label,
                               Lexicon.attention_label,
                               Lexicon.neighborhood4_label,
                               Lexicon.homophily1_label, Lexicon.homophily2_label, Lexicon.homophily3_label]
        )


class comments(Page):
    form_model = 'player'
    form_fields = ['comment']


# Page sequence
page_sequence = [
    probability,
    risks,
    neighbors,
    cc_concern,
    pol_orientation,
    comments
]
