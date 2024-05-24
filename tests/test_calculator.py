from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 0
        cal = Calculator()

        # act & assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)
