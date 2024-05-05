from praktikum.database import Database


class TestDatabase:
    def test_available_buns_return_3_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_return_6_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
