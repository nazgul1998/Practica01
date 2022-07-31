#Desarrollar un programa que cargue los datos de un triángulo. 
#Implementar una clase con los métodos para inicializar los 
#atributos, imprimir el valor del lado con un tamaño mayor y
#el tipo de triángulo que es (equilátero, isósceles o escaleno).

#equilatero => lados iguales
#isosceles => cuando dos de sus lados son iguales
#escaleno => 3 lados diferentes



class Triangulo:
    lado_a = 0.0
    lado_b = 0.0
    lado_c = 0.0 

    tipo = ""

    def tipo_de_triangulo(self):
        if(self.lado_a == self.lado_b and self.lado_b== self.lado_c):
            self.tipo = "equilatero"
        elif(self.lado_a == self.lado_b or self.lado_b == self.lado_c or self.lado_a == self.lado_c):
            self.tipo = "isosceles"
        elif(self.lado_a != self.lado_b and self.lado_a!= self.lado_c):
            self.tipo = "escaleno"

        print("Estado seteado...")

    def __init__(self, a, b, c) :
        self.lado_a = a
        self.lado_b = b
        self.lado_c = c 
        print("Triangulo guardado ...")


    def __str__(self):
        mayor = self.lado_a
        if(mayor <= self.lado_b):
            mayor = self.lado_b
            if(mayor <= self.lado_c):
                mayor = self.lado_c

        resultado = "Lado mayor: " + str(mayor) + " - Tipo: " + self.tipo
        return resultado



triangulos = []
opcion = 0

while opcion != 3:
    print("""
    ====================================
                  MENU
    ====================================
    1) Agregar triangulo. 
    2) Mostrar triangulos.
    3) Salir.

    -------------------------------------
    Ingrese una opcion: """)
    opcion = int(input())


    if opcion == 1:
        a = float(input("Ingrese el lado a: "))
        b = float(input("Ingrese el lado b: "))
        c = float(input("Ingrese el lado c: "))
        new_triangulo = Triangulo(a,b,c)
        new_triangulo.tipo_de_triangulo()
        triangulos.append(new_triangulo)


    elif opcion == 2:
        for item in triangulos:
            print(item)

    elif opcion != 1 and opcion != 2 and opcion != 3 :
        print("Opcion invalida...")



