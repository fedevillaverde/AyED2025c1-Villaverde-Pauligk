import unittest
from modules.Temperaturas_DB import Temperaturas

class TestTemperaturas(unittest.TestCase):
    def setUp(self):
        self.temp = Temperaturas()
        # Datos de prueba
        self.registros = [
            ("01/01/2023", 25.0),
            ("02/01/2023", 26.5),
            ("03/01/2023", 24.0),
            ("04/01/2023", 27.8),
            ("05/01/2023", 22.3),
        ]
        for fecha, valor in self.registros:
            self.temp.guardar_temperatura(valor, fecha)

    def test_guardar_y_devolver_temperatura(self):
        self.assertEqual(self.temp.devolver_temperatura("01/01/2023"), 25.0)
        self.assertEqual(self.temp.devolver_temperatura("05/01/2023"), 22.3)

    def test_max_temp_rango(self):
        self.assertEqual(self.temp.max_temp_rango("01/01/2023", "05/01/2023"), 27.8)

    def test_min_temp_rango(self):
        self.assertEqual(self.temp.min_temp_rango("01/01/2023", "05/01/2023"), 22.3)

    def test_temp_extremos_rango(self):
        extremos = self.temp.temp_extremos_rango("01/01/2023", "05/01/2023")
        self.assertEqual(extremos, (22.3, 27.8))

    def test_borrar_temperatura(self):
        self.temp.borrar_temperatura("04/01/2023")
        with self.assertRaises(AttributeError):  # porque buscar devuelve None y se accede a .cargaUtil
            self.temp.devolver_temperatura("04/01/2023")

    def test_devolver_temperaturas_en_rango(self):
        lista = self.temp.devolver_temperaturas("02/01/2023", "04/01/2023")
        self.assertEqual(len(lista), 3)
        self.assertIn("03/01/2023: 24.0 ºC", lista)

    def test_cantidad_muestras(self):
        self.assertEqual(self.temp.cantidad_muestras(), 5)
        self.temp.borrar_temperatura("01/01/2023")
        self.assertEqual(self.temp.cantidad_muestras(), 4)

if __name__ == '__main__':
    unittest.main()
