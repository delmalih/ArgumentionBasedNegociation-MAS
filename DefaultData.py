###########
# Imports #
###########


from preferences.Item import Item
from preferences.Criterion import Criterion
from preferences.CriterionName import CriterionName
from preferences.CriterionValue import CriterionValue


#########
# ITEMS #
#########


diesel_engine = Item("ICED", "A super cool diesel engine")
electric_engine = Item("E", "A very quiet engine")
DEFAULT_ITEMS = [diesel_engine, electric_engine]


##############
# CRITERIONS #
##############


DEFAULT_CRITERIONS = [
    Criterion(
        diesel_engine,
        CriterionName.PRODUCTION_COST,
        CriterionValue.VERY_GOOD),
    Criterion(
        diesel_engine,
        CriterionName.CONSUMPTION,
        CriterionValue.GOOD),
    Criterion(
        diesel_engine,
        CriterionName.DURABILITY,
        CriterionValue.VERY_GOOD),
    Criterion(
        diesel_engine,
        CriterionName.ENVIRONMENT_IMPACT,
        CriterionValue.VERY_BAD),
    Criterion(
        diesel_engine,
        CriterionName.NOISE,
        CriterionValue.VERY_BAD),
    Criterion(
        electric_engine,
        CriterionName.PRODUCTION_COST,
        CriterionValue.BAD),
    Criterion(
        electric_engine,
        CriterionName.CONSUMPTION,
        CriterionValue.VERY_BAD),
    Criterion(
        electric_engine,
        CriterionName.DURABILITY,
        CriterionValue.GOOD),
    Criterion(
        electric_engine,
        CriterionName.ENVIRONMENT_IMPACT,
        CriterionValue.VERY_GOOD),
    Criterion(
        electric_engine,
        CriterionName.NOISE,
        CriterionValue.VERY_GOOD),
]
