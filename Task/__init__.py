from otree.api import *
import random

author = 'Anne Guenther'

doc = """
Mouse Tracking Task
"""


# Constants
class Constants(BaseConstants):
    name_in_url = 'Task'
    players_per_group = None
    blocks = ['A', 'B', 'C', 'D', 'E']
    trials_per_block = 18
    num_rounds = 90
    possible_orders = [
        ['B', 'D', 'C', 'A'],
        ['B', 'D', 'A', 'C'],
        ['D', 'B', 'C', 'A'],
        ['D', 'B', 'A', 'C'],
        ['C', 'D', 'B', 'D'],
        ['A', 'C', 'B', 'D'],
        ['C', 'A', 'D', 'B'],
        ['A', 'C', 'D', 'B']
    ]

    from .attributes_en import attributes_listA_small as attributes_listA_small
    from .attributes_en import attributes_listB_small as attributes_listB_small
    from .attributes_en import attributes_listC_small as attributes_listC_small
    from .attributes_en import attributes_listD_small as attributes_listD_small
    from .attributes_en import attributes_listA_medium as attributes_listA_medium
    from .attributes_en import attributes_listB_medium as attributes_listB_medium
    from .attributes_en import attributes_listC_medium as attributes_listC_medium
    from .attributes_en import attributes_listD_medium as attributes_listD_medium
    from .attributes_en import attributes_listA_large as attributes_listA_large
    from .attributes_en import attributes_listB_large as attributes_listB_large
    from .attributes_en import attributes_listC_large as attributes_listC_large
    from .attributes_en import attributes_listD_large as attributes_listD_large
    from .attributes_en import attributes_listE as attributes_listE

    from .attributes_es import attributes_listA_small as attributes_listA_small_es
    from .attributes_es import attributes_listB_small as attributes_listB_small_es
    from .attributes_es import attributes_listC_small as attributes_listC_small_es
    from .attributes_es import attributes_listD_small as attributes_listD_small_es
    from .attributes_es import attributes_listA_medium as attributes_listA_medium_es
    from .attributes_es import attributes_listB_medium as attributes_listB_medium_es
    from .attributes_es import attributes_listC_medium as attributes_listC_medium_es
    from .attributes_es import attributes_listD_medium as attributes_listD_medium_es
    from .attributes_es import attributes_listA_large as attributes_listA_large_es
    from .attributes_es import attributes_listB_large as attributes_listB_large_es
    from .attributes_es import attributes_listC_large as attributes_listC_large_es
    from .attributes_es import attributes_listD_large as attributes_listD_large_es
    from .attributes_es import attributes_listE as attributes_listE_es


# Subsession
class Subsession(BaseSubsession):
    pass


# Group
class Group(BaseGroup):
    pass


# Player
class Player(BasePlayer):

    def store_tracking_data(self, payload):
        HoverEvent.create(
            player=self,
            element_id=payload["element_id"],
            enter_time=payload["enter_time"],
            leave_time=payload["leave_time"],
            duration=payload["duration"],
            attributeType=payload["attributeType"],
            attributeValue=payload["attributeValue"],
        )

    # Add a field to store the radio button decision
    choice = models.StringField(
        choices=["Yes", "No"],
        widget=widgets.RadioSelectHorizontal,
    )

    current_task = models.IntegerField(initial=0)
    block = models.StringField()
    current_task_pol = models.IntegerField(initial=0)

    car = models.StringField()


# Extra model for tracking hover events
class HoverEvent(models.ExtraModel):
    player = models.Link(Player)
    element_id = models.StringField()
    enter_time = models.FloatField()
    leave_time = models.FloatField()
    duration = models.IntegerField()
    attributeType = models.StringField()
    attributeValue = models.StringField()


# Custom export function
def custom_export(players):
    print("DEBUG: custom_export function called")
    yield ["session", "participant_code", "round_number", "block", "current_task", "id_in_group",
           "element_id", "enter_time", "leave_time", "duration", "attributeType", "attributeValue", "choice"]
    for player in players:
        print(f"DEBUG: Exporting data for player {player.id_in_group}")
        for e in HoverEvent.filter(player=player):
            yield [
                player.session.code,
                player.participant.code,
                player.round_number,
                player.block,
                player.current_task,
                player.id_in_group,
                e.element_id,
                e.enter_time,
                e.leave_time,
                e.duration,
                e.attributeType,
                e.attributeValue,
                player.choice,  # Include the choice variable
            ]


def creating_session(subsession: Subsession):
    if subsession.session.config['language'] == 'mx':
        from .lexicon_mx import Lexicon
        subsession.session.myLangCode = "_mx"
    else:
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_en"
    subsession.session.taskLexi = Lexicon

    if subsession.round_number == 1:
        for p in subsession.get_players():
            tasks = ['TaskPage'] * Constants.num_rounds + ['PolicyPage']
            random.shuffle(tasks)
            task_rounds = dict(zip(tasks, range(1, len(tasks) + 1)))
            p.participant.task_rounds = task_rounds

    if subsession.round_number <= Constants.num_rounds:
        trials_per_block = Constants.trials_per_block

        for p in subsession.get_players():
            possible_orders = Constants.possible_orders.copy()

            # Shuffle the order of blocks (excluding Block E)
            block_order = random.choice(possible_orders)

            # Decide whether Block E should be placed before or after the shuffled blocks
            if random.choice([True, False]):
                block_order = ['E'] + block_order
            else:
                block_order = block_order + ['E']

            randomized_sequence = []

            # Generate a sequence that completes all trials for each block before moving on to the next block
            for block in block_order:
                block_sequence = [(block, trial_number) for trial_number in range(1, trials_per_block + 1)]
                random.shuffle(block_sequence)
                randomized_sequence.extend(block_sequence)

            p.participant.task_rounds = randomized_sequence
            p.participant.vars['randomized_sequence'] = randomized_sequence


# Page with Blocks A, B, C, D, E
class TaskPage(Page):
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def vars_for_template(player: Player):
        Lexicon = player.session.taskLexi
        # Ensure that randomized_sequence is set before trying to access it
        if player.session.config['language'] == "mx":
            attributes_listA_small = Constants.attributes_listA_small_es
            attributes_listB_small = Constants.attributes_listB_small_es
            attributes_listC_small = Constants.attributes_listC_small_es
            attributes_listD_small = Constants.attributes_listD_small_es
            attributes_listA_medium = Constants.attributes_listA_medium_es
            attributes_listB_medium = Constants.attributes_listB_medium_es
            attributes_listC_medium = Constants.attributes_listC_medium_es
            attributes_listD_medium = Constants.attributes_listD_medium_es
            attributes_listA_large = Constants.attributes_listA_large_es
            attributes_listB_large = Constants.attributes_listB_large_es
            attributes_listC_large = Constants.attributes_listC_large_es
            attributes_listD_large = Constants.attributes_listD_large_es
            attributes_listE = Constants.attributes_listE_es
        else:
            attributes_listA_small = Constants.attributes_listA_small
            attributes_listB_small = Constants.attributes_listB_small
            attributes_listC_small = Constants.attributes_listC_small
            attributes_listD_small = Constants.attributes_listD_small
            attributes_listA_medium = Constants.attributes_listA_medium
            attributes_listB_medium = Constants.attributes_listB_medium
            attributes_listC_medium = Constants.attributes_listC_medium
            attributes_listD_medium = Constants.attributes_listD_medium
            attributes_listA_large = Constants.attributes_listA_large
            attributes_listB_large = Constants.attributes_listB_large
            attributes_listC_large = Constants.attributes_listC_large
            attributes_listD_large = Constants.attributes_listD_large
            attributes_listE = Constants.attributes_listE_es

        if 'randomized_sequence' not in player.participant.vars:
            print("DEBUG: 'randomized_sequence' not found in participant.vars. Calling creating_session.")

        current_task_tuple = player.participant.task_rounds[player.round_number - 1]

        print("Randomized Sequence:", player.participant.vars['randomized_sequence'])

        if not isinstance(current_task_tuple, tuple) or len(current_task_tuple) != 2:
            # Handle the case where current_task_tuple is not a tuple of length 2
            current_task_tuple = ('', 0)

        block, trial_number = current_task_tuple
        print(f"DEBUG: current_task_tuple: {current_task_tuple}, block: {block}, trial_number: {trial_number}")

        player.block = block
        player.current_task = trial_number

        # Define which blocks are product choice and which is the policy block
        policy_block = block == 'E'
        product_block = player.block in ['A', 'B', 'C', 'D']

        # Check if the current trial is the very first trial and the block is A, B, C, or D
        product_first = player.round_number == 1 and player.block in ['A', 'B', 'C', 'D']
        product_second = not product_first and player.round_number == 19 and player.block in ['A', 'B', 'C', 'D']

        blockC_first = player.round_number == 1 and player.block == 'C'
        blockC_second = not product_first and player.round_number in [19, 37, 55, 73] and player.block == 'C'

        round_number = player.round_number

        if player.round_number == 1 and policy_block:
            player.participant.vars['first_block_was_policy'] = True

        if player.round_number in [1, 19] and player.block in ['B', 'D']:
            player.participant.vars['label_first'] = True

        if player.round_number in [1, 19] and player.block in ['A', 'C']:
            player.participant.vars['label_second'] = True

        BD1 = (player.participant.vars.get('label_first', False) and
               ((player.round_number == 1 and not player.participant.vars.get('first_block_was_policy', False)) or
                (player.round_number == 19 and player.participant.vars.get('first_block_was_policy', False))) and
               block == 'B')
        BD19 = (player.participant.vars.get('label_first', False) and
                ((player.round_number == 19 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 37 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'D')

        DB1 = (player.participant.vars.get('label_first', False) and
               ((player.round_number == 1 and not player.participant.vars.get('first_block_was_policy', False)) or
                (player.round_number == 19 and player.participant.vars.get('first_block_was_policy', False))) and
               block == 'D')
        DB19 = (player.participant.vars.get('label_first', False) and
                ((player.round_number == 19 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 37 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'B')

        BD37 = (player.participant.vars.get('label_second', False) and
                ((player.round_number == 37 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 55 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'B')
        BD55 = (player.participant.vars.get('label_second', False) and
                ((player.round_number == 55 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 73 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'D')

        DB37 = (player.participant.vars.get('label_second', False) and
                ((player.round_number == 37 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 55 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'D')
        DB55 = (player.participant.vars.get('label_second', False) and
                ((player.round_number == 55 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 73 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'B')

        AC1 = (player.participant.vars.get('label_second', False) and
               ((player.round_number == 1 and not player.participant.vars.get('first_block_was_policy', False)) or
                (player.round_number == 19 and player.participant.vars.get('first_block_was_policy', False))) and
               block == 'A')
        AC19 = (player.participant.vars.get('label_second', False) and
                ((player.round_number == 19 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 37 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'C')

        CA1 = (player.participant.vars.get('label_second', False) and
               ((player.round_number == 1 and not player.participant.vars.get('first_block_was_policy', False)) or
                (player.round_number == 19 and player.participant.vars.get('first_block_was_policy', False))) and
               block == 'C')
        CA19 = (player.participant.vars.get('label_second', False) and
                ((player.round_number == 19 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 37 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'A')

        AC37 = (player.participant.vars.get('label_first', False) and
                ((player.round_number == 37 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 55 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'A')
        AC55 = (player.participant.vars.get('label_first', False) and
                ((player.round_number == 55 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 73 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'C')

        CA37 = (player.participant.vars.get('label_first', False) and
                ((player.round_number == 37 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 55 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'C')
        CA55 = (player.participant.vars.get('label_first', False) and
                ((player.round_number == 55 and not player.participant.vars.get('first_block_was_policy', False)) or
                 (player.round_number == 73 and player.participant.vars.get('first_block_was_policy', False))) and
                block == 'A')

        # Specify the rounds where the message is supposed to be visually attractive -> first trials of each block
        attractive_rounds = {1, 19, 37, 55, 73}
        # Check if trial_number is in attractive_rounds = first trial of the block
        is_first_trial_of_block = player.round_number in attractive_rounds

        # Well done rounds
        well_done = {19, 37, 55, 73}
        completed_block = player.round_number in well_done

        # Conditionally choose the attributes lists based on the "car" value and block
        if player.participant.vars['car'] == 'small':
            attributes_list = {
                'A': attributes_listA_small,
                'B': attributes_listB_small,
                'C': attributes_listC_small,
                'D': attributes_listD_small,
                'E': attributes_listE,
            }
        elif player.participant.vars['car'] == 'medium':
            attributes_list = {
                'A': attributes_listA_medium,
                'B': attributes_listB_medium,
                'C': attributes_listC_medium,
                'D': attributes_listD_medium,
                'E': attributes_listE,
            }
        elif player.participant.vars['car'] == 'large':
            attributes_list = {
                'A': attributes_listA_large,
                'B': attributes_listB_large,
                'C': attributes_listC_large,
                'D': attributes_listD_large,
                'E': attributes_listE,
            }

        try:
            if block == 'E':
                attributes = attributes_listE[trial_number - 1]
                if 'shuffled_attributes_policy' not in player.participant.vars:
                    keys_list_policy = list(attributes.keys())
                    random.shuffle(keys_list_policy)
                    player.participant.vars['keys_list_policy'] = keys_list_policy
                    shuffled_attributes = {key: attributes[key] for key in keys_list_policy}
                    player.participant.vars['shuffled_attributes_policy'] = shuffled_attributes
                else:
                    shuffled_attributes = {key: attributes[key] for key in player.participant.vars['keys_list_policy']}
            else:
                # Retrieve the attributes_list for the given block
                current_attributes_list = attributes_list[block]
                if not current_attributes_list:
                    print("DEBUG: current_attributes_list is empty. Available blocks:", attributes_list.keys())
                    raise KeyError(f"Block {block} not found in attributes_list")
                # Retrieve the attributes for the given trial_number
                attributes = current_attributes_list[trial_number - 1]
                if 'shuffled_attributes_product' not in player.participant.vars:
                    keys_list = list(attributes.keys())
                    random.shuffle(keys_list)
                    player.participant.vars['keys_list'] = keys_list
                    shuffled_attributes = {key: attributes[key] for key in keys_list}
                    player.participant.vars['shuffled_attributes_product'] = shuffled_attributes
                else:
                    shuffled_attributes = {key: attributes[key] for key in player.participant.vars['keys_list']}
        except KeyError:
            print("DEBUG: KeyError occurred. Available blocks:", attributes_list.keys())
            raise

        return {
            "attributes": shuffled_attributes,
            "current_task": trial_number,  # Set current_task to the extracted trial_number
            "block": block,  # Include the block information
            "round_number": round_number,
            "is_first_trial_of_block": is_first_trial_of_block,
            "completed_block": completed_block,
            "policy_block": policy_block,
            "product_first": product_first,
            "product_second": product_second,
            "first_block_was_policy": player.participant.vars.get('first_block_was_policy', False),
            "product_block": product_block,
            "blockC_first": blockC_first,
            "blockC_second": blockC_second,
            "label_first": player.participant.vars.get('label_first', False),
            "label_second": player.participant.vars.get('label_second', False),
            "Lexicon": player.session.taskLexi,
            "BD1": BD1,
            "BD19": BD19,
            "DB1": DB1,
            "DB19": DB19,
            "AC1": AC1,
            "AC19": AC19,
            "CA1": CA1,
            "CA19": CA19,
            "BD37": BD37,
            "BD55": BD55,
            "DB37": DB37,
            "DB55": DB55,
            "AC37": AC37,
            "AC55": AC55,
            "CA37": CA37,
            "CA55": CA55
        }

    def live_method(player, data):
        player.store_tracking_data(data)

    def store_tracking_data(self, data):
        pass


# Page sequence
page_sequence = [TaskPage]