# ----------------------------------------------------------------------------------------------------------------------

import numpy as np
from util.file import *

# ----------------------------------------------------------------------------------------------------------------------

class Shotgun(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, nombre_archivo_entrada, nombre_archivo_salida, cantidad_fragmentos,
                 promedio_tamanho, desviacion_estandar, traslape_minimo, traslape_maximo,
                 sustituciones=0, inserciones=0, deleciones=0, inversiones=0, quimeras=0):

    # ------------------------------------------------------------------------------------------------------------------

        self.nombre_archivo_entrada = nombre_archivo_entrada
        self.nombre_archivo_salida = nombre_archivo_salida

        self.cantidad_fragmentos = cantidad_fragmentos
        self.promedio_tamanho = promedio_tamanho
        self.desviacion_estandar = desviacion_estandar

        self.traslape_minimo = traslape_minimo
        self.traslape_maximo = traslape_maximo

        self.sustituciones = sustituciones
        self.inserciones = inserciones
        self.delecioens = deleciones
        self.inversiones = inversiones
        self.quimeras = quimeras

        self.frags = self.ejecutar()
        self.guardar()

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar(self):
        texto = leer_y_sustituir_por_espacios(self.nombre_archivo_entrada)
        print("Texto original: " + texto)
        rango = calcularRango(self.desviacion_estandar, self.promedio_tamanho)
        frags = generadorFragmentos(texto, self.cantidad_fragmentos, rango, self.traslape_minimo, self.traslape_maximo)
        # frags = agregar_errores(texto, frags, 60, sustitucion)
        # frags = agregar_errores(texto, frags, 60, insercion)
        # frags = agregar_errores(texto, frags, 60, delecion)
        print("Fragmentos generados: " + str(frags))
        return frags

    def guardar(self):
        # Colocar aqui el crear el archivo descriptivo
        escribir_archivo_fragmentos(self.nombre_archivo_salida, self.frags)

    # ------------------------------------------------------------------------------------------------------------------


def leer_y_sustituir_por_espacios(nombre_archivo):
    cadena = open_file(nombre_archivo)
    cadena = cadena.replace("\n", " ")
    return cadena


def escribir_archivo_fragmentos(nombre_archivo, frags):
    cadena = ""
    for frag in frags:
        cadena += frag + "\n"
    save_file(nombre_archivo, cadena)


def calcularRango(desviacion, promedio):
    rango = [promedio-desviacion, promedio+desviacion]
    return rango

def obtenerFragmentos(i, texto, frags, rango, cantidad, traslapeMin, traslapeMax):
    longMin = rango[0]
    longMax = rango[1]
    while i<len(texto):
        tamanno= np.random.randint(longMin, longMax)
        frag=""
        cont=0
        traslape = np.random.randint(traslapeMin, traslapeMax)
        if (i > traslape):
            i -= traslape
        while cont < tamanno and i<len(texto):
            frag=frag+texto[i]
            i+= 1
            cont+= 1
        frags.append(frag)
        if len(frags)==cantidad:
            break
    return frags

def generadorFragmentos(texto, cantidad, rango, traslapeMin, traslapeMax):
    frags = []
    i=0
    frags = obtenerFragmentos(i, texto, frags, rango, cantidad, traslapeMin, traslapeMax)
    while len(frags) < cantidad:
        i = np.random.randint(0, len(frags))
        frags = obtenerFragmentos(i, texto, frags, rango, cantidad, traslapeMin, traslapeMax)

    return frags

# ----------------------------------------------------------------------------------------------------------------------


def sustitucion(cadena, dominio):

    cadena = list(cadena)
    dominio = list(dominio.replace(" ", ""))

    indice_sustituto = np.random.randint(0, len(dominio))
    indice_sustitucion = np.random.randint(0, len(cadena))

    cadena[indice_sustitucion] = dominio[indice_sustituto]
    return "".join(cadena)


# ----------------------------------------------------------------------------------------------------------------------


def insercion(cadena, dominio):

    cadena = list(cadena)
    dominio = list(dominio.replace(" ", ""))

    indice_insertar = np.random.randint(0, len(dominio))
    indice_insercion = np.random.randint(0, len(cadena))

    cadena.insert(indice_insercion, dominio[indice_insertar])
    return "".join(cadena)

# ----------------------------------------------------------------------------------------------------------------------


def delecion(cadena, *dominio):

    cadena = np.array(list(cadena))

    indice_delecion = np.random.randint(0, len(cadena))
    indices_conservar = np.delete(range(0, len(cadena)), indice_delecion)

    cadena = cadena[indices_conservar]
    return "".join(cadena)

# ----------------------------------------------------------------------------------------------------------------------

# def quimera(*cadena, dominio):
#
#     frag1 = dominio[np.random.randint(0, len(dominio))]
#     frag2 = dominio[np.random.randint(0, len(dominio))]
#     print("Fragmentps a unir")
#
#     indice_delecion = np.random.randint(0, len(cadena))
#     indices_conservar = np.delete(range(0, len(cadena)), indice_delecion)
#
#     cadena = cadena[indices_conservar]
#     return "".join(cadena)

# ----------------------------------------------------------------------------------------------------------------------


def agregar_errores(texto, frags, porcentaje, funcion):

    frags = np.array(frags)
    cantidad = int(porcentaje / 100 * len(frags))
    # print("Cantidad de fragmentos: " + str(cantidad))

    indices = np.sort(np.random.choice(len(frags), cantidad, False))
    # print("Indices de los fragmentos para agregar errores: \n" + str(indices))

    frags[indices] = [funcion(frag, texto) for frag in frags[indices]]
    # print("Fragmentos alterados: \n" + str(frags))
    return frags

# ----------------------------------------------------------------------------------------------------------------------

# texto = "cuenta la historia de un mago"
# frags = ["cuent", "a la his", "historia de", " de un ma", "ago"]
# # frags = agregar_errores(texto, frags, 60, sustitucion)
# # frags = agregar_errores(texto, frags, 60, insercion)
# # frags = agregar_errores(texto, frags, 60, delecion)
# # frags = agregar_errores(texto, frags, 60, quimera)
#
# # Ejemplo del generador de fragmentos (texto, cantidad, rangoInicial, rangoFinal)
# print(generadorFragmentos(texto, 9, 3, 7))
shotgun = Shotgun("../docs/prueba1.txt", "../docs/salida.txt", cantidad_fragmentos=20, desviacion_estandar=3, promedio_tamanho=10, traslape_minimo=2, traslape_maximo=6)
# shotgun.ejecutar()