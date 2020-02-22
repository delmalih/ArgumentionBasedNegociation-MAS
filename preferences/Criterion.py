###########
# Imports #
###########


from CriterionName import CriterionName


#############
# Criterion #
#############


class Criterion:
    """Criterion class.

    attr:
        item: the item to be associated with a criterion value and name
        criterion_name: the criterion name for the item
        criterion_value: the criterion value for the item
    """

    def __init__(self, item, criterion_name, criterion_value):
        """Associates an Item with its criterion name and criterion value.
        """
        self.__item = item
        self.__criterion_name = criterion_name
        self.__criterion_value = criterion_value

    def get_item(self):
        """Getter for the item.
        """
        return self.__item

    def get_name(self):
        """Getter for the criterion name.
        """
        return self.__criterion_name

    def get_value(self):
        """Getter for the criterion value.
        """
        return self.__criterion_value

    def __eq__(self, criterion):
        """TODO.
        """
        if type(criterion) == str:
            return self.__criterion_name.name == criterion
        if type(criterion) == int:
            return self.__criterion_name.value == criterion
        if type(criterion) == CriterionName:
            return self.__criterion_name.value == criterion.value
        if type(criterion) == Criterion:
            return self.__criterion_name.value == criterion.get_name().value
        return False

    def __str__(self):
        return self.get_name()
