import numpy as np

# Pedir al usuario:
# -La cantidad de fragmentos que desea
# -Promedio del tamanno de cada fragmento
# -
# -Decidir si incluir estos datos en el archivo donde esta el texto o se le solicita
# por medio de la consola


def leerArchivo():  # La idea de esta funcion es pasar el texto del archivo a una lista
    # hay que implementarlo
    return "Lista"

def calcularRango(desviacion, promedio):
    rango =[promedio-desviacion, promedio+desviacion]
    return rango

def obtenerFragmentos(i, texto, frags, longMin, longMax, cantidad):
    while i<len(texto):
        tamanno= np.random.randint(longMin, longMax)
        frag=""
        cont=0
        while cont < tamanno and i<len(texto):
            frag=frag+texto[i]
            i+= 1
            cont+= 1
        frags.append(frag)
        if len(frags)==cantidad:
            break
    return frags

def generadorFragmentos(texto, cantidad, longMin, longMax):
    frags = []
    i=0
    frags = obtenerFragmentos(i, texto, frags, longMin, longMax, cantidad)
    while len(frags) < cantidad:
        i = np.random.randint(0, len(frags))
        frags = obtenerFragmentos(i, texto, frags, longMin, longMax, cantidad)

    return frags



def escribirFragmentos():  # La idea es leer la lista y escribirla en el archivo resultado
    return

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


def quimera(*cadena, dominio):

    frag1 = dominio[np.random.randint(0, len(dominio))]
    frag2 = dominio[np.random.randint(0, len(dominio))]
    print("Fragmentps a unir")

    indice_delecion = np.random.randint(0, len(cadena))
    indices_conservar = np.delete(range(0, len(cadena)), indice_delecion)

    cadena = cadena[indices_conservar]
    return "".join(cadena)

# ----------------------------------------------------------------------------------------------------------------------


def agregar_errores(texto, frags, porcentaje, funcion):

    frags = np.array(frags)
    cantidad = int(porcentaje / 100 * len(frags))
    print("Cantidad de fragmentos: " + str(cantidad))

    indices = np.sort(np.random.choice(len(frags), cantidad, False))
    print("Indices de los fragmentos para agregar errores: \n" + str(indices))

    frags[indices] = [funcion(frag, texto) for frag in frags[indices]]
    print("Fragmentos alterados: \n" + str(frags))
    return frags

# ----------------------------------------------------------------------------------------------------------------------

texto = "cuenta la historia de un mago"
frags = ["cuent", "a la his", "historia de", " de un ma", "ago"]
# frags = agregar_errores(texto, frags, 60, sustitucion)
# frags = agregar_errores(texto, frags, 60, insercion)
# frags = agregar_errores(texto, frags, 60, delecion)
frags = agregar_errores(texto, frags, 60, quimera)

# Ejemplo del generador de fragmentos (texto, cantidad, rangoInicial, rangoFinal)
print(generadorFragmentos(texto, 9, 3, 7))
