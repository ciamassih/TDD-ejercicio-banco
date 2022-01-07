class Cuenta:

    def __init__(self, balance):
        self.balance = balance

    def ingreso(self, cantidad):
        self.balance += cantidad

    def retiro(self, cantidad):
        pass