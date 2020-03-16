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
    VERY_BAD = 0
    BAD = 1
    MEDIUM = 2
    GOOD = 3
    VERY_GOOD = 4
