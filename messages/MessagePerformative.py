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
    PROPOSE = 1
    ACCEPT = 2
    COMMIT = 3
    ASK_WHY = 4
    ARGUE = 5
    QUERY_REF = 6
    INFORM_REF = 7
