###########
# Imports #
###########


from osbrain.agent import Agent


############
# Engineer #
############


class Engineer(Agent):
    """Engineer agent class.
    This class implements the engineer agent.

    attr:
        preferences: this preferences of the agent
    """

    def on_init(self):
        """Initializes the agent.
        """
        self.log_info(f"Agent {self.name} is initialized !")
