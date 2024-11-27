import funciones as pr
import conexion as er
import menus as vr
er.conexion
while True:
    print('bienvenido al centro deportivo virtual\n\
          1.trabar con clientes\n\
          2.trabajar con actividades\n\
          3.trabajar con entrenadores\n\
          4.trabajar con inscripciones\n\
          5.salir')
    opcion=int(input('eliige la opcion con la que quieres trabajar poniendo su numero:'))

    if opcion==1:
        vr.menu_cliente()
    if opcion==2:
        vr.menu_actividad()      
    if opcion==3:
        vr.menu_entrenador()
    if opcion==4:
        vr.menu_inscpricion()
    if opcion==5:
        print('gracias por su visita')
        break

