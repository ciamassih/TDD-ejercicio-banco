import unittest

from cuenta_banco import Cuenta, Error, Transferencia

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

    def test_retiro_cuenta_5_retiro_3(self):
        cuenta = Cuenta(5)
        cuenta.retiro(3)
        self.assertEqual(cuenta.balance, 2)

    def test_retiro_cuenta_0_retiro_5(self):
        cuenta = Cuenta(0)
        with self.assertRaises(Error):
            cuenta.retiro(5)

    def test_transferencia_valor_1(self):
        cuenta1 = Cuenta(5)
        cuenta2 = Cuenta(0)
        valor = Transferencia()
        valor.transferir(cuenta1, cuenta2, 1)
        self.assertEqual(cuenta1.balance, 4)
        self.assertEqual(cuenta2.balance, 1)


