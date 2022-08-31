from Ejercicio2 import *


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, edad):
        super().__init__(titular, cantidad)
        self.edad = edad

    def getBonificacion(self):
        return self.bonificacionfinal

    def calcularBonificacion(self, porcentaje):
        self.bonificacionfinal = self.cantidad * (porcentaje/100)

    def esTitularValido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        else:
            return False

    def mostrar(self):
        super().mostrar()
        print(
            f'la cuenta tiene una bonificacion de {self.getBonificacion()} en base a la cantidad {self.getCantidad}')

    def retirar(self, cantidad):
        if self.esTitularValido() == True:
            while cantidad > self.cantidad or cantidad < 0:
                print(
                    "la cantidad que desea retirar es excesiva. De otro modo el numero ingresado es negativo.")
                cantidad = int(input("ingrese la cantidad de nuevo: "))
            else:
                self.cantidad = self.cantidad - cantidad
        else:
            print("Titular no valido.")


a = CuentaJoven("Pato", 10000, 18)

a.calcularBonificacion(20)
a.mostrar()
a.retirar(15000)
a.mostrar()
print(a.esTitularValido())
