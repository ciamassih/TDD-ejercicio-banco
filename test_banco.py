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

    def test_cuenta_con_estado_guardado(self):
        estado = 5
        suma = Cuenta.sumar((estado), 5)
        self.assertEqual(suma, 10)

    def test_cuenta_con_estado_y_transferencia(self):
        estado = 5
        transferencia = 3
        resta = Cuenta.restar((estado), (transferencia))
        self.assertEqual(resta, 2)

    def test_cuenta_con_intereses(self):
        estado = 5
        tasa = 0.3
        intereses = Cuenta.intereses((estado), (tasa))
        self.assertEqual(intereses, 1.5)

    def test_cuenta_con_crecimiento_por_intereses(self):
        estado = 5
        intereses = 1.5
        crecimiento = Cuenta.crecimiento((estado), (intereses))
        self.assertEqual(crecimiento, 6.5)



