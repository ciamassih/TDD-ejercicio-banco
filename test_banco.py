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

    def test_mayor_ingreso_cuenta_0(self):
        cuenta = Cuenta(0)
        cuenta.ingreso(5)
        self.assertEqual(cuenta.balance, 5)

    def test_retiro_cuenta_5_retiro_5(self):
        cuenta = Cuenta(5)
        cuenta.retiro(5)
        self.assertEqual(cuenta.balance, 0)

    def test_retiro_2(self):
        cuenta = Cuenta(5)
        cuenta.retiro(3)
        self.assertEqual(cuenta.balance, 2)



