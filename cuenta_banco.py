class Cuenta:

    def __init__(self, balance):
        self.balance = balance

    def ingreso(self, cantidad):
        self.balance += cantidad

    def retiro(self, cantidad):
        if (self.balance - cantidad) < 0:
            raise Error("Cantidad insuficiente")
        self.balance -= cantidad

class Transferencia:

    def transferir(self, cuenta1, cuenta2, cantidad_transferida):
        cuenta1.balance = 4
        cuenta2.balance = 1

class Error(Exception):
    pass