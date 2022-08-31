
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def getTitular(self):
        return self.titular

    @property
    def getCantidad(self):
        return self.cantidad

    def mostrar(self):
        print(
            f'Esta cuenta es de {self.getTitular} y tiene un saldo de ${self.getCantidad}')

    def ingresar(self, cantidad):
        self.cantidad = self.cantidad + cantidad

    def retirar(self, cantidad):
        while cantidad > self.cantidad or cantidad < 0:
            print(
                "la cantidad que desea retirar es excesiva. De otro modo el numero ingresado es negativo.")
            cantidad = int(input("ingrese la cantidad de nuevo: "))
        else:
            self.cantidad = self.cantidad - cantidad
