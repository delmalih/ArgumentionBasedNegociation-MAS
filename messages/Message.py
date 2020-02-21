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
