import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    @pytest.mark.parametrize("name, price", [
        ('Флюоресцентная булка R2-D3', 988),
        ('Краторная булка N-200i', 1255)])
    def test_set_buns(self, name, price):
        bun = Bun(name, price)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ('Соусы', 'Соус Spicy-X', 90),
        ('Соусы', 'Соус фирменный Space Sauce', 80),
        ('Соусы', 'Соус традиционный галактический', 15),
        ('Соусы', 'Соус с шипами Антарианского плоскоходца', 88),
        ('Начинки', 'Мясо бессмертных моллюсков Protostomia', 1337)
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        ingredient1 = Ingredient('Соусы', 'Соус Spicy-X', 90)
        ingredient2 = Ingredient('Начинки', 'Мясо бессмертных моллюсков Protostomia', 1337)
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert ingredient1 not in burger.ingredients
        assert ingredient2 in burger.ingredients

    def test_move_ingredient(self):
        ingredient1 = Ingredient('Соусы', 'Соус фирменный Space Sauce', 80)
        ingredient2 = Ingredient('Начинки', 'Говяжий метеорит (отбивная)', 3000)
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1



