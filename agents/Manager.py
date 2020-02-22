###########
# Imports #
###########


from osbrain.agent import Agent

from messages.MessagePerformative import MessagePerformative
from messages.Message import Message


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

        """Initializes the communication channels.
        """
        self.bind('REP', alias=f"{self.name}-channel",
                  handler=self.answer_handler)
        self.__channel = f"{self.name}-channel"

        """Prints that the agent is initialized
        """
        self.log_info(f"{self.name} is initialized !")

    def set_list_items(self, items):
        """Setter for list_items attribute.
        """
        self.__list_items = items

    def add_selected_item(self, item):
        """Adds an item to the list of selected items.
        """
        if item not in self.__selected_items:
            self.__selected_items.append(item)

    def get_channel(self):
        """Getter for the channel attribute.
        """
        return self.__channel

    def send_message(self, receiver, performative, content):
        message = Message(self, receiver, performative, content)
        message.send()

    def answer_handler(self, message):
        """TODO.
        """
        if message.get_performative() == MessagePerformative.QUERY_REF:
            answer = self.answer_query_ref(message)
        if message.get_performative() == MessagePerformative.TAKE:
            answer = self.answer_take(message)
        if message.needs_answer():
            self.log_info(answer)
        return answer

    def answer_query_ref(self, message):
        """TODO.
        """
        if message.get_content() == "LIST ITEMS":
            return self.answer_request_list_items(message)
        if message.get_content() == "SELECTED ITEMS":
            return self.answer_request_selected_items(message)

    def answer_request_list_items(self, message):
        """TODO.
        """
        receiver = message.get_sender()
        performative = MessagePerformative.INFORM_REF
        content = ("LIST ITEMS", self.__list_items)
        return Message(self, receiver, performative, content)

    def answer_request_selected_items(self, message):
        """TODO.
        """
        receiver = message.get_sender()
        performative = MessagePerformative.INFORM_REF
        content = ("SELECTED ITEMS", self.__selected_items)
        return Message(self, receiver, performative, content)

    def answer_take(self, message):
        """TODO.
        """
        item = message.get_content()
        self.add_selected_item(item)
        return
