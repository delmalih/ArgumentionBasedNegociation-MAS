class Preferences:
    """Preferences class.
    """

    def __init__(self):
        """Creates a new Preference.
        """
        self.__criterion_order = list()
        self.__criterions = list()

    def set_criterion_name_list(self, criterion_names):
        """Set the list of criterions, ordered by importance.
        """
        self.__criterion_order = criterion_names

    def get_criterion_level(self, criterion):
        for i, criterion_name in enumerate(self.__criterion_order):
            if criterion == criterion_name:
                return len(self.__criterion_order) - i
        # TODO: raise Error

    def add_criterion(self, criterion):
        """TODO.
        """
        self.__criterions.append(criterion)

    def get_criterion_value(self, criterion_name):
        """TODO.
        """
        for criterion in self.__criterions:
            if criterion == criterion_name:
                return criterion.get_value()
        # TODO: raise Error

    def get_criterions_from_item(self, item):
        """TODO.
        """
        criterions = list()
        for criterion in self.__criterions:
            if criterion.get_item() == item:
                criterions.append(criterion)
        return criterions

    def get_criterion_weight(self, criterion):
        """TODO.
        """
        return self.get_criterion_level(criterion)

    def compute_item_score(self, item):
        """Computes the score of a given item.
        """
        score = 0
        for criterion in self.get_criterions_from_item(item):
            criterion_value = criterion.get_value().value
            criterion_weight = self.get_criterion_weight(criterion)
            score += criterion_value * criterion_weight
        return score

    def is_preferred_criterion(self, criterion1, criterion2):
        """TODO.
        """
        level1 = self.get_criterion_level(criterion1)
        level2 = self.get_criterion_level(criterion2)
        return level1 >= level2

    def is_preferred_item(self, item1, item2):
        """TODO.
        """
        score1 = self.compute_item_score(item1)
        score2 = self.compute_item_score(item2)
        return score1 >= score2

    def most_preferred(self, items):
        """TODO.
        """
        max_score = 0
        best_item = None
        for item in items:
            item_score = self.compute_item_score(item)
            if item_score > max_score:
                max_score = item_score
                best_item = item
        return best_item
