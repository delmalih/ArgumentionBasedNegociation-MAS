###########
# Imports #
###########


import enum


##################
# CriterionValue #
##################


class CriterionValue(enum.Enum):
    """CriterionValue class.
    """
    VERY_BAD = -1e1
    BAD = -1e0
    MEDIUM = 0
    GOOD = 1e0
    VERY_GOOD = 1e1
