import unittest

def suma(num1, num2):
    return num1 + num2

class cajanegraTest(unittest.TestCase):

    def test_sumar_dos_positivos(self):
        num1 = 10
        num2 = 5
        result = suma(num1, num2)
        self.assertEqual(result, 15)

    def test_suma_dos_negativos(self):
        num1 = -5
        num2 = -12
        result = suma(num1, num2)
        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()