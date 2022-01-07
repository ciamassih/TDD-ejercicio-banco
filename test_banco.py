import unittest

from cuenta_banco import Cuenta

class TestCuentaBanco(unittest.TestCase):

    def test_balance_0(self):
        cuenta = Cuenta(0)
        self.assertEqual(cuenta.balance, 0)



