from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
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
    subsession.session.demographicsLexi = Lexicon


class Group(BaseGroup):
    pass


def make_likert10():
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect,
    )


def education_choices(player):
    Lexicon = player.session.demographicsLexi
    education_choices = [
            ["none", Lexicon.none],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["college", Lexicon.college],
            ["university", Lexicon.university],
            ["doctor", Lexicon.doctor]
        ]
    return education_choices


def gender_choices(player):
    Lexicon = player.session.demographicsLexi
    gender_choices = [
        ["female", Lexicon.female],
        ["male", Lexicon.male],
        ["other", Lexicon.other]
    ]
    return gender_choices


def region_choices(player):
    Lexicon = player.session.demographicsLexi
    region_choices = [
        ["urban", Lexicon.urban],
        ["suburban", Lexicon.suburban],
        ["rural", Lexicon.rural]
    ]
    return region_choices


def income_choices(player):
    Lexicon = player.session.demographicsLexi
    income_choices = [
        ["1", Lexicon.income_quintile1],
        ["2", Lexicon.income_quintile2],
        ["3", Lexicon.income_quintile3],
        ["4", Lexicon.income_quintile4],
        ["5", Lexicon.income_quintile5]
    ]
    return income_choices

def own_car_choices(player):
    Lexicon = player.session.demographicsLexi
    own_car_choices = [
        ["yes", Lexicon.yes],
        ["no", Lexicon.no]
    ]
    return own_car_choices

def car_type_choices(player):
    Lexicon = player.session.demographicsLexi
    car_type_choices = [
        ["gasoline", Lexicon.gasoline],
        ["ev", Lexicon.ev],
        ["hev", Lexicon.hev]
    ]
    return car_type_choices

def car_model_choices(player):
    Lexicon = player.session.demographicsLexi
    car_model_choices = [
        ["small", Lexicon.small],
        ["medium", Lexicon.medium],
        ["large", Lexicon.large]
    ]
    return car_model_choices

def car_replace_choices(player):
    Lexicon = player.session.demographicsLexi
    car_replace_choices = [
        ["1", Lexicon.one],
        ["4", Lexicon.four],
        ["8", Lexicon.eight],
        ["12", Lexicon.twelve]
    ]
    return car_replace_choices

def car_choices(player):
    Lexicon = player.session.demographicsLexi
    car_choices = [
        ["small", Lexicon.small],
        ["medium", Lexicon.medium],
        ["large", Lexicon.large]
    ]
    return car_choices

def wom_owner_choices(player):
    Lexicon = player.session.demographicsLexi
    wom_owner_choices = [
        ["neutral", Lexicon.neutral],
        ["positive", Lexicon.positive],
        ["negative", Lexicon.negative]
    ]
    return wom_owner_choices

def wom_positive_choices(player):
    Lexicon = player.session.demographicsLexi
    wom_positive_choices = [
        ["0", Lexicon.never],
        ["1", Lexicon.rarely],
        ["2", Lexicon.sometimes],
        ["3", Lexicon.often],
        ["4", Lexicon.very_often]
    ]
    return wom_positive_choices

def wom_negative_choices(player):
    Lexicon = player.session.demographicsLexi
    wom_negative_choices = [
        ["0", Lexicon.never],
        ["1", Lexicon.rarely],
        ["2", Lexicon.sometimes],
        ["3", Lexicon.often],
        ["4", Lexicon.very_often]
    ]
    return wom_negative_choices

def no_car_choices(player):
    Lexicon = player.session.demographicsLexi
    no_car_choices = [
        ["yes", Lexicon.yes],
        ["no", Lexicon.no]
    ]
    return no_car_choices


class Player(BasePlayer):

    # Demographics
    age = models.IntegerField(min=18, max=99)
    gender = models.StringField(widget=widgets.RadioSelect,)
    education = models.StringField(widget=widgets.RadioSelect,)
    income = models.StringField(widget=widgets.RadioSelect,)
    household = models.IntegerField(min=1, max=12)
    region = models.StringField(widget=widgets.RadioSelect,)
    zip_code = models.StringField(blank=True)

    # Car_questions
    own_car = models.StringField(widget=widgets.RadioSelect,)
    car = models.StringField(widget=widgets.RadioSelect,)

    # car_owner
    car_type = models.StringField(widget=widgets.RadioSelect,)
    car_model = models.StringField(widget=widgets.RadioSelect,)
    car_number = models.IntegerField(min=1, max=8)
    car_age = models.IntegerField(min=1, max=30)
    car_replace = models.StringField(widget=widgets.RadioSelect,)
    km_day = models.IntegerField(min=0, max=1000)
    km_year = models.IntegerField(min=0, max=100000)

    # no_car_owner
    no_car = models.StringField(widget=widgets.RadioSelect,)

    # WoM
    wom_owner = models.StringField(widget=widgets.RadioSelect, blank=True)
    wom_number = models.IntegerField(min=0, max=50)
    wom_positive = models.StringField(widget=widgets.RadioSelect,)
    wom_negative = models.StringField(widget=widgets.RadioSelect,)

    # affect
    affect_ev = make_likert10()


# Demographics Page class
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'income', 'household', 'region', 'zip_code']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['age', 'gender', 'education', 'income', 'household', 'region', 'zip_code'],
            form_field_labels=[Lexicon.age_label, Lexicon.gender_label, Lexicon.education_label,
                               Lexicon.income_label, Lexicon.household_label, Lexicon.region_label,
                               Lexicon.zip_code_label]
        )


class Car_questions(Page):
    form_model = 'player'
    form_fields = ['own_car', 'car']

    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['car'] = player.car
        player.participant.vars['own_car'] = player.own_car

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['own_car', 'car'],
            form_field_labels=[Lexicon.own_car_label, Lexicon.car_label]
        )


class car_owner(Page):
    form_model = 'player'
    form_fields = ['car_number', 'car_type', 'car_model', 'car_age', 'car_replace', 'km_day', 'km_year']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'yes'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['car_number', 'car_type', 'car_model', 'car_age', 'car_replace', 'km_day', 'km_year'],
            form_field_labels=[Lexicon.car_number_label, Lexicon.car_type_label, Lexicon.car_model_label,
                               Lexicon.car_age_label, Lexicon.car_replace_label, Lexicon.km_day_label, Lexicon.km_year_label]
        )


class no_car_owner(Page):
    form_model = 'player'
    form_fields = ['no_car']

    def is_displayed(player):
        return player.participant.vars['own_car'] == 'no'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['no_car'],
            form_field_labels=[Lexicon.no_car_label]
        )


class WoM(Page):
    form_model = 'player'
    form_fields = ['wom_owner', 'wom_number', 'wom_positive', 'wom_negative']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)

    @staticmethod
    def js_vars(player):
        Lexicon = player.session.demographicsLexi
        return dict(
            form_fields=['wom_owner', 'wom_number', 'wom_positive', 'wom_negative'],
            form_field_labels=[Lexicon.wom_owner_label, Lexicon.wom_number_label, Lexicon.wom_positive_label,
                               Lexicon.wom_negative_label]
        )


class affect(Page):
    form_model = 'player'
    form_fields = ['affect_ev']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.demographicsLexi)


# Page sequence
page_sequence = [
    Demographics,
    Car_questions,
    car_owner,
    no_car_owner,
    WoM,
    affect
]
