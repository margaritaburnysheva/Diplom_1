from unittest.mock import Mock

import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture(scope="function")
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = 'Test bun'
    mock_bun.price = 100
    mock_bun.get_name.return_value = 'Test bun'
    mock_bun.get_price.return_value = 100
    return mock_bun

@pytest.fixture(scope="function")
def mock_ingredient_sauce():
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.ingredient_type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.name = 'test sauce'
    mock_ingredient_sauce.price = 200
    mock_ingredient_sauce.get_name.return_value = 'test sauce'
    mock_ingredient_sauce.get_price.return_value = 200
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient_sauce

@pytest.fixture(scope="function")
def mock_ingredient_filling():
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.ingredient_type = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.name = 'test filling'
    mock_ingredient_filling.price = 300
    mock_ingredient_filling.get_name.return_value = 'test filling'
    mock_ingredient_filling.get_price.return_value = 300
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_ingredient_filling
