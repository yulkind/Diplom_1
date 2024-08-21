from praktikum.praktikum import Database


class TestDatabase:
    def test_available_buns(self):
        buns = Database().available_buns()
        #Проверка, что возвращаемое значение - это список
        assert isinstance(buns, list)

    def test_available_ingredients(self):
        ingredients = Database().available_ingredients()
        # Проверка, что возвращаемое значение - это список
        assert isinstance(ingredients, list)
