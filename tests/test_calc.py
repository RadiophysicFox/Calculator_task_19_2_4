from app.calculator import Calculator
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_multiply_success(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(6, 3) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(7, 8) == -1

    def teardown(self):
        print("Выполнение метода Teardown")
