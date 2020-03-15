###########
# Imports #
###########


import unittest

from preferences.Item import Item
from preferences.Criterion import Criterion
from preferences.Preferences import Preferences
from preferences.CriterionName import CriterionName
from preferences.CriterionValue import CriterionValue


###################
# TestPreferences #
###################


class TestPreferences(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__preference = Preferences()
        self.__diesel_engine = Item("ICED",
                                    "A super cool diesel engine")
        self.__electric_engine = Item("E",
                                      "A very quiet engine")
        self.setup()

    def setup(self):
        # Set criterion name list
        self.__preference.set_criterion_name_list([
            CriterionName.PRODUCTION_COST,
            CriterionName.CONSUMPTION,
            CriterionName.DURABILITY,
            CriterionName.ENVIRONMENT_IMPACT,
            CriterionName.NOISE,
        ])

        # Set criterions
        self.__preference.add_criterion(Criterion(
            self.__diesel_engine,
            CriterionName.PRODUCTION_COST,
            CriterionValue.VERY_GOOD))
        self.__preference.add_criterion(Criterion(
            self.__diesel_engine,
            CriterionName.CONSUMPTION,
            CriterionValue.GOOD))
        self.__preference.add_criterion(Criterion(
            self.__diesel_engine,
            CriterionName.DURABILITY,
            CriterionValue.VERY_GOOD))
        self.__preference.add_criterion(Criterion(
            self.__diesel_engine,
            CriterionName.ENVIRONMENT_IMPACT,
            CriterionValue.VERY_BAD))
        self.__preference.add_criterion(Criterion(
            self.__diesel_engine,
            CriterionName.NOISE,
            CriterionValue.VERY_BAD))
        self.__preference.add_criterion(Criterion(
            self.__electric_engine,
            CriterionName.PRODUCTION_COST,
            CriterionValue.BAD))
        self.__preference.add_criterion(Criterion(
            self.__electric_engine,
            CriterionName.CONSUMPTION,
            CriterionValue.VERY_BAD))
        self.__preference.add_criterion(Criterion(
            self.__electric_engine,
            CriterionName.DURABILITY,
            CriterionValue.GOOD))
        self.__preference.add_criterion(Criterion(
            self.__electric_engine,
            CriterionName.ENVIRONMENT_IMPACT,
            CriterionValue.VERY_GOOD))
        self.__preference.add_criterion(Criterion(
            self.__electric_engine,
            CriterionName.NOISE,
            CriterionValue.VERY_GOOD))

    def test_item_value(self):
        value = self.__diesel_engine.get_value(
            self.__preference,
            CriterionName.PRODUCTION_COST)
        self.assertEqual(value, CriterionValue.VERY_GOOD)

    def test_is_preferred_criterion(self):
        is_preferred = self.__preference.is_preferred_criterion(
            CriterionName.CONSUMPTION,
            CriterionName.NOISE)
        self.assertTrue(is_preferred)

    def test_score(self):
        score1 = self.__preference.compute_item_score(self.__diesel_engine)
        score2 = self.__preference.compute_item_score(self.__electric_engine)
        self.assertEqual(score1, 54)
        self.assertEqual(score2, -12)

    def test_is_preferred_item(self):
        is_preferred1 = self.__preference.is_preferred_item(
            self.__diesel_engine,
            self.__electric_engine)
        is_preferred2 = self.__preference.is_preferred_item(
            self.__electric_engine,
            self.__diesel_engine)
        self.assertTrue(is_preferred1)
        self.assertFalse(is_preferred2)

    def test_most_preferred(self):
        most_preferred_item = self.__preference.most_preferred([
            self.__diesel_engine, self.__electric_engine])
        self.assertTrue(most_preferred_item == self.__diesel_engine)
