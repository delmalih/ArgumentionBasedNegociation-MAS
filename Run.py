###########
# Imports #
###########


from osbrain import run_agent
from osbrain import run_nameserver

from preferences.Preferences import Preferences
from preferences.CriterionName import CriterionName

from agents.Manager import Manager
from agents.Engineer import Engineer

from DefaultData import DEFAULT_ITEMS, DEFAULT_CRITERIONS


##################
# INITIALIZATION #
##################


def init_all_communications(agents):
    """TODO.
    """
    for i1 in range(len(agents)):
        for i2 in range(len(agents)):
            if i1 != i2:
                agents[i1].connect(agents[i2].addr(agents[i2].get_channel()),
                                   alias=agents[i2].get_channel())


def init_preferences(criterions):
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


########
# MAIN #
########


if __name__ == "__main__":
    """Main program.
    """

    # System deployment
    ns = run_nameserver()

    # Init items, criterions and preferences
    items = DEFAULT_ITEMS
    criterions = DEFAULT_CRITERIONS
    preferences_1, preferences_2 = init_preferences(criterions)

    # Running agents
    engineer1 = run_agent(name="Engineer1", base=Engineer)
    engineer2 = run_agent(name="Engineer2", base=Engineer)
    manager = run_agent(name="Manager", base=Manager)
    manager.set_list_items(items)

    # Setup preferences
    engineer1.set_preferences(preferences_1)
    engineer2.set_preferences(preferences_2)

    # Register to manager
    engineer1.register_manager(manager)
    engineer2.register_manager(manager)

    # Setup communications
    init_all_communications([manager, engineer1, engineer2])

    # Send messages
    engineer1.send_query(manager)
    engineer2.send_query(manager)
    engineer1.send_propose_item(engineer2)

    # Close the sytem
    ns.shutdown()
