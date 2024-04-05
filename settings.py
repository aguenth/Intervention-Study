from os import environ


SESSION_CONFIGS = [

    dict(
       name='USA',
       display_name="USA_Intervention_Study",
       num_demo_participants=5,
       language="en",
       app_sequence=['Demographics',
                     'Task',
                     'tracking_intro',
                     'Consent',
                     'Questionnaires',
                     'End']
     ),
    dict(
       name='Mexico',
       display_name="Mexico_Intervention_Study",
       num_demo_participants=5,
       language="mx",
       app_sequence=['Demographics',
                     'Questionnaires',
                     'End',
                     'Consent',
                     'tracking_intro',
                     'Task']
     ),
    dict(
        name='UK',
        display_name="UK_Intervention_Study",
        num_demo_participants=5,
        language="uk",
        app_sequence=['Demographics',
                      'Questionnaires',
                      'End',
                      'Consent',
                      'tracking_intro',
                      'Task']
    ),
    dict(
        name='SouthAfrica',
        display_name="ZA_Intervention_Study",
        num_demo_participants=5,
        language="za",
        app_sequence=['Demographics',
                      'Questionnaires',
                      'End',
                      'Consent',
                      'tracking_intro',
                      'Task']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'task_rounds',
    'car'
]


SESSION_FIELDS = [

    'questionnairesLexi',

    'introLexi',

    'demographicsLexi',

    'tracking_introLexi',

    'taskLexi',


    'endLexi',

    'myLangCode'
]

# ISO-639 code

LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3153268574945'

INSTALLED_APPS = ['otree', 'django_extensions']
EXTENSION_APPS = ['otree_tools']
