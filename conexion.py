def conexion():#conexion my-sql
    import mysql.connector
        # Conexión a la base de dato
    conexion = mysql.connector.connect(
        host="localhost",       # Dirección del servidor
        user="root",            # Usuario de la base de datos
        password="curso",       # Contraseña del usuario
        database="centro_deportivo"  # Nombre de la base de datos
        )

    if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            # Crear un cursor para ejecutar consultas
            cursor = conexion.cursor()
            conexion.commit()