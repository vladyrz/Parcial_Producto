from crud import *
from function_basic import *

while True:
    print("Menú")
    print("1) Consultar todos los productos")
    print("2) Buscar un producto")
    print("3) Agregar un producto")
    print("4) Modificar un producto")
    print("5) Eliminar un producto")
    print("6) Salir del sistema" )

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        mostrar_producto()
    elif opcion == "2":
        find_producto()
    elif opcion == "3":
        producto = create_json_producto()
        create_producto(producto)
    elif opcion == "4":
        id = int(input("Ingrese el id del producto a modificar: "))
        producto = create_json_producto_update()
        update_producto(id, producto)
    elif opcion == "5":
        delete_producto_f()
    elif opcion == "6":
        break
    else:
        print("Opción no válida!")