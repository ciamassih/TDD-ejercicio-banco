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

    def test_transferencia_valor_2(self):
        cuenta1 = Cuenta(5)
        cuenta2 = Cuenta(0)
        valor = Transferencia()
        valor.transferir(cuenta1, cuenta2, 2)
        self.assertEqual(cuenta1.balance, 3)
        self.assertEqual(cuenta2.balance, 2)

    def test_transferencia_valor_2_de_cuenta_en_0(self):
        cuenta1 = Cuenta(0)
        cuenta2 = Cuenta(0)
        valor = Transferencia()
        with self.assertRaises(Error):
            valor.transferir(cuenta1, cuenta2, 2)

    def test_transferencia_valor_2_de_cuenta_en_10(self):
        cuenta1 = Cuenta(10)
        cuenta2 = Cuenta(0)
        valor = Transferencia()
        with self.assertRaises(Error):
            valor.transferir(cuenta1, cuenta2, 100)

    def test_parametros_incorrectos(self):
        with self.assertRaises(Error):
            cuenta = Cuenta("Hola")

    def test_sin_parametro_cuenta1(self):
        cuenta1 = Cuenta(5)
        cuenta2 = Cuenta(0)
        valor = Transferencia()
        with self.assertRaises(Error):
            valor.transferir("hola", cuenta2, 1)



