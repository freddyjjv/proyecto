import Gestion_de_ventas
import Gestion_de_pagos
import gestion_de_envios

# Definición de la función menú estadísticas que permite al usuario seleccionar diferentes opciones para obtener estadísticas de ventas, pagos y envíos a través de diferentes submenús.
def menuestadisticas():
    while True:
        # Impresión del menú principal
        print("          -------- [ Menú ] --------          \n")
        print("     1. Ventas totales por día")
        print("     2. Ventas totales por mes")
        print("     3. Ventas totales por año")
        print("     4. Producto más vendido")
        print("     5. Cliente con más compras")
        print("     6. Pagos totales por día")
        print("     7. Pagos totales por mes")
        print("     8. Pagos totales por año")
        print("    9. Envíos totales por día")
        print("    10. Envíos totales por mes")
        print("    11. Envíos totales por año")
        print("    12. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        # Cálculo de las ventas totales por día
        if opcion == "1":
            ventaspordia=0
            fecha=input("Ingrese el día de la fecha con el siguiente formato: DD")
            for x in Gestion_de_ventas.lista_ventas:
                if x["fecha"][8:] == fecha:
                    ventaspordia += x["cantidad"]
            print(f"Las ventas por día son {ventaspordia}")
        # Cálculo de las ventas totales por mes
        elif opcion == "2":
            ventaspormes=0
            fecha=input("Ingrese el mes de la fecha con el siguiente formato: MM")
            for x in Gestion_de_ventas.lista_ventas:
                if x["fecha"][5:7] == fecha:
                    ventaspormes += x["cantidad"]
            print(f"Las ventas por mes son {ventaspormes}")
        # Cálculo de las ventas totales por año
        elif opcion == "3":
            ventasporano=0
            fecha=input("Ingrese el año de la fecha con el siguiente formato: YYYY")
            for x in Gestion_de_ventas.lista_ventas:
                if x["fecha"][0:4] == fecha:
                    ventasporano += x["cantidad"]
            print(f"Las ventas por año son {ventasporano}")
        # Cálculo del producto más vendido
        elif opcion == "4":
            producto_mas_vendido = ""
            cantidad_mas_vendida = 0
            for producto in Gestion_de_ventas.lista_ventas:
                ventas_producto = 0
                for venta in Gestion_de_ventas.lista_ventas:
                    if venta["producto"] == producto["producto"]:
                        ventas_producto += venta["cantidad"]
                if ventas_producto > cantidad_mas_vendida:
                    producto_mas_vendido = producto["producto"]
                    cantidad_mas_vendida = ventas_producto
            print(f"El producto más vendido es {producto_mas_vendido} con {cantidad_mas_vendida} ventas.")
        # Cálculo del cliente con más compras
        elif opcion == "5":
            cliente_mas_frecuente = ""
            frecuencia_cliente_mas_frecuente = 0
            for venta in Gestion_de_ventas.lista_ventas:
                cliente_venta = venta["cliente"]
                frecuencia_cliente = sum(1 for v in Gestion_de_ventas.lista_ventas if v["cliente"] == cliente_venta)
                if frecuencia_cliente > frecuencia_cliente_mas_frecuente:
                    cliente_mas_frecuente = cliente_venta
                    frecuencia_cliente_mas_frecuente = frecuencia_cliente

            print(f"El cliente más frecuente es {cliente_mas_frecuente} con {frecuencia_cliente_mas_frecuente} compras.")
        # Cálculo de los pagos totales por día
        elif opcion == "6":
            pagospordia=0
            fecha=input("Ingrese el día de la fecha con el siguiente formato: DD")
            for x in Gestion_de_pagos.pagos:
                if x["fecha"][8:] == fecha:
                    pagospordia += x["monto"]
            print(f"Los pagos por día son {pagospordia}")
        # Cálculo de los pagos totales por mes
        elif opcion == "7":
            pagospormes=0
            fecha=input("Ingrese el mes de la fecha con el siguiente formato: MM")
            for x in Gestion_de_pagos.pagos:
                if x["fecha"][5:7] == fecha:
                    pagospormes += x["monto"]
            print(f"Los pagos por mes son {pagospormes}")
        # Cálculo de los pagos totales por año
        elif opcion=="8":
            pagosporano=0
            fecha=input("Ingrese el mes de la fecha con el siguiente formato: MM")
            for x in Gestion_de_pagos.pagos:
                if x["fecha"][0:4] == fecha:
                    pagosporano += x["monto"]
            print(f"Los pagos por mes son {pagosporano}")
        # Cálculo de los envíos totales por día
        elif opcion == "9":
            enviospordia=0
            fecha=input("Ingrese el día de la fecha con el siguiente formato: DD")
            for x in gestion_de_envios.lista_envios:
                if x["fecha"][8:] == fecha:
                    enviospordia += 1
            print(f"Los envíos por día son {enviospordia}")
        # Cálculo de los envíos totales por mes
        elif opcion == "10":
            enviospormes=0
            fecha=input("Ingrese el mes de la fecha con el siguiente formato: MM")
            for x in gestion_de_envios.lista_envios:
                if x["fecha"][5:7] == fecha:
                    enviospormes += 1
            print(f"Los envíos por mes son {enviospormes}")
        # Cálculo de los envíos totales por año
        elif opcion == "11":
            enviosporano=0
            fecha=input("Ingrese el año de la fecha con el siguiente formato: YYYY")
            for x in gestion_de_envios.lista_envios:
                if x["fecha"][0:4] == fecha:
                    enviosporano += 1
            print(f"Los envíos por año son {enviosporano}")
        # Salida del menú
        elif opcion == "12":
            break
        else:
            # Impresión de un mensaje de error en caso de que el usuario seleccione una opción inválida
            print("Opción inválida. Por favor, ingrese un número de opción válido.")
        break