import unittest
from  modules.ArbolAVL import ArbolAVL
from modules.NodoArbol import NodoArbol


class TestArbolAVL(unittest.TestCase):
    def setUp(self):
        self.arbol = ArbolAVL()
        # Insertar algunos nodos (clave, valor)
        for clave, valor in [(20, 'a'), (10, 'b'), (30, 'c'), (5, 'd'), (15, 'e'), (25, 'f'), (35, 'g')]:
            self.arbol.agregar(clave, valor)

    def test_buscar_existente(self):
        nodo = self.arbol.buscar(10)
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.clave, 10)
        self.assertEqual(nodo.cargaUtil, 'b')

    def test_buscar_inexistente(self):
        nodo = self.arbol.buscar(99)
        self.assertIsNone(nodo)

    def test_eliminar_hoja(self):
        self.arbol.eliminar(5)
        self.assertIsNone(self.arbol.buscar(5))

    def test_eliminar_con_un_hijo(self):
        self.arbol.eliminar(35)
        self.assertIsNone(self.arbol.buscar(35))

    def test_eliminar_con_dos_hijos(self):
        self.arbol.eliminar(10)
        self.assertIsNone(self.arbol.buscar(10))

    def test_buscar_min(self): ##estan comentados porque hubo que cambiar el metodo para que funcione con el valor.
        valor_min = self.arbol.buscar_min(10, 30)
        self.assertEqual(valor_min, 'a')  # 10 -> 'a'

    def test_buscar_max(self): ## lo mismo que el metodo buscar_min
        valor_max = self.arbol.buscar_max(10, 30)
        self.assertEqual(valor_max, 'f')  # 30 -> 'f'

    def test_buscar_rango(self):
        nodos = self.arbol.buscar_rango(10, 25)
        claves = sorted([n.clave for n in nodos])
        self.assertEqual(claves, [10, 15, 20, 25])

    def test_extraer(self):
        nodo = self.arbol.extraer(15)
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.clave, 15)
        self.assertIsNone(self.arbol.buscar(15))

    def test_len(self):
        self.assertEqual(len(self.arbol), 7)
        self.arbol.eliminar(10)
        self.assertEqual(len(self.arbol), 6)

if __name__ == '__main__': # test para verificar que las rotaciones se hagan de forma correcta
    arbol = ArbolAVL()
    for clave, valor in [(20, 'a'), (10, 'b'), (30, 'c'), (5, 'd'), (15, 'e'), (18, 'f'), (14, 'g')]:
        arbol.agregar(clave, valor)
    arbol.imprimir_en_orden()
    unittest.main()