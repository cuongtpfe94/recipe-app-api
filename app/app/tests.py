"""
sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
  def test_add_numbers(self):
    self.assertEqual(calc.add(3, 8), 11)

  def test_subtract_numbers(self):
    func = calc.subtract(10, 2)

    self.assertEqual(func, 8)