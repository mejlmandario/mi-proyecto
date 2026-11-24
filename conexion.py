import sqlite3

def conectar():
    conexion = sqlite3.connect("inventario.db")
    return conexion

def crear_tabla():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT,
                cantidad INTEGER NOT NULL,
                precio INTEGER NOT NULL
            )                           
        """)
        
        conexion.commit()
        print("Tabla de productos creada correctamente")
    except sqlite3.Error as error:
        print(f"Error al crear la tabla: {error}")
    finally:
        conexion.close()