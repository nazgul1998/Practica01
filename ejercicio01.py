#Realizar un programa que conste de una clase llamada Alumno 
#que tenga como atributos el nombre y la nota del alumno. Definir 
#los métodos para inicializar sus atributos, imprimirlos y mostrar
#un mensaje con el resultado de la nota y si ha aprobado o no.´
#>=11 aprobado 


class Alumno:
    nombre = ""
    nota = 0.0


    def __str__(self) -> str:
        estado = "desaprobado"
        if self.nota >= 11:
            estado = "aprobado"
        resultado = self.nombre + " - " + str(self.nota) +  " => " + estado 
        return resultado



    def __init__(self, nombre=None, nota=None):
        self.nombre = nombre
        self.nota = nota

        print(self.nombre + " fue agregado.")

alumnos = []
opcion = 0

while opcion != 3:
    print("""
    ====================================
                  MENU
    ====================================
    1) Agregar alumno. 
    2) Mostrar alumnos.
    3) Salir.

    -------------------------------------
    Ingrese una opcion: """)
    opcion = int(input())


    if opcion == 1:
        nombre = input("Ingrese el nombre del alumno: ")
        nota = float(input("Ingrese la nota del alumno: "))
        new_alumno = Alumno(nombre,nota)
        alumnos.append(new_alumno)

    elif opcion == 2:
        for item in alumnos:
            print(item)

    elif opcion != 1 and opcion != 2 and opcion != 3 :
        print("Opcion invalida...")





