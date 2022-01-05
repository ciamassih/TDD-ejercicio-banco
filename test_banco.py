import unittest

from cuenta_banco import Cuenta

class TestCuentaBanco(unittest.TestCase):
    cuenta = Cuenta()

    def test_cuenta_vacía(self):
        estado = self.cuenta.estado()
        self.assertEqual(estado, 0)

    def test_cuenta_de_pobre(self):
        suma = Cuenta.sumar(0, 5)
        self.assertEqual(suma, 5)

    def test_cuenta_no_tan_pobre(self):
        suma = Cuenta.sumar(7, 5)
        self.assertEqual(suma, 12)

