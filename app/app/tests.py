
from django.test import TestCase

from app.calc import Calculator


class calcTes(TestCase):


    def test_add(self):
        calculator = Calculator()
        result = calculator.add(5, 6)
        self.assertEqual(result, 11)

    def test_sub(self):
        calculator = Calculator()
        result = calculator.sub(5, 6)
        self.assertEqual(result, -1)