###########
# Imports #
###########


import argparse
import numpy as np
from osbrain import run_agent
from osbrain import run_nameserver

from preferences.Item import Item
from preferences.Criterion import Criterion
from preferences.Preferences import Preferences
from preferences.CriterionName import CriterionName
from preferences.CriterionValue import CriterionValue

from agents.Manager import Manager
from agents.Engineer import Engineer

from DefaultData import DEFAULT_ITEMS, DEFAULT_CRITERIONS


##################
# INITIALIZATION #
##################


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--random",
        dest="random",
        help="Generate random data",
        action="store_true")
    return parser.parse_args()


def init_items(args):
    """TODO.
    """
    if args.random:
        items = []
        for k in range(np.random.randint(2, 6)):
            items.append(Item(f"Item{k + 1}", f"Item number {k + 1}"))
        return items
    else:
        items = DEFAULT_ITEMS
    return items


def init_criterions(args, items):
    """TODO.
    """
    if args.random:
        criterions = []
        for item in items:
            for criterion_name in CriterionName:
                criterion_value = np.random.choice(CriterionValue)
                criterions.append(Criterion(
                    item,
                    criterion_name,
                    criterion_value))
    else:
        criterions = DEFAULT_CRITERIONS
    return criterions


def init_default_preferences(criterions):
    """TODO.
    """

    # Start preferences
    preferences_1 = Preferences()
    preferences_2 = Preferences()

    # Set criterion name
    preferences_1.set_criterion_order([
        CriterionName.PRODUCTION_COST,
        CriterionName.ENVIRONMENT_IMPACT,
        CriterionName.CONSUMPTION,
        CriterionName.DURABILITY,
        CriterionName.NOISE,
    ])
    preferences_2.set_criterion_order([
        CriterionName.ENVIRONMENT_IMPACT,
        CriterionName.NOISE,
        CriterionName.PRODUCTION_COST,
        CriterionName.CONSUMPTION,
        CriterionName.DURABILITY,
    ])

    # Add criterions
    preferences_1.add_criterions(criterions)
    preferences_2.add_criterions(criterions)

    return preferences_1, preferences_2


def init_random_preferences(criterions):
    """TODO.
    """

    # Start preferences
    preferences_1 = Preferences()
    preferences_2 = Preferences()

    # Set criterion name
    criterion_order_1 = list(CriterionName)
    criterion_order_2 = list(CriterionName)
    np.random.shuffle(criterion_order_1)
    np.random.shuffle(criterion_order_2)
    preferences_1.set_criterion_order(criterion_order_1)
    preferences_2.set_criterion_order(criterion_order_2)

    # Add criterions
    preferences_1.add_criterions(criterions)
    preferences_2.add_criterions(criterions)

    return preferences_1, preferences_2


def init_preferences(args, criterions):
    """TODO.
    """
    if args.random:
        preferences = init_random_preferences(criterions)
    else:
        preferences = init_default_preferences(criterions)
    return preferences


def init_all_communications(agents):
    """TODO.
    """
    for i1 in range(len(agents)):
        for i2 in range(len(agents)):
            if i1 != i2:
                agents[i1].connect(agents[i2].addr(agents[i2].get_channel()),
                                   alias=agents[i2].get_channel())


def print_data(items, criterions, preferences_1, preferences_2):
    """TODO.
    """
    print("="*40)
    print("||" + " "*16 + "ITEMS" + " "*15 + "||")
    print("="*40)
    for k, item in enumerate(items):
        print(f"ITEM: {item.get_name()}")
        for criterion in preferences_1.get_criterions_from_item(item):
            criterion_name = criterion.get_name().name
            criterion_value = preferences_1.get_criterion_value(
                criterion_name, item).name
            print(f"{criterion_name}: {criterion_value}")
        if k != len(items) - 1:
            print("-"*40)
    print("\n")

    print("="*40)
    print("||" + " "*13 + "PREFERENCES" + " "*12 + "||")
    print("="*40)
    criterion_order_1 = map(lambda x: x.name,
                            preferences_1.get_criterion_order())
    criterion_order_2 = map(lambda x: x.name,
                            preferences_2.get_criterion_order())
    print(f"Agent 1: {' > '.join(criterion_order_1)}")
    print(f"Agent 2: {' > '.join(criterion_order_2)}")
    print("\n")


########
# MAIN #
########


if __name__ == "__main__":
    """Main program.
    """

    # Get args
    args = parse_args()

    # Init items, criterions and preferences
    items = init_items(args)
    criterions = init_criterions(args, items)
    preferences_1, preferences_2 = init_preferences(args, criterions)

    # Prints
    print_data(items, criterions, preferences_1, preferences_2)

    # System deployment
    ns = run_nameserver()

    # Running agents
    engineer1 = run_agent(name="Engineer1", base=Engineer)
    engineer2 = run_agent(name="Engineer2", base=Engineer)
    manager = run_agent(name="Manager", base=Manager)

    # Setup agents
    manager.set_list_items(items)
    engineer1.set_preferences(preferences_1)
    engineer2.set_preferences(preferences_2)
    engineer1.register_manager(manager)
    engineer2.register_manager(manager)

    # Setup communications
    init_all_communications([manager, engineer1, engineer2])

    # Send messages
    engineer1.send_query(manager)
    engineer2.send_query(manager)
    engineer1.start_negociation(engineer2)

    # Close the sytem
    ns.shutdown()
