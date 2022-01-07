import unittest

from cuenta_banco import Cuenta

class TestCuentaBanco(unittest.TestCase):

    def test_balance_0(self):
        cuenta = Cuenta(0)
        self.assertEqual(cuenta.balance, 0)

    def test_balance_1(self):
        cuenta = Cuenta(1)
        self.assertEqual(cuenta.balance, 1)

    def test_ingreso_cuenta_0(self):
        cuenta = Cuenta(0)
        cuenta.ingreso(1)
        self.assertEqual(cuenta.balance, 1)



