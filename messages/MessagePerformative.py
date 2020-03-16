###########
# Imports #
###########


import enum


#######################
# MessagePerformative #
#######################


class MessagePerformative(enum.Enum):
    """MessagePerformative class.
    """
    # Those who needs an answer
    PROPOSE = 1
    ASK_WHY = 3
    QUERY_REF = 5
    COMMIT = 7
    ARGUE = 9
    # Those who does not need an answer
    ACCEPT = 2
    INFORM_REF = 4
    TAKE = 6
