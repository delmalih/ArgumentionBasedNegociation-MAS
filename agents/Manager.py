###########
# Imports #
###########


from osbrain.agent import Agent


###########
# Manager #
###########


class Manager(Agent):
    """Manager agent class.
    This class implements the manager agent.

    attr:
        list_items: this list of items to discuss
        selected_items: the list of selected items
    """

    def on_init(self):
        """Initializes the agent.
        """
        self.__list_items = []
        self.__selected_items = []

        """Initializes the communication channel.
        """
