import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ('Флюоресцентная булка R2-D3', 988),
        ('Краторная булка N-200i', 1255), ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        actual_result = bun.get_name()
        assert actual_result == name

    @pytest.mark.parametrize("name, price", [
        ('Флюоресцентная булка R2-D3', 988),
        ('Краторная булка N-200i', 1255), ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        actual_result = bun.get_price()
        assert actual_result == price

    def test_empty_name(self):
        name = ''
        price = 988
        bun = Bun(name, price)
        actual_result = bun.get_name()
        assert actual_result == ''

    def test_zero_price(self):
        name = 'Краторная булка N-200i'
        price = 0
        bun = Bun(name, price)
        actual_result = bun.get_price()
        assert actual_result == 0

    def test_invalid_price_type(self):
        name = 'Краторная булка N-200i'
        price = 'string'
        bun = Bun(name, price)
        actual_result = bun.get_price()
        assert actual_result == 'string'

    def test_negative(self):
        name = 'Краторная булка N-200i'
        price = -988
        bun = Bun(name, price)
        actual_result = bun.get_price()
        assert actual_result == -988
