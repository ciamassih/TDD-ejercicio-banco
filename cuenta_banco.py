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

    def __init__(self, cuenta1, cuenta2):
        pass

    def transferir(self, cantidad_transferida):
        pass

class Error(Exception):
    pass