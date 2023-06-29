class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

cuenta = CuentaBancaria()
print("Saldo:",cuenta.saldo)  # Salida: 0
cuenta.saldo = 1000
print("Saldo:",cuenta.saldo)