import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_succes(self):
        assert self.calc.adding(1, 1) == 2

    def test_division_succes(self):
        assert self.calc.division(100, 25) == 4

    def test_multiply_success(self):
        assert self.calc.multiply(15, 3) == 45

    def test_subtraction_succes(self):
        assert self.calc.subtraction(154, 30) == 124
