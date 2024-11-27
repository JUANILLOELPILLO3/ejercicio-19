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


def crear_cliente():#con esta funcion vamos a agregar un cliente a nuestra base de datos 
    nombre = input("Ingrese el nombre del cliente: ")#pedimos que introduzca el nombre
    edad= int(input("Ingrese su edad:"))#pedimos que introduzca el email
    tipo_membresia = input("Ingrese su tipo de membresia: ")#pedimos que introduzca el numeir de telefono 
    cursor.execute(#con curso.excute lo que hacemos es acceder a la base de datos y ejecutar un select un inser into etc.. dependiendo con que lo llamemos
        "INSERT INTO clientes (nombre, edad,tipo_membresia) VALUES (%s, %s, %s)",#en este caso hemos ejecutado un inser into para agregar tanto nombre,como email, como telefono                                                                   
        (nombre, edad, tipo_membresia)#en todo el codigo que tiene que ver con mysql vemos %s esto nos indica la cantidad de columnas que tiene la tabla en este caso tres ponemos 3
    )
    conexion.commit() #  confirmar los cambios en la base de datos
    cliente_id = cursor.lastrowid  #curso.lastrowid es un atributo que tiene pyton que nos permite obtener el id del cliente en funcion de la fila en el que esta es decir si es primera fila sera 1

    print(f"Cliente registrado exitosamente con ID: {cliente_id}")#imprimos el id y el siguiente mensaeje
    return cliente_id
    
def leer_clientes():
        cursor.execute("SELECT * FROM clientes")
        clientes= cursor.fetchall()
        print("Categorías existentes:")
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, edad:{cliente[2]},tipo_membresia:{cliente[3]}")

def actualizar_clientes():
        id_cliente = int(input('Ingresa el ID del cliente a actualizar: '))
        nuevo_nombre = input('Ingresa el nuevo nombre del cliente:')
        nuevo_edad=input('ingresa la nueva edad:')
        nuvo_membresia=input('ingresa la nueva membresia')
        query = " UPDATE cliente SET nombre = %s, edad = %s, tipo_membresia = %s WHERE id_cliente = %s"
        cursor.execute(query, (nuevo_nombre, id_cliente,nuevo_edad,nuvo_membresia))
        conexion.commit()
        print(f'La categoría con ID {id_cliente} ha sido actualizada')
              
def eliminar_clientes():
        id_cliente = int(input('Ingresa el ID de la categoría que deseas eliminar: '))
        query = "DELETE FROM cliente WHERE id_cliente = %s"
        cursor.execute(query, (id_cliente,))
        conexion.commit()
        print(f'La categoría con ID {id_cliente} ha sido eliminada.')
    
 


def crear_actividad():#con esta funcion vamos a agregar un cliente a nuestra base de datos 
    nombre = input("Ingrese el nombre de la actividad: ")#pedimos que introduzca el nombre
    horario= (input("Ingrese su horario:"))#pedimos que introduzca el email
    id_entrenador = int(input("Ingrese el id del entrenador que deseas elegir:"))#pedimos que introduzca el numeir de telefono 
    cursor.execute(#con curso.excute lo que hacemos es acceder a la base de datos y ejecutar un select un inser into etc.. dependiendo con que lo llamemos
        "INSERT INTO actividades (nombre, horario,id_entrenador) VALUES (%s, %s, %s)",#en este caso hemos ejecutado un inser into para agregar tanto nombre,como email, como telefono                                                                   
        (nombre, horario, id_entrenador)#en todo el codigo que tiene que ver con mysql vemos %s esto nos indica la cantidad de columnas que tiene la tabla en este caso tres ponemos 3
    )
    conexion.commit() #  confirmar los cambios en la base de datos
    actividad_id = cursor.lastrowid  #curso.lastrowid es un atributo que tiene pyton que nos permite obtener el id del cliente en funcion de la fila en el que esta es decir si es primera fila sera 1

    print(f"Cliente registrado exitosamente con ID: {actividad_id}")#imprimos el id y el siguiente mensaeje
    return actividad_id
def leer_actividades():
        cursor.execute("SELECT * FROM actividades")
        actividades= cursor.fetchall()
        print("Categorías existentes:")
        for actividad in actividades:
            print(f"ID: {actividad[0]}, Nombre: {actividad[1]}, horario:{actividad[2]},identrenador:{actividad[3]}")
def actualizar_actividades():
        id_actividad = int(input('Ingresa el ID de la actividad a actualizar: '))
        nuevo_nombre= input('Ingresa el nuevo nombre de la actividad:')
        nuevo_horario=input('ingresa el nuevo horario:')
        nuevo_identrenador=input('ingresa el nuevo id')
        query = " UPDATE actividad SET nombre_actividad = %s, horario = %s id_entrenador=%s,  WHERE id_actividad= %s"
        cursor.execute(query, (nuevo_nombre, id_actividad,nuevo_horario,nuevo_identrenador))
        conexion.commit()
        print(f'La categoría con ID {id_actividad} ha sido actualizada')
def eliminar_actividades():
        id_actividad = int(input('Ingresa el ID de la actividad que deseas eliminar: '))
        query = "DELETE FROM actividad WHERE id_actividad= %s"
        cursor.execute(query, (id_actividad,))
        conexion.commit()
        print(f'La categoría con ID {id_actividad} ha sido eliminada.')

def crear_entrenador():#con esta funcion vamos a agregar un cliente a nuestra base de datos 
    nombre = input("Ingrese el nombre del entrenador: ")#pedimos que introduzca el nombre
    especialidad= input("Ingrese su actividad:")#pedimos que introduzca el email
    query = "INSERT INTO entrenadores (nombre_entrenador, especialidad) VALUES (%s, %s)"
    cursor.execute(query, (nombre, especialidad,) )
    conexion.commit() #  confirmar los cambios en la base de datos
    entrenador_id = cursor.lastrowid  #curso.lastrowid es un atributo que tiene pyton que nos permite obtener el id del cliente en funcion de la fila en el que esta es decir si es primera fila sera 1

    print(f"Cliente registrado exitosamente con ID: {entrenador_id}")#imprimos el id y el siguiente mensaeje
    return entrenador_id
def leer_entrenadores():
        cursor.execute("SELECT * FROM entrenadores")
        entrenadores= cursor.fetchall()
        print("entrenaodres existentes:")
        for entrenador in entrenadores:
            print(f"ID: {entrenador[0]}, Nombre: {entrenador[1]}, especialidad:{entrenador[2]}")
def actualizar_entrenador():
      id_entrenador= int(input('ingresa el id del entrenaodr que quieres actualizar'))
      nuevo_nombre=input('ingresa el nuevo nombre del entrenador')
      nueva_especialidad=input('ingrese la nueva especialidad que quieres actualizar')
      querey="UPDATE entrenador set nombre_entrenador=%s,especialidad=%s, where id_entrenador=%s" 
      cursor.execute(querey(id_entrenador,nuevo_nombre,nueva_especialidad))
      conexion.commit()
      print(f'La categoría con ID {id_entrenador} ha sido actualizada')
def eliminar_entrenador():
      id_entrenador=int(input('ingresa el id del entrenador que deseas eliminar'))
      querey="DELETE FROM actividad WHERE id_entrenador= %s"
      cursor.execute(querey(id_entrenador))
      print(f'La categoría con ID {id_entrenador} ha sido eliminada.')        

    
    
def crear_inscripcion():#con esta funcion vamos a agregar un cliente a nuestra base de datos 
    id_Cliente = int(input("Ingrese el id del cliente "))#pedimos que introduzca el nombre
    id_actividad= int(input("Ingrese el id de la actividad"))#pedimos que introduzca el email
    cursor.execute(#con curso.excute lo que hacemos es acceder a la base de datos y ejecutar un select un inser into etc.. dependiendo con que lo llamemos
        "INSERT INTO clientes (id_clie, especialidad,) VALUES (%s, %s)",#en este caso hemos ejecutado un inser into para agregar tanto nombre,como email, como telefono                                                                   
        (id_Cliente, id_actividad)#en todo el codigo que tiene que ver con mysql vemos %s esto nos indica la cantidad de columnas que tiene la tabla en este caso tres ponemos 3
    )
    conexion.commit() #  confirmar los cambios en la base de datos
    inscripcion_id = cursor.lastrowid  #curso.lastrowid es un atributo que tiene pyton que nos permite obtener el id del cliente en funcion de la fila en el que esta es decir si es primera fila sera 1

    print(f"Cliente registrado exitosamente con ID: {inscripcion_id}")#imprimos el id y el siguiente mensaeje
    
def leer_inscripciones():
      cursor.execute("select * from inscripciones")
      inscripciones=cursor.fetchall
      print("entrenadores existentes")
      for inscripcion in inscripciones:
            print(f"id: {inscripcion[0]}, id: {inscripcion[1]}, id: {inscripcion[1]}")


  
 