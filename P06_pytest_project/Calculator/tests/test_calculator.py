from Calculator.Calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()
 
        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()
 
        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 43
        b = 12
        cal = Calculator()
 
        # act
        result = cal.multiply(a, b)

        # assert
        expected = 516
        assert result == expected

    def test_divide(self):
        # arrange
        a = 321
        b = 12
        cal = Calculator()
 
        # act
        result = cal.divide(a, b)

        # assert
        expected = 26.75
        assert result == expected