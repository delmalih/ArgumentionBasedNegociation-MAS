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
    
    def get_criterion_level_from_criterion(self, criterion):
        for i in range(len(self.__criterion_order)):
            if criterion.get_name() == self.__criterion_order[i].value:
                return len(self.__criterion_order) - i
        # TODO: raise Error
    
    def get_criterion_level_from_criterion_name(self, criterion_name):
        for i in range(len(self.__criterion_order)):
            if criterion_name.value == self.__criterion_order[i].value:
                return len(self.__criterion_order) - i
        # TODO: raise Error
    
    def add_criterion(self, criterion):
        """TODO.
        """
        self.__criterions.append(criterion)
    
    def get_criterion_value_from_name(self, criterion_name):
        """TODO.
        """
        for criterion in self.__criterions:
            if criterion.get_name() == criterion_name.value:
                return criterion.get_value()
        # TODO: raise Error
    
    def get_criterions_from_item(self, item):
        """TODO.
        """
        criterions = list()
        for criterion in self.__criterions:
            criterion_item = criterion.get_item()
            if criterion_item.get_name() == item.get_name():
                criterions.append(criterion)
        return criterions
    
    def get_criterion_weight(self, criterion):
        """TODO.
        """
        return self.get_criterion_level_from_criterion(criterion)

    def compute_item_score(self, item):
        """Computes the score of a given item.
        """
        score = 0
        for criterion in self.get_criterions_from_item(item):
            criterion_value = criterion.get_value()
            criterion_weight = self.get_criterion_weight(criterion)
            score += criterion_value * criterion_weight
        return score
    
    def is_preferred_criterion(self, criterion_name1, criterion_name2):
        """TODO.
        """
        level1 = self.get_criterion_level_from_criterion_name(criterion_name1)
        level2 = self.get_criterion_level_from_criterion_name(criterion_name2)
        return level1 >= level2
    
    def is_preferred_item(self, item1, item2):
        score1 = self.compute_item_score(item1)
        score2 = self.compute_item_score(item2)
        return score1 >= score2