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
        self.__list_items = []
        self.__selected_items = []
        self.__commited_items = []

        """Initializes the communication channels.
        """
        self.bind('REP', alias=f"{self.name}-channel",
                  handler=self.handle_message_reception)
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

    # <-- General functions for message --> #

    def handle_message_reception(self, message):
        """TODO.
        """
        if message.get_performative() == MessagePerformative.PROPOSE:
            answer = self.answer_proposed_item(message)
        if message.get_performative() == MessagePerformative.COMMIT:
            answer = self.answer_commited_item(message)
        if message.needs_answer():
            self.log_info(answer)
        return answer

    def treat_answer(self, message):
        """TODO.
        """
        if message.get_performative() == MessagePerformative.INFORM_REF:
            self.treat_inform_ref(message)
        if message.get_performative() == MessagePerformative.ACCEPT:
            self.treat_accept(message)
        if message.get_performative() == MessagePerformative.ARGUE:
            self.treat_argue(message)
        if message.get_performative() == MessagePerformative.COMMIT:
            self.treat_commit(message)

    def send_message(self, receiver, performative, content):
        message = Message(self, receiver, performative, content)
        message.send()
        answer = self.recv(receiver.get_channel())
        if message.needs_answer():
            self.treat_answer(answer)

    # <-- Message Sending --> #

    def send_query_list_items(self, manager):
        """TODO.
        """
        self.send_message(manager, MessagePerformative.QUERY_REF, "LIST ITEMS")

    def send_query_selected_items(self, manager):
        """TODO.
        """
        self.send_message(manager, MessagePerformative.QUERY_REF, "SELECTED ITEMS")

    def send_take_item(self, manager, item):
        """TODO.
        """
        self.send_message(manager, MessagePerformative.TAKE, item)

    def send_propose_item(self, engineer):
        """TODO.
        """
        content = self.__preferences.most_preferred(self.__list_items)
        self.send_message(engineer, MessagePerformative.PROPOSE, content)

    def send_commit_item(self, engineer, item):
        self.__commited_items.append(item)
        self.send_message(engineer, MessagePerformative.COMMIT, item)

    # <-- Message Answering --> #

    def answer_proposed_item(self, message):
        """TODO.
        """
        sender = message.get_sender()
        proposed_item = message.get_content()
        most_preferred_item = self.__preferences.most_preferred(
            self.__list_items)
        if proposed_item == most_preferred_item:
            answer = Message(self, sender, MessagePerformative.ACCEPT,
                             proposed_item)
            return answer
        else:
            answer = Message(self, sender, MessagePerformative.ASK_WHY,
                             proposed_item)
            return answer

    def answer_commited_item(self, message):
        """TODO.
        """
        sender = message.get_sender()
        item = message.get_content()
        if item not in self.__commited_items:
            self.__commited_items.append(item)
            answer = Message(self, sender, MessagePerformative.COMMIT, item)
            return answer

    # <-- Treat Answers --> #

    def treat_inform_ref(self, message):
        key, value = message.get_content()
        if key == "LIST ITEMS":
            self.__list_items = value
        if key == "SELECTED ITEMS":
            self.__selected_items = value

    def treat_accept(self, message):
        """TODO.
        """
        sender = message.get_sender()
        item = message.get_content()
        self.send_commit_item(sender, item)

    # def treat_argue(self, message):
    #     """TODO.
    #     """
    #     sender = message.get_sender()
    #     item = message.get_content()

    def treat_commit(self, message):
        """TODO.
        """
        sender = message.get_sender()
        item = message.get_content()
        if item not in self.__commited_items:
            self.send_commit_item(sender, item)
