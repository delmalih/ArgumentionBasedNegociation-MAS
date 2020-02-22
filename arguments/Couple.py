###########
# Imports #
###########


from preferences.Criterion import Criterion
from preferences.CriterionName import CriterionName
from preferences.CriterionValue import CriterionValue


##########
# Couple #
##########


class Couple:
    """Couple class.

    attr:
        criterion: the criterion for the comparison
        element: the second element for the comparison
                 (could be a criterion or a value)
    """

    def __init__(self, criterion, element):
        """Associates an Item with its criterion name and criterion value.
        """
        self.__criterion = criterion
        self.__element = element

    def __str__(self):
        if type(self.__element) == Criterion:
            if self.__criterion.get_value() > self.__element.get_value():
                return f"{self.__criterion} > {self.__element.name}"
            if self.__criterion.get_value() < self.__element.get_value():
                return f"{self.__criterion} < {self.__element.name}"
            if self.__criterion.get_value() == self.__element.get_value():
                return f"{self.__criterion} = {self.__element.name}"
        if type(self.__element) == CriterionName:
            return f"{self.__criterion} > {self.__element.name}"
        if type(self.__element) == CriterionValue:
            return f"{self.__criterion} = {self.__element.name}"
