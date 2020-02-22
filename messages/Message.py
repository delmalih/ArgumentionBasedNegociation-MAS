###########
# Message #
###########


class Message:
    """Message class.
    This class implements the message object which is exchanged between
    agent during communication

    attr:
        sender: the agent who sends the message
        receiver: the agent who receives the message
        performative: the performative verb
        content: the message content
    """

    def __init__(self, sender, receiver, performative, content):
        """Associates an Item with its criterion name and criterion value.
        """
        self.__sender = sender
        self.__receiver = receiver
        self.__performative = performative
        self.__content = content

    def __str__(self):
        """String represention of the class elements.
        """
        snd = self.__sender.get_attr("name")
        rcv = self.__receiver.get_attr("name")
        per = self.__performative.name
        content = self.__content
        return f"{snd} to {rcv} : {per}({content})"

    def get_sender(self):
        """Getter for the sender attribute.
        """
        return self.__sender

    def get_receiver(self):
        """Getter for the receiver attribute.
        """
        return self.__receiver

    def get_performative(self):
        """Getter for the performative attribute.
        """
        return self.__performative

    def get_content(self):
        """Getter for the content attribute.
        """
        return str(self.__content)

    def needs_answer(self):
        """Returns true if the message needs an answer from the receiver.
        """
        return self.get_performative().value % 2 == 1

    def send(self):
        sender = self.get_sender()
        receiver = self.get_receiver()
        sender.log_info(self)
        sender.send(receiver.get_channel(), self)
