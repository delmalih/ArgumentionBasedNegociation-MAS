##########
# Couple #
##########


class Couple:
    """Couple class.

    attr:
        criterion: the criterion for the comparison
        element: the second element for the comparison
                 (could be a criterion or a value)
        link: the link between criterion and element
              (could be >, < and =)
    """

    def __init__(self, criterion_name, element, link="="):
        """Associates an Item with its criterion name and criterion value.
        """
        self.__criterion_name = criterion_name
        self.__element = element
        self.__link = link

    def __repr__(self):
        criterion_name = self.__criterion_name.name
        link = self.__link
        element_name = self.__element.name
        return f"{criterion_name}{link}{element_name}"
