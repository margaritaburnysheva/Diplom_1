import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                                 [INGREDIENT_TYPE_SAUCE, "sour cream", 0],
                                 [INGREDIENT_TYPE_FILLING, "sausage", -1],
                                 [INGREDIENT_TYPE_FILLING, "sausage", 10000000000]
                             ])
    def test_get_price_return_expected_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, 'Цена ингредиента не соответствует ожидаемой'

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                                 [INGREDIENT_TYPE_SAUCE, "", 200],
                                 [INGREDIENT_TYPE_SAUCE, " ", 300],
                                 [INGREDIENT_TYPE_FILLING, "начинка", 100],
                                 [INGREDIENT_TYPE_FILLING, "dinosaurdinosaurdinosaurdinosaurdinosaurdinosaur", 200]
                             ])
    def test_get_name_return_expected_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, 'Название ингредиента не соответствует ожидаемому'

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                                 [INGREDIENT_TYPE_FILLING, "cutlet", 100]
                             ])
    def test_get_type_return_expected_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, 'Тип ингредиента не соответствует ожидаемому'
