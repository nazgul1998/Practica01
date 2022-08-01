#En un banco tienen clientes que pueden hacer depósitos 
#y extracciones de dinero. El banco requiere también al
#final del día calcular la cantidad de dinero que se ha depositado.

#Se deberán crear dos clases, la clase cliente y la clase banco. 
#La clase cliente tendrá los atributos nombre y cantidad y los
# métodos __init__, depositar, extraer, mostrar_total.

#La clase banco tendrá como atributos 3 objetos de la clase
#cliente y los métodos __init__, operar y deposito_total.


class Cliente:
    total_retirado = 0.0
    total_depositado = 0.0

    def __init__(self, nombre="",cantidad=0.0):
        self.nombre = nombre
        self.cantidad = cantidad
 

    def depositar(self, monto:float):
        try:
            self.cantidad += monto
            self.total_depositado += monto 
            print("Deposito realizado con exito... ")
        except ValueError:
            print("Error durante la transaccion...")
            

    def extraer(self, monto:float):
        try:
            if self.cantidad >= monto:
                self.cantidad -= monto
                self.total_retirado += monto
                print("Retiro realizado con exito...")
            else:
                print("Saldo insuficiente...")
        except:
            print("Error durante la transaccion...")


    def mostrar_total(self):
        try:
            print(f"""
                Nombre: ${self.nombre}
                Monto total: ${str(self.cantidad)}
            """)
        except:
            print("Error al mostrar datos de cliente...")



class Banco:
    def __init__(self, cliente1 = Cliente(), cliente2=Cliente(),
    cliente3=Cliente()) :
        self.cliente1 = cliente1
        self.cliente2 = cliente2
        self.cliente3 = cliente3

    def operar(self):
        #operaciones cliente 1... 
        self.cliente1.depositar(500.00)
        self.cliente1.mostrar_total()
        self.cliente1.extraer(200.00)
        self.cliente1.mostrar_total()
        self.cliente1.depositar(100.00)
        self.cliente1.mostrar_total()


        #operaciones cliente 2... 
        self.cliente2.depositar(200.00)
        self.cliente2.mostrar_total()
        self.cliente2.depositar(100.00)
        self.cliente2.mostrar_total()


        #operaciones cliente 3... 
        self.cliente3.extraer(200.00)
        self.cliente3.mostrar_total()
        self.cliente3.depositar(500.00)
        self.cliente3.mostrar_total()

    def deposito_total(self):
        print(f"""
            ==================================
            ~ Cliente 1...
            ==================================
            *Total depositado: ${str(self.cliente1.total_depositado)}
            *Total retirado: ${str(self.cliente1.total_retirado)}


            ==================================
            ~ Cliente 2...
            ==================================
            *Total depositado: ${str(self.cliente2.total_depositado)}
            *Total retirado: ${str(self.cliente2.total_retirado)}


            ==================================
            ~ Cliente 3...
            ==================================
            *Total depositado: ${str(self.cliente3.total_depositado)}
            *Total retirado: ${str(self.cliente3.total_retirado)}
        """)


cliente1 = Cliente("Miguel",1200.00)
cliente2 = Cliente(nombre="Rodrigo")
cliente3 = Cliente("Lilith",200.00)


banco = Banco(cliente1,cliente2, cliente3)

banco.operar()
banco.deposito_total()