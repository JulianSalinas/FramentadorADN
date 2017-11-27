# ----------------------------------------------------------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------------------------------------------------------

class AlgErrores(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, texto, fragmentos):
        self.texto = texto
        self.fragmentos = np.array(fragmentos)

    # ------------------------------------------------------------------------------------------------------------------

    def agregar_errores(self, sustituciones=0, inserciones=0, deleciones=0, inversiones=0, quimeras=0):

        self.fragmentos = self.aplicar_errores(sustituciones, self.sustitucion)
        self.fragmentos = self.aplicar_errores(inserciones, self.insercion)
        self.fragmentos = self.aplicar_errores(deleciones, self.delecion)
        self.fragmentos = self.aplicar_errores(inversiones, self.insercion)
        self.fragmentos = self.aplicar_errores(quimeras, self.quimera)

        return self.fragmentos

    # ------------------------------------------------------------------------------------------------------------------

    def aplicar_errores(self, porcentaje, funcion):

        cantidad = int(porcentaje / 100 * len(self.fragmentos))
        indices = np.sort(np.random.choice(len(self.fragmentos), cantidad, False))
        self.fragmentos[indices] = [funcion(frag) for frag in self.fragmentos[indices]]

        return self.fragmentos

    # ------------------------------------------------------------------------------------------------------------------

    def sustitucion(self, cadena):

        cadena = list(cadena)
        texto = list(self.texto.replace(" ", ""))

        indice_sustituto = np.random.randint(0, len(texto))
        indice_sustitucion = np.random.randint(0, len(cadena))

        cadena[indice_sustitucion] = texto[indice_sustituto]
        return "".join(cadena)

    # ------------------------------------------------------------------------------------------------------------------


    def insercion(self, cadena):

        cadena = list(cadena)
        dominio = list(self.texto.replace(" ", ""))

        indice_insertar = np.random.randint(0, len(dominio))
        indice_insercion = np.random.randint(0, len(cadena))

        cadena.insert(indice_insercion, dominio[indice_insertar])
        return "".join(cadena)

    # ------------------------------------------------------------------------------------------------------------------


    def delecion(self, cadena):

        cadena = np.array(list(cadena))

        indice_delecion = np.random.randint(0, len(cadena))
        indices_conservar = np.delete(range(0, len(cadena)), indice_delecion)

        cadena = cadena[indices_conservar]
        return "".join(cadena)

    # ------------------------------------------------------------------------------------------------------------------

    def quimera(self, fragmentos):
        return self.fragmentos

    # ------------------------------------------------------------------------------------------------------------------


    def inversion(self, cadena):
        return self.fragmentos

    # ------------------------------------------------------------------------------------------------------------------