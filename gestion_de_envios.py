import datetime
import Gestion_de_ventas

envios=[]

class Envio:
    def __init__(self, orden_compra, servicio_envio, costo, fecha, motorizado=None):
        self.orden_compra = orden_compra
        self.servicio_envio = servicio_envio
        self.costo = costo
        self.fecha = fecha
        self.motorizado = motorizado
      
    # Método para agregar los datos del motorizado en caso de que el servicio sea Delivery
    def agregar_motorizado(self, nombre, placa):
        self.motorizado = {'nombre': nombre, 'placa': placa}

# Función para validar el formato de la fecha ingresada
def validar_fecha(date_text):
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False

# Función para agregar un envío a la lista de envíos
def agregar_envio():
    # Se solicita la orden de compra al usuario y se valida que sea un string
    while True:
        orden_compra= input('Ingrese la orden de compra: ')
        if not orden_compra.isalpha():
            print("Error: La orden de compra debe ser un string.")
        else:
            break
    # Se solicita el servicio de envío al usuario y se valida que sea MRW, Zoom o Delivery
    while True:
        servicio_envio = input('Ingrese si el servicio de envío es MRW, Zoom o Delivery: ')
        if not servicio_envio=="MRW" or servicio_envio=="Zoom" or servicio_envio== "Delivery":
            print("Error: La descripción del producto debe ser MRW, Zoom o Delivery.")
        # Si el servicio es Delivery, se solicitan los datos del motorizado
        if servicio_envio=="Delivery":
            nombre_motorizado=''
            while True:
                nombre_motorizado=input("Ingrese el nombre del motorizado: ")
                if not nombre_motorizado.isalpha():
                    print("Error: El nombre del motorizado debe ser un string")
                else:
                    break
            placa_motorizado=''
            while True:
                placa_motorizado=input("Ingrese la placa del motorizado: ")
                if not placa_motorizado.isnumeric():
                    print("Error: La placa del motorizado debe ser un número")
                else:
                    break
        else:
            break
    # Se solicita el costo del servicio al usuario y se valida que sea un número
    while True:
        costo=input("Ingrese el costo del servicio: ")
        if not costo.isnumeric():
            print("Error: El costo debe ser un número: ")
        else:  
            break
    # Se solicita la fecha del envío al usuario y se valida que tenga el formato correcto
    while True:
        fecha=input('Ingrese la fecha del envio con el formato AAAA-MM-DD: ')
        if validar_fecha(fecha):
            break
        else:
            print('Error: El formato de fecha debe ser AAAA-MM-DD.')
      
    # Se crea un objeto Envio con los datos ingresados por el usuario y se agrega a la lista de envíos
    envio=Envio(orden_compra,servicio_envio,costo,fecha)
    if servicio_envio=="Delivery":
        envio.agregar_motorizado(nombre_motorizado,placa_motorizado)
    envios.append(envio)

# Función para buscar envíos por un atributo y un valor
def buscar_envio_por_atributo(envios, atributo, valor):
    resultados = []
    for envio in envios:
        if getattr(envio, atributo) == valor:
            resultados.append({
                'orden_compra': envio.orden_compra,
                'servicio_envio': envio.servicio_envio,
                'costo': envio.costo,
                'fecha': envio.fecha
            })
    if resultados:
        return resultados
    else:
        return f"No se encontraron ventas con {atributo} = {valor}"

# Función para mostrar el menú de opciones
def menuenvios():
    while True:
        print("          -------- [ Menú ] --------          \n")
        print("     1. Registrar envio")
        print("     2. Buscar envio por fecha")
        print("     3. Buscar envio por cliente")
        print("     4. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        if opcion == "1":
            # Se llama a la función agregar_envio para registrar un nuevo envío
            agregar_envio()
        elif opcion == "2":
            # Se llama a la función buscar_envio_por_atributo para buscar envíos por fecha
            print(buscar_envio_por_atributo(envios,"fecha",input("ingrese la fecha")))
        elif opcion == "3":
            # Se solicita el nombre del cliente y se llama a la función buscar_venta_por_cliente del módulo Gestion_de_ventas
            nombre=input("Ingrese el nombre del cliente: ")
            ventas:Gestion_de_ventas.EncabezadoVenta
            ventas=Gestion_de_ventas.buscar_venta_por_cliente(Gestion_de_ventas.lista_ventas,nombre)
            # Para cada venta encontrada, se busca el envío correspondiente por orden de compra
            for i in ventas:
                print(buscar_envio_por_atributo(envios,"orden_compra",i.codigo))
        elif opcion == "4":
            # Se sale del menú si el usuario selecciona la opción 4
            break
        else:
            # Se muestra un mensaje de error si el usuario ingresa una opción inválida
            print("Opción inválida. Por favor, seleccione una opción válida.")
    # Se muestra un mensaje de despedida al usuario al salir del menú
    print("Gracias por utilizar el sistema de gestión de envíos.")