import time
import random
import threading

cantidad_Autos = 0

# Función para agregar un auto al estacionamiento
def agregar_Auto(estacionamiento, agregar_lock, agregar_freq):
    while True:
        agregar_lock.acquire()
        if len(estacionamiento) < 12:
            estacionamiento.append("Auto")
            print(f"Se ha agregado un auto al estacionamiento.")
            global cantidad_Autos
            cantidad_Autos += 1
            mostrar_Cantidad_Autos()
        else:
            print("El estacionamiento está lleno. No se puede agregar más autos.")
        tiempo_agregar = random.choice(agregar_freq)
        agregar_lock.release()
        time.sleep(tiempo_agregar)

# Función para retirar un auto del estacionamiento
def retirar_Auto(estacionamiento, retirar_lock, retirar_freq):
    while True:
        retirar_lock.acquire()
        if len(estacionamiento) > 0:
            estacionamiento.pop(0)
            print(f"Se ha retirado un auto del estacionamiento.")
            global cantidad_Autos
            cantidad_Autos -= 1
            mostrar_Cantidad_Autos()
        else:
            print("El estacionamiento está vacío. No se puede retirar ningún auto.")
        tiempo_retirar = random.choice(retirar_freq)
        retirar_lock.release()
        time.sleep(tiempo_retirar)

#Función para mostrar la cantidad de autos en el estacionamiento
def mostrar_Cantidad_Autos():
    global cantidad_Autos
    print(f"Cantidad de autos en el estacionamiento: {cantidad_Autos}")

# Función para que el usuario modifique la frecuencia de agregar autos
def modificar_frecuencia(agregar_lock, agregar_freq):
    while True:
        nueva_Frecuencia = input("Introduce una nueva frecuencia para agregar autos: \n").split(',')
        nueva_Frecuencia = [float(f) for f in nueva_Frecuencia]
        agregar_lock.acquire()
        agregar_freq.clear()
        agregar_freq.extend(nueva_Frecuencia)
        agregar_lock.release()

# Función para que el usuario modifique la frecuencia de retirar autos
def modificar_frecuencia_retirar(retirar_lock, retirar_freq):
    while True:
        nueva_Frecuencia = input("Introduce una nueva frecuencia para retirar autos: \n").split(',')
        nueva_Frecuencia = [float(f) for f in nueva_Frecuencia]
        retirar_lock.acquire()
        retirar_freq.clear()
        retirar_freq.extend(nueva_Frecuencia)
        retirar_lock.release()

# Función para ejecutar el programa principal
def programa_Estacionamiento():
    estacionamiento = []
    agregar_Frecuencia = [0.5, 1, 2]
    retirar_Frecuencia = [0.5, 1, 2]
    
    # Crear cerrojos para controlar la modificación de frecuencias
    agregar_Lock = threading.Lock()
    retirar_Lock = threading.Lock()

    # Crear hilos para agregar, retirar y modificar frecuencias
    hilo_Agregar_Auto = threading.Thread(target=agregar_Auto, args=(estacionamiento, agregar_Lock, agregar_Frecuencia))
    hilo_Retirar_Auto = threading.Thread(target=retirar_Auto, args=(estacionamiento, retirar_Lock, retirar_Frecuencia))
    hilo_Modificar_Frecuencia_Agregar = threading.Thread(target=modificar_frecuencia, args=(agregar_Lock, agregar_Frecuencia))
    hilo_Modificar_Frecuencia_Retirar = threading.Thread(target=modificar_frecuencia_retirar, args=(retirar_Lock, retirar_Frecuencia))
    hilo_Mostrar_Autos = threading.Thread(target=mostrar_Cantidad_Autos)

    # Iniciar los hilos
    hilo_Agregar_Auto.start()
    hilo_Retirar_Auto.start()
    hilo_Modificar_Frecuencia_Agregar.start()
    hilo_Modificar_Frecuencia_Retirar.start()
    hilo_Mostrar_Autos.start()

programa_Estacionamiento()