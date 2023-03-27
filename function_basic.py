from crud import *
from parameters import *

def find_producto():
    print("Qué método de búsqueda desea usar?")
    print("1. Categoría")
    print("2. Nombre")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        categoria = input("Ingrese categoría del producto a buscar: ")
        buscar_producto_categoria(categoria)
    elif opcion == "2":
        nombre = input("Ingrese nombre del producto a buscar: ")
        buscar_producto_nombre(nombre)
    else:
        print("Opción no válida...")

def delete_producto_f():
    id = int(input("Ingrese el id del producto a eliminar: "))
    delete_producto(id)

def create_json_producto():
    nombre = input("Nombre del Producto: ")
    categoria = input("Categoría: ")
    tipo = input("Tipo: ")
    cantidad = int(input("Cantidad: "))
    estado = input("Estado: ")
    precio = input("Precio: ")

    producto = {
        "nombreProducto": nombre,
        "categoria": categoria,
        "tipo": tipo,
        "cantidad": cantidad,
        "estado": estado,
        "precio": precio
    }
    return producto

def create_json_producto_update():
    print("Menú")
    print("1. Modificar todo el documento")
    print("2. Moficar un elemento del documento")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        return create_json_producto()
    elif opcion == "2":
        indice = input("Ingrese el indice a buscar: ")
        valor = input("Ingrese el valor a sustituir: ")
        producto = {indice: valor}
        return producto