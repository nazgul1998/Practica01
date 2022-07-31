#Realizar una clase que administre una agenda. 
#Se debe almacenar para cada contacto el nombre, 
#el teléfono y el email. Además deberá mostrar 
#un menú con las siguientes opciones
# *Añadir contacto
# *Lista de contactos
# *Buscar contacto
# *Editar contacto
# *Cerrar agenda


class Agenda:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre 
        self.telefono = telefono
        self.email = email
        print("Contacto guardado... ")

    def __str__(self):
        resultado = f"""
            ~=========================
            ~ Nombre: {self.nombre}
            ~ Telefono: {self.telefono}
            ~ Email: {self.email}
            ~=========================
        """
        return resultado


contactos = []
opcion = 0



def buscar_contacto(texto):
    resultados = []
    for item in contactos:
        if texto in item.nombre:
            resultados.append(item)

    return resultados



while opcion != 5:
    print("""
    ====================================
                  MENU
    ====================================
    1) Agregar contacto. 
    2) Mostrar contactos.
    3) Buscar contacto.
    4) Editar contacto
    5) Salir.

    -------------------------------------
    Ingrese una opcion: """)
    opcion = int(input())


    if opcion == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        contacto = Agenda(nombre=nombre,telefono=telefono,email=email)
        contactos.append(contacto)
        print("Contacto agregado a la agenda...")


    elif opcion == 2:
        for item in contactos:
            resultado = item
            print(resultado) 

    elif opcion == 3 :
        busqueda = input("Buscar: ")
        resultados = buscar_contacto(busqueda)
        if resultados == []:
            print("Aun no tiene contactos guardados...")
        else:
            for item in resultados: 
                print(f"{item} - id: {contactos.index(item)}")

    elif opcion == 4 : 
        busqueda = input("Buscar: ")
        resultados = buscar_contacto(busqueda)
        if resultados == []:
            print("Aun no tiene contactos guardados...")
        else:
            for item in resultados: 
                print(f"{item} - id: {contactos.index(item)}")

        id = int(input("Ingrese el id del contacto que desea borrar: "))
        contacto = ""
        try:
            contacto = contactos[id]

            contacto.nombre = input("Ingrese el nuevo nombre: ")
            contacto.telefono = input("Ingrese el nuevo telefono: ")
            contacto.email = input("Ingrese el nuevo correo: ")
            
            print("Actualizado con exito...")

        except:
            print("El contacto no existe")

    