###########
# Imports #
###########


from preferences.CriterionValue import CriterionValue


###############
# Preferences #
###############


class Preferences:
    """Preferences class.
    """

    def __init__(self):
        """Creates a new Preference.
        """
        self.__criterion_order = list()
        self.__criterions = list()

    def set_criterion_order(self, criterion_order):
        """Set the list of criterions, ordered by importance.
        """
        self.__criterion_order = criterion_order

    def get_criterion_order(self):
        """Getter for criterion_order attribute.
        """
        return self.__criterion_order

    def add_criterion(self, criterion):
        """TODO.
        """
        self.__criterions.append(criterion)

    def add_criterions(self, criterions):
        """TODO.
        """
        self.__criterions += criterions

    def get_criterion_level(self, criterion):
        for i, criterion_name in enumerate(self.__criterion_order):
            if criterion == criterion_name:
                return i
        # TODO: raise Error

    def get_criterion_value(self, criterion_name, item):
        """TODO.
        """
        for criterion in self.get_criterions_from_item(item):
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

    def compute_item_binary_score(
            self, item,
            CRITERION_THRESHOLD=CriterionValue.GOOD.value):
        """Computes the binary score of a given item.
        """
        binary_score = ["0"] * len(self.__criterion_order)
        for criterion in self.get_criterions_from_item(item):
            criterion_level = self.get_criterion_level(criterion)
            criterion_value = criterion.get_value().value
            if criterion_value >= CRITERION_THRESHOLD:
                criterion_score = "1"
            else:
                criterion_score = "0"
            binary_score[criterion_level] = criterion_score
        binary_score = "".join(binary_score)
        return binary_score

    def compute_item_score(
            self, item,
            CRITERION_THRESHOLD=CriterionValue.GOOD.value):
        """Computes the score of a given item.
        """
        binary_score = self.compute_item_binary_score(item,
                                                      CRITERION_THRESHOLD)
        return int(binary_score, 2)

    def is_preferred_criterion(self, criterion1, criterion2):
        """TODO.
        """
        level1 = self.get_criterion_level(criterion1)
        level2 = self.get_criterion_level(criterion2)
        return level1 <= level2

    def is_preferred_item(self, item1, item2):
        """TODO.
        """
        score1 = self.compute_item_score(item1)
        score2 = self.compute_item_score(item2)
        return score1 >= score2

    def most_preferred(self, items):
        """TODO.
        """
        max_score = -float("inf")
        best_item = None
        for item in items:
            item_score = self.compute_item_score(item)
            if item_score > max_score:
                max_score = item_score
                best_item = item
        return best_item

    def belongs_to_10percent_most_preferred(self, item, items):
        sorted_items = sorted(items, key=lambda i: self.compute_item_score(i),
                              reverse=True)
        most_preferred_10percent = sorted_items[:int(0.1 * len(items))]
        return item in most_preferred_10percent
