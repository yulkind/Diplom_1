import pytest

from praktikum.bun import Bun


class TestBun:
    price = 988
    name = 'Флюоресцентная булка R2-D3'

    @pytest.mark.parametrize("name", ['Флюоресцентная булка R2-D3', '', 123, 'N-i'])
    def test_get_name(self, name):
        bun = Bun(name, self.price)
        actual_result = bun.get_name()
        assert actual_result == name

    @pytest.mark.parametrize("price", [988, (-1), 0, 'bun'])
    def test_get_price(self, price):
        bun = Bun(self.name, price)
        actual_result = bun.get_price()
        assert actual_result == price

    def test_empty_name(self):
        name = ''
        bun = Bun(name, self.price)
        actual_result = bun.get_name()
        assert actual_result == ''

    def test_zero_price(self):
        price = 0
        bun = Bun(self.name, price)
        actual_result = bun.get_price()
        assert actual_result == 0

    def test_invalid_price_type(self):
        price = 'string'
        bun = Bun(self.name, price)
        actual_result = bun.get_price()
        assert actual_result == 'string'

    def test_negative_price(self):
        price = -988
        bun = Bun(self.name, price)
        actual_result = bun.get_price()
        assert actual_result == -988
