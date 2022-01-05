import unittest

from cuenta_banco import Cuenta

class TestCuentaBanco(unittest.TestCase):
    cuenta = Cuenta()

    def test_cuenta_vacía(self):
        estado = self.cuenta.estado()
        self.assertEqual(estado, 0)
