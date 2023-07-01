import requests
#Producto: define la estructura de un objeto Producto, que almacena información sobre el nombre, descripción, precio, categoría y cantidad del inventario.
class Producto:
    def __init__(self, name, description, price, category, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity
    
    def modificar(self, atributo, nuevo_valor):
        if hasattr(self, atributo):
            setattr(self, atributo, nuevo_valor)

productos = []
response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json')
data = response.json()
productos=data
productos = [Producto(name=producto["name"], description=producto["description"], price=producto["price"], category=producto["category"], quantity=producto["quantity"]) for producto in data]



def agregar_producto():
    while True:
        name = input('Ingrese el nombre del producto que desea agregar: ')
        if not name.isalpha():
            print("Error: El nombre del producto debe ser un string.")
        else:
            break
    while True:
        description = input('Ingrese la descripcion del producto que desea agregar: ')
        if not description.isalpha():
            print("Error: La descripción del producto debe ser un string.")
        else:
            break
    while True:
        price = input('Ingrese el precio del producto que desea agregar: ')
        if not price.isnumeric() or float(price) <= 0:
            print("Error: El precio del producto debe ser un número mayor a cero.")
        else:
            break
    while True:
        category = input('Ingrese la categoria del producto que desea agregar: ')
        if not category.isalpha():
            print("Error: La categoría del producto debe ser un string.")
        else:
            break
    while True:
        quantity = input('Ingrese la cantidad en quantity del producto que desea agregar: ')
        if not quantity.isnumeric() or int(quantity) < 0:
            print("Error: El inventario del producto debe ser un número entero mayor o igual a cero.")
        else:
            break
    productos.append(Producto(name, description, price, category, quantity))
#modificar_producto(): permite al usuario buscar un producto por nombre y modificar cualquier atributo del objeto producto correspondiente.
def modificar_producto():
    name = input("Ingrese el nombre del producto que desea modificar: ")
    encontrado = False

    for producto in productos:
        if producto.name == name:
            nuevo_name = input(f"Ingrese el nuevo nombre del producto {producto.name}: ")
            nuevo_description = input(f"Ingrese la nueva descripcion del producto {producto.name}: ")
            nuevo_price = input(f"Ingrese el nuevo precio del producto {producto.name}: ")
            nuevo_category = input(f"Ingrese la nueva categoria del producto {producto.name}: ")
            nuevo_quantity = input(f"Ingrese la nueva cantidad disponible del producto {producto.name}: ")
            producto.modificar("name", nuevo_name)
            producto.modificar("description", nuevo_description)
            producto.modificar("price", nuevo_price)
            producto.modificar("category", nuevo_category)
            producto.modificar("quantity", nuevo_quantity)

            print("Producto modificado con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un producto con ese name.")  

def eliminar_producto():
    name = input("Ingrese el name del producto que desea eliminar: ")
    encontrado = False

    for producto in productos:
        if producto.name == name:
            productos.remove(producto)
            print("Producto eliminado con éxito.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un producto con ese name.")
#buscar_producto_por_atributo: toma una lista de productos y busca aquellos productos que tengan un atributo específico igual a un valor específico.
def buscar_producto_por_atributo(lista_productos, atributo, valor):
    resultados = []
        
    for producto in lista_productos:
        if getattr(producto, atributo) == valor:
            resultados.append(producto.__dict__)
    if resultados:
        return resultados
    else:
        return f"No se encontraron productos con {atributo} = {valor}"
#menuproductos: muestra un menú de opciones al usuario y llama a las funciones correspondientes según la opción seleccionada. 
def menuproductos():
    while True:
        print("          -------- [ Menú ] --------          \n")
        print("     1. Registrar nuevo producto")
        print("     2. Modificar información del producto")
        print("     3. Eliminar producto")
        print("     4. Buscar producto por categoría")
        print("     5. Buscar producto por price")
        print("     6. Buscar producto por name")
        print("     7. Buscar producto por disponibilidad")
        print("     8. Salir")
        opcion = input("     Ingrese el número de opción deseada: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            modificar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
          valor = input("Ingrese el valor de la categoría a buscar: ")
          print(buscar_producto_por_atributo(productos,"category",input("ingrese el valor a buscar")))
        elif opcion == "5":
            print(buscar_producto_por_atributo(productos,"price",input("ingrese el valor a buscar")))
        elif opcion == "6":
            print(buscar_producto_por_atributo(productos,"name",input("ingrese el valor a buscar")))
        elif opcion == "7":
            print(buscar_producto_por_atributo(productos,"quantity",input("ingrese el valor a buscar")))
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    print("Gracias por utilizar el sistema de gestión de productos.")