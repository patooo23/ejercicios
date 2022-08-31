
class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    # con property indicamos a Python que el método deberá ser tratado como un atributo. Un Atributo únicamente de lectura.
    @property
    def getNombre(self):
        return self.nombre

    @property
    def getDni(self):
        return self.dni

    @property
    def getEdad(self):
        return self.edad

    def validarTipoDatoEdad(self):
        if type(self.edad) == int:
            return True
        else:
            print("Ingrese un dato de tipo entero.")
            return False

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDni(self, dni):
        self.dni = dni

    def setEdad(self, edad):
        self.edad = edad

    def mostrar(self):
        print(
            f'la persona: {self.getNombre}  con el dni  {self.getDni} tiene {self.getEdad}')

    def mayorEdad(self):
        # para validar si es entero o no podriamos usar int() para convertirlo a entero o crear una funcion de validacion.
        if self.validarTipoDatoEdad() == True:
            if self.edad >= 18:
                print("es mayor de edad")
            else:
                print("es menor")
        else:
            while True:
                try:
                    self.edad = int(input())
                except ValueError:
                    print("debes ingresar un numero entero")
                    continue
                break


a = Persona("roberto", "43060864", 15)
b = Persona("cristian", "43050402", "21")
a.mostrar()
a.mayorEdad()
b.mostrar()
b.mayorEdad()
a.mostrar()
b.mostrar()
