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
    VERY_BAD = 1
    BAD = 2
    MEDIUM = 3
    GOOD = 4
    VERY_GOOD = 5
