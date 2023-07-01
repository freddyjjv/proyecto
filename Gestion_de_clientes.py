#Define la clase Clientes que representa un cliente y almacena información sobre el nombre, el tipo de cliente, la identificación, el correo, la dirección y el teléfono.
class Clientes:
    def __init__(self, nombre, tipo_cliente, identificacion, correo, direccion, telefono):
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.identificacion = identificacion
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def modificar(self, atributo, nuevo_valor):
        if hasattr(self, atributo):
            setattr(self, atributo, nuevo_valor)


clientes = []

#Define la función agregar_cliente que interactúa con el usuario para solicitar información sobre el cliente y crea una instancia de la clase Clientes para representar el cliente, y luego la agrega a la lista de clientes.
def agregar_cliente():
    while True:
        nombre = input('Ingrese el nombre del cliente que desea registrar: ')
        if not nombre.isalpha():
            print("Error: el nombre del cliente debe ser un string.")
        else:
            break
    while True:
        tipo_cliente = input('Ingrese si el cliente es Natural o Jurídico: ')
        if tipo_cliente not in ['Natural', 'Jurídico']:
            print("Error: Debe afirmar si el cliente es Natural o Jurídico.")
        else:
            break
    while True:
        identificacion = input('Ingrese la Cédula o el RIF, del cliente: ')
        if not identificacion.isnumeric():
            print("Error: La Cédula o el RIF, deben ser números.")
        else:
            break
    while True:
        correo = input('Ingrese el correo del cliente: ')
        if not correo.isalnum():
            print("Error: El correo del cliente debe ser un string alfanumérico.")
        else:
            break
    while True:
        direccion = input('Ingrese la dirección del cliente: ')
        if not direccion.isalnum():
            print("Error: La dirección del cliente debe ser un string alfanumérico.")
        else:
            break
    while True:
        telefono = input('Ingrese el teléfono del cliente: ')
        if not telefono.isnumeric():
            print("Error: el teléfono del cliente debe ser un número.")
        else:
            break

    clientes.append(Clientes(nombre, tipo_cliente, identificacion, correo, direccion, telefono))


def modificar_cliente():
    nombre = input("Ingrese el nombre del cliente que desea modificar: ")
    encontrado = False

    for clientmodi in clientes:
        if clientmodi.nombre == nombre:
            nuevo_nombre = input(f"Ingrese el nuevo nombre del cliente {clientmodi.nombre}: ")
            nuevo_tipo_cliente = input(f"Ingrese la nueva descripción del cliente {clientmodi.nombre}: ")
            nuevo_identificacion = input(f"Ingrese el nuevo identificador del cliente {clientmodi.nombre}: ")
            nuevo_correo = input(f"Ingrese el nuevo correo del cliente {clientmodi.nombre}: ")
            nuevo_direccion = input(f"Ingrese la nueva dirección del cliente {clientmodi.nombre}: ")
            nuevo_telefono = input(f"Ingrese el nuevo teléfono del cliente {clientmodi.nombre}: ")
            clientmodi.modificar("nombre", nuevo_nombre)
            clientmodi.modificar("tipo_cliente", nuevo_tipo_cliente)
            clientmodi.modificar("identificacion", nuevo_identificacion)
            clientmodi.modificar("correo", nuevo_correo)
            clientmodi.modificar("direccion", nuevo_direccion)
            clientmodi.modificar("telefono", nuevo_telefono)

            print("Cliente modificado con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un cliente con ese nombre.")

#Define la función eliminar_cliente que interactúa con el usuario para solicitar el nombre del cliente que desea eliminar y elimina la instancia del cliente correspondiente de la lista de clientes.
def eliminar_cliente():
    nombre = input("Ingrese el nombre del cliente que desea eliminar: ")
    encontrado = False

    for clientdelete in clientes:
        if clientdelete.nombre == nombre:
            clientes.remove(clientdelete)
            print("Cliente eliminado con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un cliente con ese nombre")

#Define la función buscar_cliente_por_atributo que permite al usuario buscar clientes registrados por atributo tipo de cliente, identificación o nombre y muestra los clientes correspondientes.
def buscar_cliente_por_atributo(lista_clientes, atributo, valor):
    resultados = []

    for cliente in lista_clientes:
        if getattr(cliente, atributo) == valor:
            resultados.append(cliente.__dict__)
    return resultados


def menuclientes():
    while True:
        print("          -------- [ Menú ] --------          \n")
        print("     1. Registrar nuevo cliente")
        print("     2. Modificar información del cliente")
        print("     3. Eliminar cliente")
        print("     4. Buscar cliente por tipo de cliente")
        print("     5. Buscar cliente por identificación")
        print("     6. Buscar cliente por nombre")
        print("     7. Buscar cliente por disponibilidad")
        print("     8. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            modificar_cliente()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            print(buscar_cliente_por_atributo(clientes, "tipo_cliente", input("Ingrese el valor a buscar: ")))
        elif opcion == "5":
            print(buscar_cliente_por_atributo(clientes, "identificacion", input("Ingrese el valor a buscar: ")))
        elif opcion == "6":
            print(buscar_cliente_por_atributo(clientes, "nombre", input("Ingrese el valor a buscar: ")))
        elif opcion == "7":
            print(buscar_cliente_por_atributo(clientes, "disponibilidad", input("Ingrese el valor a buscar: ")))
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    print("Gracias por utilizar el sistema de gestión de clientes.")