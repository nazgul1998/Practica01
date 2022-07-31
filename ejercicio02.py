#Realizar un programa que tenga una clase 
#Persona con las siguientes características. 
#La clase tendrá como atributos el nombre y la 
#edad de una persona. Implementar los métodos 
#necesarios para inicializar los atributos, mostrar
#los datos e indicar si la persona es mayor de edad 
#o no.


class Persona:
    nombre = ""
    edad = 0.0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    def __str__(self):
        mayor = False
        if self.edad >= 18:
            mayor = True

        resultado = ((self.nombre + " es mayor de edad.") if mayor else (self.nombre + " es menor de edad." ))
        return resultado


personas = []
opcion = 0

while opcion != 3:
    print("""
    ====================================
                  MENU
    ====================================
    1) Agregar Persona. 
    2) Mostrar Personas.
    3) Salir.

    -------------------------------------
    Ingrese una opcion: """)
    opcion = int(input())


    if opcion == 1:
        nombre = input("Ingrese el nombre de la persona: ")
        edad = float(input("Ingrese su edad: "))
        new_alumno = Persona(nombre,edad)
        personas.append(new_alumno)

    elif opcion == 2:
        for item in personas:
            print(item)

    elif opcion != 1 and opcion != 2 and opcion != 3 :
        print("Opcion invalida...")










