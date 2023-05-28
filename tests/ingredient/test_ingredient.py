from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("hmmm comida")

    assert ingredient.name == "hmmm comida"
    assert ingredient == Ingredient("hmmm comida")
    assert repr(ingredient) == "Ingredient('hmmm comida')"
    assert hash(ingredient) == hash("hmmm comida")
    assert isinstance(ingredient, Ingredient)
    assert not ingredient.restrictions
