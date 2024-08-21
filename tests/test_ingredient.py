from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        ingredient_type = 'Начинки'
        name = 'Говяжий метеорит (отбивная)'
        price = 3000
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_price()
        assert actual_result

    def test_get_name(self):
        ingredient_type = 'Начинки'
        name = 'Говяжий метеорит (отбивная)'
        price = 3000
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_price()
        assert actual_result

    def test_get_type(self):
        ingredient_type = 'Начинки'
        name = 'Говяжий метеорит (отбивная)'
        price = 3000
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_price()
        assert actual_result
