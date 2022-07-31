#Realizar un programa en el cual se declaren
#dos valores enteros por teclado utilizando el
#método __init__. Calcular después la suma, resta,
#multiplicación y división. Utilizar un método 
#para cada una e imprimir los resultados obtenidos.
#Llamar a la clase Calculadora.


from __future__ import division


class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.suma = 0
        self.resta = 0
        self.multiplicacion = 0
        self.division = 0.0

        print("Numeros guardados...")


    def sumar(self):
        self.suma = self.num1 + self.num2
        print("Suma asignada...")

    def restar(self):
        self.resta = self.num1 - self.num2
        print("Resta asignada...")

    def multiplicar(self): 
        self.multiplicacion = self.num1 * self.num2
        print("Multiplicacion asignada...")

    def dividir(self):
        self.division = self.num1 / self.num2
        print("Division asignada...")


    def __str__(self):
        resultado = f"""
        ========================================================
        ~    Numero 1: {str(self.num1)}                         
        ~    Numero 2: {str(self.num2)}                         
        ~    Suma: {str(self.suma)}                             
        ~    Resta: {str(self.resta)}                           
        ~    Multiplicacion: {str(self.multiplicacion)}         
        ~    Division: {str(self.division)}                     
        ========================================================
        """
        return resultado


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

calculadora = Calculadora(num1,num2)

calculadora.sumar()
calculadora.restar()
calculadora.multiplicar()
calculadora.dividir()

print(calculadora)

