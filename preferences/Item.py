########
# Item #
########


class Item:
    """Item class.
    This class implements the objects about which the argumentation will be
    conducted.

    attr:
        name: the name of the item
        description: the description of the item
    """

    def __init__(self, name, description):
        """Creates a new Item.
        """
        self.__name = name
        self.__description = description

    def get_name(self):
        """Getter for the name.
        """
        return self.__name

    def get_value(self, preference, criterion_name):
        """TODO.
        """
        return preference.get_criterion_value(criterion_name)

    def __eq__(self, item):
        """TODO.
        """
        if type(item) == str:
            return self.__name == item
        return self.__name == item.get_name()

    def __repr__(self):
        """TODO.
        """
        return f"{self.__name}"
