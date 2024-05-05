from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_is_real(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, 'Ошибка при выборе булoчки'

    def test_add_ingredient_is_real(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert mock_ingredient_sauce in burger.ingredients and mock_ingredient_filling in burger.ingredients, 'Ошибка при добавлении ингредиента'

    def test_remove_ingredient_is_real(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == [], 'Ошибка при удалении ингредиента'

    def test_move_ingredient_is_real(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        first_will_be_second = burger.ingredients[0]
        second_will_be_first = burger.ingredients[1]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == second_will_be_first and burger.ingredients[1] == first_will_be_second, 'Ошибка при перемещении ингредиентов'

    def test_get_price_return_expected_price(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        expected_price = 700  # 100*2 + 200 + 300
        assert burger.get_price() == expected_price, 'Ошибка при расчете стоимости бургера'

    def test_get_receipt_return_expected_receipt(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        expected_receipt = f'(==== Test bun ====)\n= sauce test sauce =\n= filling test filling =\n(==== Test bun ====)\n\nPrice: 700'
        assert burger.get_receipt() == expected_receipt, 'Ошибка в чеке с информацией о бургере'
