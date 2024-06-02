import unittest
from calculadora import suma, resta, multiplicacion, division, raiz_cuadrada, exponencial

class TestOperacionesBasicas(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)
        self.assertEqual(resta(-1, 1), -2)
        self.assertEqual(resta(-1, -1), 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 5), 15)
        self.assertEqual(multiplicacion(-1, 1), -1)
        self.assertEqual(multiplicacion(-1, -1), 1)

    def test_division(self):
        self.assertEqual(division(10, 5), 2)
        self.assertEqual(division(-1, 1), -1)
        self.assertEqual(division(10, 0), "Error: División por cero")

class TestOperacionesAvanzadas(unittest.TestCase):

    def test_raiz_cuadrada(self):
        self.assertAlmostEqual(raiz_cuadrada(9), 3, places=3)
        self.assertAlmostEqual(raiz_cuadrada(16), 4, places=3)
        self.assertRaises(ValueError, raiz_cuadrada, -1)  
    def test_exponencial(self):
        self.assertAlmostEqual(exponencial(1), 2.718, places=3)
        self.assertAlmostEqual(exponencial(0), 1, places=3)

if __name__ == '__main__':
    unittest.main()
