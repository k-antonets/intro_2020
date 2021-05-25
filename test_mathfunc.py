import unittest
import mathfunc


class TestMathFuncs(unittest.TestCase):
    def setUp(self) -> None:
        self.value1 = 2
        self.value2 = 4
        self.zero = 0



    def test_add(self):
        self.assertEqual(mathfunc.add(self.value1, self.value2), 6)
        self.assertNotEqual(mathfunc.add(2, 4), 10)

    def test_mult(self):
        self.assertEqual(mathfunc.mult(1, 1), 1)
        self.assertEqual(mathfunc.mult(5, 8), 40)

    def test_div(self):
        self.assertEqual(2, mathfunc.div(self.value2, self.value1))
        self.assertEqual(0, mathfunc.div(self.zero, self.zero))
        with self.assertRaises(ZeroDivisionError):
            mathfunc.div(1, self.zero)

    def test_degree(self):
        self.assertEqual(mathfunc.degree(2, 1), 2)
        self.assertEqual(mathfunc.degree(2, 2), 4)
        self.assertEqual(0.5, mathfunc.degree(2, -1))
        with self.assertRaises(ValueError):
            mathfunc.degree(9, 0.5)
