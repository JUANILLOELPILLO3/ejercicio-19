import funciones as pr#creamos todos los submenus del menu y con estos sera con los que trabajemos 
def menu_cliente():#submenu cliente
    while True:
            print('bienvenido al servicio clientes\n\
                1.crear cliente\n\
                2.leer lista de clientes\n\
                3.actualizar cliente\n\
                4.borrar cliente\n\
                5.salir')
            opcion=int(input('introduce la opcion que deseas realizar con su numero'))
            if opcion==1:
                pr.crear_cliente()
            elif opcion==2:
                pr.leer_clientes()
            elif opcion==3:
                pr.actualizar_clientes()
            elif opcion==4:
                pr.eliminar_clientes()
            elif opcion==5:
                print('se han guardado los cambios')
                break

def menu_actividad():#submenu actividad
      while True:
            print('bienvenido al servicio actividades\n\
                1.crear actividad\n\
                2.leer lista de actividades\n\
                3.actualizar actividad\n\
                4.borrar actividad\n\
                5.salir')
            opcion=int(input('introduce la opcion que deseas realizar con su numero'))
            if opcion==1:
                pr.crear_actividad()
            elif opcion==2:
                pr.leer_actividades()
            elif opcion==3:
                pr.actualizar_actividades()
            elif opcion==4:
                pr.eliminar_actividades()
            elif opcion==5:
                print('se han guardado los cambios')
                break   

def menu_entrenador():#sub menu entrenador 
       while True:
            print('bienvenido al servicio entrnadores\n\
                1.crear entrenador\n\
                2.leer lista de entrenadores\n\
                3.actualizar entrenador\n\
                4.borrar entrenador\n\
                5.salir')
            opcion=int(input('introduce la opcion que deseas realizar con su numero'))
            if opcion==1:
                pr.crear_entrenador()
            elif opcion==2:
                pr.leer_entrenadores()
            elif opcion==3:
                pr.actualizar_entrenador()
            elif opcion==4:
                pr.eliminar_entrenador()
            elif opcion==5:
                print('se han guardado los cambios')
                break         

def menu_inscpricion():#sub menu inscripcion 
      while True:
            print('bienvenido al servicio clientes\n\
                1.crear cliente\n\
                2.leer lista de inscripciones\n\
                3.salir')
            opcion=int(input('que opcion quieres elegir'))
            if opcion==1:
                pr.crear_inscripcion()
            elif opcion==2:
                pr.leer_inscripciones()
            elif opcion==3:
                print('se han guardado los cambios')
                break