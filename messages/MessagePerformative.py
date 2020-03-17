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
    # Those who need an answer
    PROPOSE = 1
    ASK_WHY = 3
    QUERY_REF = 5
    COMMIT = 7
    ARGUE = 9
    ACCEPT = 11
    # Those who do not need an answer
    INFORM_REF = 2
    TAKE = 4
