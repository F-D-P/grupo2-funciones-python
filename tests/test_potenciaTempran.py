
from funciones.potenciaTempran import potenciaTempran
import unittest


class testTempranFuncion(unittest.TestCase):
    def test_potencia(self):
        self.assertEqual(potenciaTempran(2, 3), 8)
        self.assertEqual(potenciaTempran(5, 0), 1)
        self.assertEqual(potenciaTempran(3, 2), 9)     


if __name__ == '__main__':
    unittest.main()
    print("Ejecucion de pruebas de las funciones del grupo")
