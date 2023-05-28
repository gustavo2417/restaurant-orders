from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("frango a milanesa", 50.00)

    assert dish == Dish("frango a milanesa", 50.00)
    assert repr(dish) == "Dish('frango a milanesa', R$50.00)"
    assert dish.name == "frango a milanesa"
    assert hash(dish) == hash(repr(dish))

    ingredient1 = Ingredient("Peito de frango")
    ingredient2 = Ingredient("Farinha de Rosca")
    dish.add_ingredient_dependency(ingredient1, 1)
    dish.add_ingredient_dependency(ingredient2, 1)

    assert dish.get_restrictions() == set()
    assert dish.get_ingredients() == set({ingredient1, ingredient2})
    assert isinstance(dish, Dish)

    with pytest.raises(TypeError):
        Dish("Frango", "100.00")
    with pytest.raises(ValueError):
        Dish("Arroz", -10.00)
