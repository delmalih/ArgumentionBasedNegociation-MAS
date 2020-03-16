############
# Argument #
############


class Argument:
    """Argument class.

    attr:
        item: the item agent argue for
        is_positive: boolean indicating if the argument is
                     positive for the item
        list_couples: the couples
    """

    def __init__(self, item, is_positive, list_couples):
        """Associates an Item with its criterion name and criterion value.
        """
        self.__item = item
        self.__is_positive = is_positive
        self.__list_couples = list_couples

    def get_item(self):
        """Getter for the item.
        """
        return self.__item

    def is_positive_argument(self):
        """Getter for the criterion name.
        """
        return self.__is_positive

    def __repr__(self):
        """TODO.
        """
        if self.__is_positive:
            B = f"{self.__item}"
        else:
            B = f"not {self.__item}"
        list_couples_str = map(lambda x: x.__repr__(), self.__list_couples)
        A = ", ".join(list_couples_str)
        return f"{B} <= {A}"

    def __eq__(self, argument):
        return self.__repr__() == argument.__repr__()
