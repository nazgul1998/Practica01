#Desarrollar un programa que conste de una clase padre Cuenta 
#y dos subclases PlazoFijo y CajaAhorro. Definir los atributos
#titular y cantidad y un método para imprimir los datos en la 
#clase Cuenta. La clase CajaAhorro tendrá un método para heredar
#los datos y uno para mostrar la información.

#La clase PlazoFijo tendrá dos atributos propios, plazo e 
#interés. Tendrá un método para obtener el importe del interés
#(cantidad*interés/100) y otro método para mostrar la 
#información, datos del titular plazo, interés y total de 
#interés.

#Crear al menos un objeto de cada subclase.


class Cuenta:
    def __init__(self, titular="",cantidad=0.0):
        self.titular =titular
        self.cantidad = cantidad
        

class CajaAhorro(Cuenta):
    def __init__(self, titular="", cantidad=0):
        super().__init__(titular, cantidad)

    def __str__(self) -> str:
        return (f"""
            =============================
            Cuenta de caja de ahorros...
            =============================
            Titular: {self.titular}
            Cantidad: {self.cantidad}
            -----------------------------
        """)


class PlazoFijo(Cuenta):
    def __init__(self, titular="", cantidad=0, plazo="Tradicional", interes=0.00):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def obtener_importe_interes(self):
        importe = 0.0

        importe = self.cantidad * self.interes / 100
        return importe

    def __str__(self) -> str:
        return (f"""
            =============================
            Cuenta de plazo fijo...
            =============================
            Titular: {self.titular}
            Cantidad: {str(self.cantidad)}
            Plazo: {self.plazo}
            Interes: {str(self.interes)}%
            Importe del interes: {str(self.obtener_importe_interes())}
            -----------------------------
        """)





#creando objetos de subclases
#objeto 1 cuenta de caja de ahrros de miguel con una cantidad de 1500.00
cuenta1 = CajaAhorro("Miguel",1500.00)
print(cuenta1)


#objeto 2 cuenta de plazo fijo de carlos con una cantidad de 500.00
cuenta2 = PlazoFijo("Carlos",500.00,"Precancelable",1)
print(cuenta2)

#objeto 3 cuenta de plazo fijo de john con una cantidad de 500.00 y plazo por defecto
cuenta2 = PlazoFijo(titular="Carlos",cantidad=500.00,interes=1)
print(cuenta2)
    