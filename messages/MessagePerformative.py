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
    # Those who does not need an answer
    ACCEPT = 2
    ARGUE = 4
    INFORM_REF = 6
    TAKE = 8
