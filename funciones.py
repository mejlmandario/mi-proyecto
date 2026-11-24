import funciones_sql

def agregar_productos():
    # Ingresar nombre    
    nombre = input("Ingrese el nombre del producto: ").lower().strip()
    while nombre == "":
        print("El nombre no puede estar vacio")
        nombre = input("Ingrese el nombre del producto: ").lower().strip()

    # Ingresar descripcion
    descripcion = input("Ingrese la descripcion del producto: ").lower().strip()
    
    # Ingresar categoria
    categoria = input("Ingrese la categoria del producto: ").lower().strip()
    while categoria == "":
        print("El categoria no puede estar vacio")
        categoria = input("Ingrese el categoria del producto: ").lower().strip()
    
    # Ingresar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese el stock del producto: "))
            
            if cantidad < 0:
                print("El valor ingresado no puede ser negativo.")
                continue
            else:
                break
        except ValueError:
            print("El valor ingresado debe ser un numero entero")
         
    # Ingresar precio
    while True:
        try:
            precio = int(input("Ingrese el precio del producto: "))
            
            if precio <= 0:
                print("El precio debe ser mayor a cero")
                continue
            
            break
        except ValueError:
            print("Error: debe ingresar un numero entero")
    
    funciones_sql.registrar_producto(nombre,descripcion,categoria,cantidad,precio)
    
    print(f"El producto {nombre} ha sido agregado correctamente.")
    
def mostrar_productos(lista):
    if len(lista) == 0:
        print("No hay productos registrados.")
    else:
        print("-- PRODUCTOS --")

        for indice in range(len(lista)):
            producto = lista[indice]

            print(f"ID: {producto[0]}. Nombre: {producto[1]}")
            print(f"   Descripcion: {producto[2]}")
            print(f"   Categoria: {producto[3]}")
            print(f"   Cantidad: {producto[4]}")
            print(f"   Precio: {producto[5]}")
            print("\n")
    
def mostrar_todos_los_productos():
    lista_productos= funciones_sql.obtener_todos_los_productos()
    mostrar_productos(lista_productos)

def buscar_productos_por_id():
    try:
        id = int(input("Ingrese el id del producto: "))
        producto = funciones_sql.obtener_producto_por_id(id)
        
        if producto:
           mostrar_productos([producto])
           return producto
        else:
            print("El producto no existe")
            return None
    except ValueError:
        print("Error: el ID debe ser un numero entero")
        
def actualizar_producto_por_id():
    producto = buscar_productos_por_id() 
    
    if producto:
        print("Campos para actualizar:")
        print("1. Actualizar nombre")
        print("2. Actualizar descripcion")
        print("3. Actualizar categoria")
        print("4. Actualizar cantidad")
        print("5. Actualizar precio")
        
        opcion = input("Seleccione la opcion deseada: ")
        
        match opcion:
            case "1":
                # actualizar nombre
                nombre = input("Ingrese el nuevo nombre del producto: ").lower().strip()
                while nombre == "":
                    print("El nombre no puede estar vacio")
                    nombre = input("Ingrese el nombre del producto: ").lower().strip()
                
                funciones_sql.actualizar_nombre(producto[0],nombre)
                print("El nombre del producto ha sido actualizado")
            
            case "2":
                # actualizcar descripcion
                descripcion = input("Ingrese la descripcion del producto: ").lower().strip()
                 
                funciones_sql.actualizar_descripcion(producto[0],descripcion)  
                print("La descripcion del producto ha sido actualizada")
                 
            case "3":
                # actualizar categoria
                categoria = input("Ingrese la categoria del producto: ").lower().strip()
                while categoria == "":
                    print("El categoria no puede estar vacio")
                    categoria = input("Ingrese el categoria del producto: ").lower().strip()
                
                funciones_sql.actualizar_categoria(producto[0],categoria)
                print("La categoria del producto ha sido actualizada")

            case "4":
                # actualizar cantidad
                while True:
                    try:
                        cantidad = int(input("Ingrese el stock del producto: "))
                        
                        if cantidad < 0:
                            print("El valor ingresado no puede ser negativo.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("El valor ingresado debe ser un numero entero")
                    
                funciones_sql.actualizar_cantidad(producto[0],cantidad)
                print("La cantidad del producto ha sido actualizada")

            case "5":
                # actualizar precio
                while True:
                    try:
                        precio = int(input("Ingrese el precio del producto: "))
                        
                        if precio <= 0:
                            print("El precio debe ser mayor a cero")
                            continue
                        
                        break
                    except ValueError:
                        print("Error: debe ingresar un numero entero")
                        
                funciones_sql.actualizar_precio(producto[0],precio)
                print("El precio del producto ha sido actualizado")
                
            case _:
                print("La opcion ingresada no es valida")
             
def eliminar_productos():
    # Eliminar producto
   try:
        id_producto = int(input("Ingrese el id del producto que desea eliminar: ")) 
        
        if id_producto <= 0:
            print("Error: el ID debe ser numero entero positivo") 
            return
        
        producto = funciones_sql.obtener_producto_por_id(id_producto)
        
        if not producto:
            print("El producto no existe.")
            return
        
        confirmacion = input(f"Confirma eliminar {producto[1]} (s/n): ").lower().strip()
        
        if confirmacion != "s":
            print("Eliminacion cancelada")
            return
        
        if funciones_sql.eliminar_producto_por_id(id_producto):
            print(f"El producto {producto[1]} ha sido eliminado")
        else:
            print("No se pudo eliminar el producto")
   except Exception as error:
       print("Error: el ID debe ser un numero entero")

def reporte_stock_minimo():
    # Validacion de la variable limite
    while True:
        try:
            limite = int(input("Ingrese el limite de cantidad: "))
            if limite < 0:
                print("El liminte no puede ser negativo")
                continue
            
            break
        except ValueError:
            print("Error: el numero debe ser entero")
        
    productos = funciones_sql.obtener_productos_bajo_stock(limite)
    
    if not productos:
        print(f"No hay productos con cantidad igual o inferior a {limite}")
    else:
        print(f"REPORTE DE STOCK (CANTIDAD <= {limite})")
        mostrar_productos(productos)
            