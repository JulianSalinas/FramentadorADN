# ----------------------------------------------------------------------------------------------------------------------

from util.file import *

# ----------------------------------------------------------------------------------------------------------------------


class DAOShotgun(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.archivo_entrada = "../files/entrada.txt"
        self.archivo_salida_fragmentos = "../files/salida.txt"
        self.archivo_salida_descripcion = "../files/salida.pyd"

    # ------------------------------------------------------------------------------------------------------------------

    def abrir_archivo_fragmentos(self, nombre_archivo=None):

        if nombre_archivo is None:
            nombre_archivo = self.archivo_entrada

        cadena = open_file(nombre_archivo)
        cadena = cadena.replace("\n", " ")

        return cadena

    # ------------------------------------------------------------------------------------------------------------------

    def guardar_archivo_fragmentos(self, fragmentos, nombre_archivo=None):

        if nombre_archivo is None:
            nombre_archivo = self.archivo_salida_fragmentos

        cadena = "".join([fragmento + "\n" for fragmento in fragmentos])
        save_file(nombre_archivo, cadena)

    # ------------------------------------------------------------------------------------------------------------------

    def abrir_archivo_descriptivo(self, nombre_archivo=None):
        diccionario = eval(open_file(nombre_archivo))
        return diccionario

    # ------------------------------------------------------------------------------------------------------------------

    def guardar_archivo_descriptivo(self, diccionario=None, nombre_archivo=None):
        contenido = str(diccionario)
        save_file(nombre_archivo, contenido)
        return diccionario

# ----------------------------------------------------------------------------------------------------------------------
