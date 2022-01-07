class Cuenta:

    def __init__(self, balance):
        if type(balance) != int:
            raise Error("Parámetro incorrecto")
        self.balance = balance

    def ingreso(self, cantidad):
        self.balance += cantidad

    def retiro(self, cantidad):
        if (self.balance - cantidad) < 0:
            raise Error("Cantidad insuficiente")
        self.balance -= cantidad

class Transferencia:

    def transferir(self, cuenta1, cuenta2, cantidad_transferida):
        if (cuenta1.balance - cantidad_transferida) <= 0:
            raise Error("No puede realizarse la transferencia.")
        cuenta1.balance -= cantidad_transferida
        cuenta2.balance += cantidad_transferida

class Error(Exception):
    pass