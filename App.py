import Gestion_de_productos
import Gestion_de_clientes
import Gestion_de_ventas
import gestion_de_envios
import Gestion_de_pagos
import estadisticas

clientes_abiertos = False
productos_abiertos = False
ventas_abiertas = False
#inicializan las variables de estado para saber si se han abierto los módulos de gestión correspondientes.

def menuprincipal():
    global clientes_abiertos, productos_abiertos, ventas_abiertas
    #comienza un bucle infinito para que el menú se muestre constantemente hasta que el usuario seleccione la opción "7" para salir.
    while True:
        print("          -------- [ Menú ] --------          \n")
        print("     1. Ver Gestión de productos")
        print("     2. Ver Gestión de clientes")
        print("     3. Ver Gestión de ventas")
        print("     4. Ver gestión de envíos")
        print("     5. Ver gestión de pagos")
        print("     6. Ver estadísticas")
        print("     7. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        if opcion == "1":
            Gestion_de_productos.menuproductos()
            productos_abiertos = True
        elif opcion == "2":
            Gestion_de_clientes.menuclientes()
            clientes_abiertos = True
        elif opcion == "3":
            if clientes_abiertos and productos_abiertos:
                Gestion_de_ventas.menu_ventas()
                ventas_abiertas = True
            else:
                print("Error: primero debe abrir los módulos de gestión de clientes y productos.")
        elif opcion == "4":
            if ventas_abiertas:
                gestion_de_envios.menuenvios()
            else:
                print("Error: primero debe abrir el módulo de gestión de ventas.")
        elif opcion== "5":
            Gestion_de_pagos.menupagos()
        elif opcion== "6":
            estadisticas.menuestadisticas()
        elif opcion== "7":
        #codigo para añadir todo lo de la lista al archivo txt
            with open("C:/Users/Usuario/Desktop/proyecto python/Gestion_de_clientes.txt","a") as a:
                for customer1 in Gestion_de_clientes.clientes:
                    nombre = customer1.nombre
                    tipo_cliente = customer1.tipo_cliente
                    identificacion = customer1.identificacion
                    correo = customer1.correo
                    direccion = customer1.direccion
                    telefono = customer1.telefono
                    a.write(f"{nombre}///{tipo_cliente}///{identificacion}///{correo}///{direccion}///{telefono}///\n")

            with open("C:/Users/Usuario/Desktop/proyecto python/Gestion_de_productos.txt","a") as a:
                for product1 in Gestion_de_productos.productos:
                    name = product1.name
                    description = product1.description
                    price = product1.price
                    category = product1.category
                    quantity = product1.quantity
                    a.write(f"{name}///{description}///{price}///{category}///{quantity}///\n")

            with open("C:/Users/Usuario/Desktop/proyecto python/Gestion_de_ventas.txt","a") as a:
                for sale1 in Gestion_de_ventas.lista_ventas:
                    fecha = sale1.fecha
                    cliente= sale1.cliente
                    metodo_pago = sale1.metodo_pago
                    moneda = sale1.moneda
                    codigo = sale1.codigo
                    venta = sale1.venta
                    a.write(f"{fecha}///{cliente}///{metodo_pago}///{moneda}///{codigo}///{venta}///\n")
                
            with open("C:/Users/Usuario/Desktop/proyecto python/Gestion_de_pagos.txt","a") as a:
                for payment1 in Gestion_de_pagos.pagos:
                    cliente=payment1.cliente
                    total=payment1.total
                    moneda=payment1.moneda
                    tipo_pago=payment1.tipo_pago
                    fecha=payment1.fecha
                    a.write(f"{cliente}///{total}///{moneda}///{tipo_pago}///{fecha}///\n")
                
            with open("C:/Users/Usuario/Desktop/proyecto python/gestion_de_envios.txt","a") as a:
                for shipment1 in gestion_de_envios.envios:
                    orden_compra=shipment1.orden_compra
                    servicio_envio =shipment1.servicio_envio 
                    costo=shipment1.costo 
                    fecha=shipment1.fecha
                    a.write(f"{orden_compra}///{servicio_envio}///{costo}///{fecha}///\n")
            break

menuprincipal()

#A veces da error con el API, pero de resto está todo bueno