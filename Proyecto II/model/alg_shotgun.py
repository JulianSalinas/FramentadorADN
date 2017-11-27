# ----------------------------------------------------------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------------------------------------------------------


class AlgShotgun(object):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):

        self.cantidad_fragmentos = 100
        self.promedio_tamanho = 6
        self.desviacion_estandar = 3
        self.rango_traslape = (1, 4)
        self.fragmentos = []

    # ------------------------------------------------------------------------------------------------------------------

    def set_cantidad_fragmentos(self, cantidad_fragmentos):

        self.cantidad_fragmentos = cantidad_fragmentos
        return self

    # ------------------------------------------------------------------------------------------------------------------

    def set_promedio_tamanho(self, promedio_tamanho):

        self.promedio_tamanho = promedio_tamanho
        return self

    # ------------------------------------------------------------------------------------------------------------------

    def set_desviacion_estandar(self, desviacion_estandar):

        self.desviacion_estandar = desviacion_estandar
        return self

    # ------------------------------------------------------------------------------------------------------------------

    def set_rango_traslape(self, rango_traslape):

        self.rango_traslape = rango_traslape
        return self

    # ------------------------------------------------------------------------------------------------------------------

    def calcular_rango(self):

        minimo = self.promedio_tamanho - self.desviacion_estandar
        maximo = self.promedio_tamanho + self.desviacion_estandar
        return minimo, maximo

    # ------------------------------------------------------------------------------------------------------------------

    def generar_fragmentos(self, texto):

        frags = []
        i = 0
        frags = self.obtener_fragmentos(i, texto, frags)

        while len(frags) < self.cantidad_fragmentos:
            i = np.random.randint(0, len(frags))
            frags = self.obtener_fragmentos(i, texto, frags)

        return frags

    # ------------------------------------------------------------------------------------------------------------------

    def obtener_fragmentos(self, i, texto, fragmentos):

        rango = self.calcular_rango()

        while i < len(texto):
            tamanno = np.random.randint(rango[0], rango[1])
            frag = ""
            cont = 0
            traslape = np.random.randint(self.rango_traslape[0], self.rango_traslape[1])

            if i > traslape :
                i -= traslape

            while cont < tamanno and i < len(texto):
                frag = frag + texto[i]
                i += 1
                cont += 1

            fragmentos.append(frag)

            if len(fragmentos) == self.cantidad_fragmentos:
                break

        return fragmentos

# ----------------------------------------------------------------------------------------------------------------------
