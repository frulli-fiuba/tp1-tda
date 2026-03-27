import unittest
from tp1_1 import main as turnos
from tp1_3 import main as cajas

class TestTurnos(unittest.TestCase):
    def test_turnos_1(self):
        # Caso facil: no hay superposiciones, puedo atender primero al primer turno y luego al segundo
        orden, ganancia = turnos([(1, 10), (2, 10)])
        self.assertEqual(orden, [0, 1])
        self.assertEqual(ganancia, 20)

    def test_turnos_2(self):
        orden, ganancia = turnos([(1, 10), (5, 20)])
        self.assertEqual(orden, [0, 1])
        self.assertEqual(ganancia, 30)
    
    def test_turnos_3(self):
        orden, ganancia = turnos([(3,25), (1,10), (2,3), (2,3)])
        self.assertEqual(orden, [1, 2, 0])
        self.assertEqual(ganancia, 38)

class TestCajas(unittest.TestCase):
    def test_cajas_1(self):
        # Caso facil: una sola caja, tiene altura 1, el orden es la unica caja con base 1 y altura 1
        altura, orden = cajas([(1, 1, 1)])
        self.assertEqual(altura, 1)
        self.assertEqual(orden, [(0, (1, 1))])

    def test_cajas_2(self):
        # Caso facil: una sola caja, tiene altura 1, el orden es la unica caja con base 1 y altura 1
        altura, orden = cajas([(1, 5, 6), (2, 4, 7)])
        self.assertEqual(altura, 10)
        self.assertEqual(orden, [(1, (2, 7)), (0, (1, 5))])

if __name__ == "__main__":
    unittest.main()
