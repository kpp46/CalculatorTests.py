import unittest

from Calculator import Calculator


class CalTestClass(unittest.TestCase):
    def test_instantiated_calculator(self):
        calculator: Calculator()
        self.assertIsInstance(calculator, Calculator)

    if __name__ == '__main__':
        unittest.main()
