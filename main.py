import funciones
from conexion import crear_tabla

lista_productos = [
    ["manzana","descripcion", "fruta",0,2000],
    ["manteca","descripcion", "lacteo",0, 4000],
    ["pan lactal","descripcion", "panaderia",0,5000],
    ["banana ecuador","descripcion","fruta",0,2000],
    ["banana roja","descripcion","fruta",0,6000]
]
crear_tabla()

while True:
    print("Sistema de gestion de productos".upper())
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock minimo")
    print("7. Salir")
    
    opcion = input("Seleccione una opcion: ").strip()
    
    match opcion:
        # Agregar productos
        case "1":   
            funciones.agregar_productos()        
        
        # Mostrar productos
        case "2":
            funciones.mostrar_todos_los_productos()
            
        # Busqueda de productos por ID
        case "3":
            funciones.buscar_productos_por_id()
            
        # Actualizar producto
        case "4":
            funciones.actualizar_producto_por_id()
        
        # Eliminar producto
        case "5":
            funciones.eliminar_productos()  
              
        # Reporte de stock minimo 
        case "6":
            funciones.reporte_stock_minimo()
               
        # Salida del programa  
        case "7":
            print("Saliendo del programa")
            break
            
        case _:
            print("La opcion ingresada no es valida, intente de nuevo")
            continue
