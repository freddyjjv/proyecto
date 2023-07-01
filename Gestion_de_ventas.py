import datetime
import Gestion_de_clientes
import Gestion_de_productos
#Importa los módulos datetime, Gestion_de_clientes y Gestion_de_productos.
lista_ventas=[]
#Define una lista vacía llamada lista_ventas para almacenar las ventas registradas.
def validar_fecha(date_text):
  try:
    datetime.date.fromisoformat(date_text)
    return True
  except ValueError:
    return False
  
#Funcion para validar la fecha de una mejor manera
    
class EncabezadoVenta:
  def __init__(self,cliente:Gestion_de_clientes.Clientes,metodo_pago,metodo_envio,fecha,moneda,codigo):
    self.cliente=cliente
    self.metodo_pago=metodo_pago
    self.metodo_envio=metodo_envio
    self.fecha=fecha
    self.codigo=codigo
    self.subtotal=0
    self.moneda=moneda
    self.IVA=0
    self.IGTF=0
    self.total=0
    self.detalles=[]
    
  def agregar_detalle(self, producto:Gestion_de_productos.productos, cantidad_producto):
        detalle = DetalleVenta(producto, cantidad_producto)
        self.detalles.append(detalle)
        if self.cliente.tipo_cliente=='Jurídico' and self.metodo_pago=='De contado':
          self.subtotal += detalle.subtotal*0.95
        else:
          self.subtotal += detalle.subtotal
        self.IVA += detalle.subtotal*0.16
        if self.moneda != 'Bs':
          self.IGTF += detalle.subtotal*0.03
        else:
          self.IGTF=0
        self.total=self.subtotal+self.IVA+self.IGTF
  
  def generar_factura(self):
    print(f"""
          Fecha: {self.fecha}
          Nombre y apellido o razon social: {self.cliente.nombre}
          Domicilio fiscal: {self.cliente.direccion}
          Cédula de identidad o RIF: {self.cliente.identificacion}
          Teléfono: {self.cliente.telefono}
          Condición de pago: {self.metodo_pago}""")
    for i in self.detalles:
      print(f"""
      Producto: {i.producto.nombre}
      Cantidad: {i.cantidad_producto}
      Precio: {i.producto.precio}
      Subtotal: {i.subtotal_producto}""")
    print(f"""
          Subtotal: {self.subtotal}
          IVA: {self.IVA}
          IGTF: {self.IGTF}
          Total: {self.total}""")
#Metodo para imprimir una factura
        
class DetalleVenta:
  def __init__(self,producto,cantidad_producto):
    self.producto=producto
    self.cantidad_producto=cantidad_producto
    self.precio=producto.precio
    self.subtotal=producto.precio*cantidad_producto
#Define la función registrar_venta que interactúa con el usuario para solicitar información sobre la venta y los detalles de venta, y crea una instancia de la clase EncabezadoVenta para representar la venta.
def registrar_venta():
  while True:
    fecha=input('Ingrese la fecha de la venta con el formato AAAA-MM-DD: ')
    if validar_fecha(fecha):
      break
    else:
      print('Error: El formato de fecha debe ser AAAA-MM-DD.')

  while True:
    cliente=Gestion_de_clientes.buscar_cliente_por_atributo()
    if cliente:
      break
    else:
      print('Error: Cliente no encontrado.')
  metodo_pago=input('Ingrese el método de pago (Credito/De contado): ')
  while metodo_pago != 'Credito' and metodo_pago != 'De contado':
    metodo_pago=input('Error: El método de pago debe ser Credito o De contado. Ingrese el método de pago nuevamente: ')
  metodo_envio=input('Ingrese el método de envío: ')
  while True:
    moneda=input('Ingrese la moneda utilizada (Bs/USD): ')
    if moneda=='Bs' or moneda=='USD':
      break
    else:
      print('Error: La moneda debe ser Bs o USD.')
  codigo=input('Ingrese el código de la venta: ')
  venta=EncabezadoVenta(cliente,metodo_pago,metodo_envio,fecha,moneda,codigo)
  while True:
    producto=Gestion_de_productos.buscar_producto_por_atributo()
    if producto:
      cantidad_producto=int(input('Ingrese la cantidad del producto: '))
      venta.agregar_detalle(producto,cantidad_producto)
      respuesta=input('¿Desea agregar otro producto a la venta? (S/N): ')
      if respuesta.upper()=='N':
        break
    else:
      print('Error: Producto no encontrado.')
  lista_ventas.append(venta)
  print('Venta registrada exitosamente.')
#Define la función buscar_venta_por_atributo que permite al usuario buscar ventas registradas por atributo (cliente, método de pago, método de envío, fecha o código) y muestra las facturas correspondientes.
def buscar_venta_por_atributo():
  resultados=[]
  atributo=input('Ingrese el atributo por el que desea buscar (cliente/metodo_pago/metodo_envio/fecha/codigo): ')
  valor=input('Ingrese el valor del atributo: ')
  for venta in lista_ventas:
    if atributo=='cliente' and venta.cliente.nombre==valor:
      resultados.append(venta)
    elif atributo=='metodo_pago' and venta.metodo_pago==valor:
      resultados.append(venta)
    elif atributo=='metodo_envio' and venta.metodo_envio==valor:
      resultados.append(venta)
    elif atributo=='fecha' and venta.fecha==valor:
      resultados.append(venta)
    elif atributo=='codigo' and venta.codigo==valor:
      resultados.append(venta)
  if resultados:
    for venta in resultados:
      venta.generar_factura()
  else:
    print('No se encontraron ventas con el atributo y valor especificados.')
#Define la función menu_ventas que muestra un menú de opciones para el usuario y llama a las funciones correspondientes en función de la opción seleccionada.
def menu_ventas():
  while True:
    print("""
          MENÚ DE VENTAS
          1. Registrar venta
          2. Buscar venta por atributo
          3. Salir""")
    opcion=input('Ingrese una opción: ')
    if opcion=='1':
      registrar_venta()
    elif opcion=='2':
      buscar_venta_por_atributo()
    elif opcion=='3':
      break
    else:
      print('Error: Opción inválida. Intente nuevamente.')