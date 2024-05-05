import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price',
                             [
                                 ["black bun", 100],
                                 ["", 500],
                                 ["Тестовая булка", 700]
                             ])
    def test_get_name_return_expected_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name, 'Название булочки не соответствует ожидаемому'

    @pytest.mark.parametrize('name, price',
                             [
                                 ["black bun", 100],
                                 ["white bun", 0],
                                 ["red bun", -1],
                                 ["red bun", 10000000]
                             ])
    def test_get_price_return_expected_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price, 'Цена булочки не соответствует ожидаемой'
