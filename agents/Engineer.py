###########
# Imports #
###########


from osbrain.agent import Agent

from messages.MessagePerformative import MessagePerformative
from messages.Message import Message

from arguments.Argument import Argument
from arguments.Couple import Couple


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
        self.__manager = None
        self.__used_arguments = []
        self.__proposed_item = []
        self.__was_proposed_to_me = []

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

    def register_manager(self, manager):
        self.__manager = manager

    def add_selected_item(self, item):
        """Adds an item to the list of selected items.
        """
        if item not in self.__selected_items:
            self.__selected_items.append(item)

    def get_selected_items(self):
        """Getter for selected items.
        """
        return self.__selected_items

    def get_non_proposed_items(self):
        """TODO.
        """
        non_proposed_items = []
        for item in self.__list_items:
            if item not in self.__proposed_item:
                non_proposed_items.append(item)
        return non_proposed_items

    def get_least_worst_proposed_item(self):
        """TODO.
        """
        filtered_proposed_items = []
        for k, item in enumerate(self.__proposed_item):
            if self.__was_proposed_to_me[k]:
                filtered_proposed_items.append(item)
        if len(filtered_proposed_items) > 0:
            return sorted(
                filtered_proposed_items,
                key=lambda item: self.__preferences.compute_item_score(item),
                reverse=True)[0]
        return sorted(
            self.__proposed_item,
            key=lambda item: self.__preferences.compute_item_score(item),
            reverse=True)[0]

    # <-- Message Sending --> #

    def send_message(self, receiver, performative, content):
        """Sends a message given a receiver, a performative and a content.
        """
        message = Message(self, receiver, performative, content)
        message.send()
        answer = self.recv(receiver.get_channel())
        if message.needs_answer():
            self.treat_answer(answer)

    def send_query(self, manager):
        """TODO.
        """
        self.send_message(manager, MessagePerformative.QUERY_REF, None)

    def send_propose_item(self, engineer, item):
        """Sends PROPOSE performative to an engineer with a given item.
        """
        self.__proposed_item.append(item)
        self.__was_proposed_to_me.append(False)
        self.send_message(engineer, MessagePerformative.PROPOSE, item)

    def send_ask_why_item(self, engineer, item):
        """TODO.
        """
        self.send_message(engineer, MessagePerformative.ASK_WHY, item)

    def send_argue_item(self, engineer, argument):
        """TODO.
        """
        self.send_message(engineer, MessagePerformative.ARGUE, argument)

    def send_accept_item(self, engineer, item):
        """TODO.
        """
        self.send_message(engineer, MessagePerformative.ACCEPT, item)

    def send_commit_item(self, engineer, item):
        """Send COMMIT message to an engineer.
        """
        self.add_selected_item(item)
        self.send_message(engineer, MessagePerformative.COMMIT, item)

    def send_take_item(self, manager, item):
        """TODO.
        """
        self.send_message(manager, MessagePerformative.TAKE, item)

    # <-- Message Answering --> #

    def handle_message_reception(self, message):
        """TODO.
        """
        if message.get_performative() == MessagePerformative.PROPOSE:
            answer = self.answer_proposed_item(message)
        if message.get_performative() == MessagePerformative.ASK_WHY:
            answer = self.answer_ask_why_item(message)
        if message.get_performative() == MessagePerformative.ARGUE:
            answer = self.answer_argue_item(message)
        if message.get_performative() == MessagePerformative.ACCEPT:
            answer = self.answer_accepted_item(message)
        if message.get_performative() == MessagePerformative.COMMIT:
            answer = self.answer_commited_item(message)
        if message.needs_answer():
            self.log_info(answer)
        return answer

    def answer_proposed_item(self, message):
        """Answers to a proposed Item.
        """
        sender = message.get_sender()
        proposed_item = message.get_content()
        self.__proposed_item.append(proposed_item)
        self.__was_proposed_to_me.append(True)
        is_accepted = self.__preferences.belongs_to_10percent_most_preferred(
            proposed_item, self.__list_items)
        if is_accepted:
            answer = Message(self, sender, MessagePerformative.ACCEPT,
                             proposed_item)
            return answer
        else:
            answer = Message(self, sender, MessagePerformative.ASK_WHY,
                             proposed_item)
            return answer

    def answer_accepted_item(self, message):
        """TODO.
        """
        sender = message.get_sender()
        item = message.get_content()
        answer = Message(self, sender, MessagePerformative.COMMIT, item)
        return answer

    def answer_commited_item(self, message):
        """Answer to a commit message.
        """
        sender = message.get_sender()
        item = message.get_content()
        if item not in self.__selected_items:
            self.add_selected_item(item)
            answer = Message(self, sender, MessagePerformative.COMMIT, item)
            return answer
        else:
            self.send_take_item(self.__manager, item)
            return

    def answer_ask_why_item(self, message):
        """TODO.
        """
        sender = message.get_sender()
        item = message.get_content()
        argument = self.argue_item(item, is_positive=True)
        if argument is not None:
            self.__used_arguments.append(argument)
            answer = Message(self, sender, MessagePerformative.ARGUE, argument)
        else:
            non_proposed_items = self.get_non_proposed_items()
            if len(non_proposed_items) > 0:
                item = self.__preferences.most_preferred(non_proposed_items)
                answer = Message(self, sender, MessagePerformative.PROPOSE,
                                 item)
            else:
                item = self.get_least_worst_proposed_item()
                answer = Message(self, sender, MessagePerformative.ACCEPT,
                                 item)
        return answer

    def answer_argue_item(self, message):
        """TODO.
        """
        sender = message.get_sender()
        received_argument = message.get_content()
        self.__used_arguments.append(received_argument)
        item = received_argument.get_item()
        is_positive = not received_argument.is_positive_argument()
        argument = self.argue_item(item, is_positive=is_positive)
        if argument is not None:
            self.__used_arguments.append(argument)
            answer = Message(self, sender, MessagePerformative.ARGUE, argument)
        else:
            non_proposed_items = self.get_non_proposed_items()
            if len(non_proposed_items) > 0:
                item = self.__preferences.most_preferred(non_proposed_items)
                self.__proposed_item.append(item)
                self.__was_proposed_to_me.append(False)
                answer = Message(self, sender, MessagePerformative.PROPOSE,
                                 item)
            else:
                item = self.get_least_worst_proposed_item()
                answer = Message(self, sender, MessagePerformative.ACCEPT,
                                 item)
        return answer

    # <-- Treat Answers --> #

    def treat_answer(self, message):
        """TODO.
        """
        if message.get_performative() == MessagePerformative.INFORM_REF:
            self.treat_inform_ref(message)
        if message.get_performative() == MessagePerformative.PROPOSE:
            self.treat_propose(message)
        if message.get_performative() == MessagePerformative.ACCEPT:
            self.treat_accept(message)
        if message.get_performative() == MessagePerformative.ASK_WHY:
            self.treat_ask_why(message)
        if message.get_performative() == MessagePerformative.ARGUE:
            self.treat_argue(message)
        if message.get_performative() == MessagePerformative.COMMIT:
            self.treat_commit(message)

    def treat_inform_ref(self, message):
        self.__list_items = message.get_content()

    def treat_propose(self, message):
        """TODO.
        """
        sender = message.get_sender()
        proposed_item = message.get_content()
        self.__proposed_item.append(proposed_item)
        self.__was_proposed_to_me.append(True)
        is_accepted = self.__preferences.belongs_to_10percent_most_preferred(
            proposed_item, self.__list_items)
        if is_accepted:
            self.send_accept_item(sender, proposed_item)
        else:
            self.send_ask_why_item(sender, proposed_item)

    def treat_accept(self, message):
        """Treat ACCEPT received message.
        """
        sender = message.get_sender()
        item = message.get_content()
        self.send_commit_item(sender, item)

    def treat_ask_why(self, message):
        """Treat ASK_WHY received message.
        """
        sender = message.get_sender()
        item = message.get_content()
        argument = self.argue_item(item, is_positive=True)
        if argument is not None:
            self.__used_arguments.append(argument)
            self.send_argue_item(sender, argument)
        else:
            non_proposed_items = self.get_non_proposed_items()
            if len(non_proposed_items) > 0:
                item = self.__preferences.most_preferred(non_proposed_items)
                self.send_propose_item(sender, item)
            else:
                self.send_accept_item(sender, item)

    def treat_argue(self, message):
        """Treat ARGUE received message.
        """
        sender = message.get_sender()
        received_argument = message.get_content()
        self.__used_arguments.append(received_argument)
        item = received_argument.get_item()
        is_positive = not received_argument.is_positive_argument()
        argument = self.argue_item(item, is_positive=is_positive)
        if argument is not None:
            self.__used_arguments.append(argument)
            self.send_argue_item(sender, argument)
        else:
            non_proposed_items = self.get_non_proposed_items()
            if len(non_proposed_items) > 0:
                item = self.__preferences.most_preferred(non_proposed_items)
                self.send_propose_item(sender, item)
            else:
                item = self.get_least_worst_proposed_item()
                self.send_accept_item(sender, item)

    def treat_commit(self, message):
        """Treat COMMIT message.
        """
        sender = message.get_sender()
        item = message.get_content()
        if item not in self.__selected_items:
            self.send_commit_item(sender, item)
        else:
            self.send_take_item(self.__manager, item)

    # <-- Argumentation --> #

    def generate_arguments(self, item, is_positive):
        """Generates an argument given an item.
        """
        arguments = []
        binary_score = self.__preferences.compute_item_binary_score(item)
        criterion_order = self.__preferences.get_criterion_order()
        if is_positive:
            requested_score = "1"
        else:
            requested_score = "0"
        for k, criterion_name in enumerate(criterion_order):
            if binary_score[k] == requested_score:
                criterion_value = self.__preferences.get_criterion_value(
                    criterion_name, item)
                couple = Couple(criterion_name, criterion_value)
                argument = Argument(item, is_positive, [couple])
                if argument not in self.__used_arguments:
                    arguments.append(argument)
        return arguments

    def argue_item(self, item, is_positive):
        arguments = self.generate_arguments(item, is_positive=is_positive)
        if len(arguments) > 0:
            argument = arguments[0]
            return argument
        return None

    # <-- RUN --> #

    def start_negotiation(self, engineer):
        """Starts the negotiation between engineers.
        """
        item = self.__preferences.most_preferred(self.get_non_proposed_items())
        self.send_propose_item(engineer, item)
