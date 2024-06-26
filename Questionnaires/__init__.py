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
    else:
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_en"
    subsession.session.questionnairesLexi = Lexicon


def make_likert6():
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6],
        widget=widgets.RadioSelect,
    )


def make_likert10():
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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

    wom_talking = models.IntegerField(min=0, max=50)

    homophily1 = make_likert6()
    homophily2 = make_likert6()
    homophily3 = make_likert6()
    homophily4 = make_likert6()

    comment = models.StringField(
        blank=True,
    )

class transition(Page):
    form_model = 'player'

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
                           Lexicon.ev_prob_benefits3_label, Lexicon.ev_prob_benefits4_label,
                           Lexicon.ev_prob_risks1_label, Lexicon.ev_prob_risks2_label]
        )


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
    form_fields = ['wom_talking',
                   'homophily1', 'homophily2', 'homophily3', 'homophily4']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.questionnairesLexi
        return dict(
            form_fields=['wom_talking',
                         'homophily1', 'homophily2', 'homophily3', 'homophily4'],
            form_field_labels=[Lexicon.wom_talking_label,
                               Lexicon.homophily1_label, Lexicon.homophily2_label,
                               Lexicon.homophily3_label, Lexicon.homophily4_label]
        )


class comments(Page):
    form_model = 'player'
    form_fields = ['comment']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.questionnairesLexi)


# Page sequence
page_sequence = [
    transition,
    probability,
    risks,
    neighbors,
    cc_concern,
    pol_orientation,
    comments
]
