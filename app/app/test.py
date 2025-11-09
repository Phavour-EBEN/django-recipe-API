""" Simple Test
from django.test import SimpleTestCase
from app import calc


class ViewTest(SimpleTestCase):
    def testAdd(self):
        res = calc.add(6, 3)
        self.assertEqual(res, 9)

    def testSubtract(self):
        res = calc.subtract(6, 3)
        self.assertEqual(res, 3)
"""