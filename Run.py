###########
# Imports #
###########


from osbrain import run_nameserver
from osbrain import run_agent

from preferences.Item import Item
from agents.Engineer import Engineer
from agents.Manager import Manager


########
# MAIN #
########


if __name__ == "__main__":
    """Main program.
    """

    # Init items and preferences
    diesel_engine = Item("Diesel Engine", "A super cool diesel engine")
    electric_engine = Item("Electric Engine", "A very quiet engine")

    # System deployment
    ns = run_nameserver()

    # Running agents
    engineer = run_agent(name="Engineer", base=Engineer)
    manager = run_agent(name="Manager", base=Manager)
    manager.add_item(diesel_engine)
    manager.add_item(electric_engine)

    # Setup communications
    engineer.connect(manager.addr(manager.get_channel()),
                     alias=manager.get_channel())
    manager.connect(engineer.addr(engineer.get_channel()),
                    alias=engineer.get_channel())

    # Send messages
    engineer.ask_list_items(manager)
    engineer.ask_selected_items(manager)

    # Close the sytem
    ns.shutdown()
