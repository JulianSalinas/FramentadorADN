# ----------------------------------------------------------------------------------------------------------------------

from util.file import *

# ----------------------------------------------------------------------------------------------------------------------


class DAOShotgun(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.archivo_entrada = "../files/entrada.txt"
        self.archivo_salida = "../files/salida.txt"

    # ------------------------------------------------------------------------------------------------------------------

    def abrir_archivo(self, nombre_archivo=None):

        if nombre_archivo is None:
            nombre_archivo = self.archivo_entrada

        cadena = open_file(nombre_archivo)
        cadena = cadena.replace("\n", " ")

        return cadena

    # ------------------------------------------------------------------------------------------------------------------

    def guardar_archivo(self, fragmentos, nombre_archivo=None):

        if nombre_archivo is None:
            nombre_archivo = self.archivo_salida

        cadena = "".join([fragmento + "\n" for fragmento in fragmentos])
        save_file(nombre_archivo, cadena)

# ----------------------------------------------------------------------------------------------------------------------
