from Gestion_de_productos import *
from Gestion_de_clientes import *
from gestion_de_envios import *
from Gestion_de_ventas import *
import datetime

class Pago:
    def __init__(self, cliente, total, moneda, tipo_pago, fecha):
        self.cliente = cliente
        self.total = total
        self.moneda = moneda
        self.tipo_pago = tipo_pago
        self.fecha = fecha
# Método para mostrar los atributos del pago.
    def mostrar_atributos(self):
        print(f"""
        Cliente: {self.cliente}
        Total: {self.total}
        Moneda: {self.moneda}
        Tipo de Pago: {self.tipo_pago}
        Fecha: {self.fecha}
            """)

class GestionPagos(Pago):
    def __init__(self, cliente, total, moneda, tipo_pago, fecha):
        super().__init__(cliente, total, moneda, tipo_pago, fecha)
# Función para registrar un pago.
    def registrar_pago(pagos, total, cliente):
        moneda = input("Ingrese la moneda de pago: (1. Dólares 2. Bolívares)")
        while not moneda.isnumeric() or int(moneda) not in range(1, 3):
            moneda = input("Error! Ingrese un dato válido: ")
        if int(moneda) == 1:
            moneda = "Dólares"
        elif int(moneda) == 2:
            moneda = "Bolívares"
# Definimos los tipos de pago válidos
        tipos_pago = ["PdV", "PM", "Zelle", "Efectivo"]
        for i, tipo in enumerate(tipos_pago):
            print(f"{i+1}. {tipo}")
        opcion = input("¿Qué tipo de pago desea realizar? ")
 # Validamos que el usuario ingrese una opción válida.
        while not opcion.isnumeric() or not int(opcion) in range(1, len(tipos_pago)+1):
            print("Error")
            opcion = input("¿Qué tipo de pago desea realizar? ")
# Asignamos el tipo de pago seleccionado.
        if int(opcion) == 1:
            tipo_pago = "PdV"
        elif int(opcion) == 2:
            tipo_pago = "PM"
        elif int(opcion) == 3:
            tipo_pago = "Zelle"
        elif int(opcion) == 4:
            tipo_pago = "Efectivo"

        fecha = datetime.datetime.now().date()
# Creamos el objeto Pago y lo agregamos a la lista de pagos.
        pago = Pago(cliente, total, moneda, tipo_pago, fecha)
        pagos.append(pago)
        return pago

    def buscar_pago_cliente(pagos, cliente):
        if Clientes.tipo_cliente == "Natural":
            opcion = input("Ingrese su cédula: ")
            while not opcion.isnumeric() or (len(opcion)) < 7 and (len(opcion)) > 8:
                opcion = input("Error! Ingrese una cédula válida: ")
        elif cliente.tipo == "Jurídico":
            opcion = input("Ingrese su RIF: ")
            while not opcion.isnumeric() or (len(opcion)) != 10:
                opcion = input("Error! Ingrese un RIF válido: ")

        encontrado = 0
        for pago_cliente in pagos:
            if pago_cliente.cliente.cedula_rif == opcion:
                encontrado += 1
                # Mostramos los atributos del pago encontrado.
                print("\nDatos encontrados: ")
                print(f"""Cliente: {pago_cliente.cliente}
                        Total: {pago_cliente.total}
                        Moneda del Pago: {pago_cliente.moneda}
                        Tipo de Pago: {pago_cliente.tipo_pago}
                        Fecha: {pago_cliente.fecha}

                        """)

        if encontrado == 0:
            print("Este pago no existe dentro de la base de datos.")

    def buscar_pago_fecha(pagos):
        opcion = input("Coloque la fecha de hoy según este ej:(día/mes) ")
        while not opcion.isnumeric() and not "/" in opcion:
            opcion = input("Error! Ingrese un dato válido: ")

        encontrado = 0
        for pago_fecha in pagos:
            if pago_fecha.fecha == opcion:
                encontrado += 1
                print("\nDatos encontrados: ")
                print(f"""Cliente: {pago_fecha.cliente}
                        Total: {pago_fecha.total}
                        Moneda del Pago: {pago_fecha.moneda}
                        Tipo de Pago: {pago_fecha.tipo_pago}
                        Fecha: {pago_fecha.fecha}

                        """)

        if encontrado == 0:
            print("Este pago no existe dentro de la base de datos.")

    def buscar_pago_tipo(pagos):
        opcion = input("¿Qué tipo de pago realizó? (PdV, PM, Zelle, Efectivo) Escríbalo igual. ").capitalize()
        while not opcion.isalpha():
            opcion = input("Error! ¿Qué tipo de pago realizó? ").capitalize()

        encontrado = 0
        for pago_tipo in pagos:
            if pago_tipo.tipo_pago == opcion:
                encontrado += 1
                print("\nDatos encontrados: ")
                print(f"""Cliente: {pago_tipo.cliente}
                        Total: {pago_tipo.total}
                        Moneda del Pago: {pago_tipo.moneda}
                        Tipo de Pago: {pago_tipo.tipo_pago}
                        Fecha: {pago_tipo.fecha}

                        """)

        if encontrado == 0:
            print("Este pago no existe dentro de la base de datos.")
def menupagos():
    pagos = []
    while True:
        print("          -------- [ Menú de Pagos ] --------          \n")
        print("     1. Registrar pago")
        print("     2. Buscar pago por cliente")
        print("     3. Buscar pago por fecha")
        print("     4. Buscar pago por tipo de pago")
        print("     5. Buscar pago por moneda de pago")
        print("     6. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        if opcion == "1":
            total = input("Ingrese el total a pagar: ")
            while not total.isnumeric():
                total = input("Error! Ingrese un dato válido: ")
            total = float(total)

            cliente = Gestion_de_clientes.buscar_cliente_por_atributo(clientes, "nombre", input("Ingrese el cliente a buscar: "))
            pago = GestionPagos.registrar_pago(pagos, total, cliente)
            print("\nPago registrado exitosamente.\n")
            pago.mostrar_atributos()
        elif opcion == "2":
            cliente = Gestion_de_clientes.buscar_cliente_por_atributo(clientes, "nombre", input("Ingrese el cliente a buscar: "))
            GestionPagos.buscar_pago_cliente(pagos, cliente)
        elif opcion == "3":
            GestionPagos.buscar_pago_fecha(pagos)
        elif opcion == "4":
            GestionPagos.buscar_pago_tipo(pagos)
        elif opcion == "5":
            moneda = input("Ingrese la moneda de pago: (1. Dólares 2. Bolívares)")
            while not moneda.isnumeric() or int(moneda) not in range(1, 3):
                moneda = input("Error! Ingrese un dato válido: ")
            if int(moneda) == 1:
                moneda = "Dólares"
            elif int(moneda) == 2:
                moneda = "Bolívares"

            encontrados = []
            for pago_moneda in pagos:
                if pago_moneda.moneda == moneda:
                    encontrados.append(pago_moneda)
            if len(encontrados) > 0:
                print(f"\n{len(encontrados)} pago(s) encontrado(s) en {moneda}:")
                for pago in encontrados:
                    pago.mostrar_atributos()
            else:
                print(f"No se encontraron pagos en {moneda}.")
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    print("\nGracias por utilizar el sistema de gestión de pagos.")