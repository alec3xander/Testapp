import unittest
from simple_test import main

class TestSimpleApp(unittest.TestCase):
    def test_main(self):
        # Aquí podrías agregar pruebas relacionadas con tu aplicación
        # Por ejemplo, verificar que se crea la ventana principal
        self.assertTrue(True)  # Esta es solo una prueba de ejemplo

if __name__ == "__main__":
    unittest.main()
