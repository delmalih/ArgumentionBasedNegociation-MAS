###########
# Imports #
###########


from osbrain.agent import Agent

from messages.MessagePerformative import MessagePerformative
from messages.Message import Message


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
        self.__preferences = None

        """Initializes the communication channels.
        """
        self.bind('REP', alias=f"{self.name}-channel",
                  handler=self.answer_handler)
        self.__channel = f"{self.name}-channel"

        """Prints that the agent is initialized
        """
        self.log_info(f"{self.name} is initialized !")

    def set_preferences(self, preferences):
        """Setter for preferences attribute.
        """
        self.__preferences = preferences

    def get_channel(self):
        """Getter for the channel attribute.
        """
        return self.__channel

    def answer_handler(self, message):
        """TODO.
        """
        pass

    def treat_answer(self, message):
        """TODO.
        """
        pass

    def send_message(self, receiver, performative, content):
        message = Message(self, receiver, performative, content)
        message.send()

    def ask_list_items(self, manager):
        """TODO.
        """
        performative = MessagePerformative.QUERY_REF
        content = "LIST ITEMS"
        self.send_message(manager, performative, content)
        answer = self.recv(manager.get_channel())
        self.treat_answer(answer)

    def ask_selected_items(self, manager):
        """TODO.
        """
        performative = MessagePerformative.QUERY_REF
        content = "SELECTED ITEMS"
        self.send_message(manager, performative, content)
        answer = self.recv(manager.get_channel())
        self.treat_answer(answer)
