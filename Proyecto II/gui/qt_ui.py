# ----------------------------------------------------------------------------------------------------------------------

import os
import sys
import subprocess

from PyQt5 import uic
from PyQt5.QtWidgets import *

from model.alg_shotgun import *
from model.alg_errores import *
from model.dao_shotgun import *

# ----------------------------------------------------------------------------------------------------------------------


class MainWindow(QMainWindow):

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("qt_ui.ui", self)
        self.show()
        self.assign_functions()
        self.set_default_options()
        self.statusbar.setText("Bienvenido")

    # ------------------------------------------------------------------------------------------------------------------

    def assign_functions(self):
        self.btnColeccion.clicked.connect(self.btn_coleccion_clicked)
        self.btnFragmentos.clicked.connect(self.btn_fragmentos_clicked)
        self.btnAbrirFuente.clicked.connect(self.btn_abrir_fuente_clicked)
        self.btnAbrirDestino.clicked.connect(self.btn_abrir_destino_clicked)

    # ------------------------------------------------------------------------------------------------------------------

    def btn_coleccion_clicked(self):
        self.statusbar.setText("Colección de archivos de fragmentos generada")

    # ------------------------------------------------------------------------------------------------------------------

    def set_default_options(self):

        self.txtFuente.setText("../files/entrada.txt")
        self.txtDestino.setText("../files/")
        self.txtNombre.setText("salida")

        self.spinCantidad.setValue(50)
        self.spinLongitud.setValue(6)
        self.spinDesviacion.setValue(2)

        self.spinTraslapeMinimo.setValue(1)
        self.spinTraslapeMaximo.setValue(8)

    # ------------------------------------------------------------------------------------------------------------------

    def btn_fragmentos_clicked(self):

        descripcion = self.extraer_informacion_procesamiento()
        fragmentos = self.ejecutar_algoritmos(descripcion)

        archivo_fragmentos, archivo_descriptivo = self.guardar_archivos_obtenidos(fragmentos, descripcion)
        self.mostrar_archivos_obtenidos(archivo_fragmentos, archivo_fragmentos)

        self.statusbar.setText("Archivo de fragmentos generado como " + archivo_fragmentos)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_algoritmos(self, params):

        dao_shotgun = DAOShotgun()
        texto = dao_shotgun.abrir_archivo_fragmentos(params["archivo"])

        alg_shotgun = AlgShotgun(params)
        fragmentos = alg_shotgun.generar_fragmentos(texto)

        alg_errores = AlgErrores(texto, fragmentos)
        fragmentos = alg_errores.agregar_errores(params["errores"])

        return fragmentos

    # ------------------------------------------------------------------------------------------------------------------

    def extraer_informacion_procesamiento(self):

        return {
            "archivo": self.txtFuente.text(),
            "cantidad_fragmentos": self.spinCantidad.value(),
            "promedio_tamanho": self.spinLongitud.value(),
            "desviacion_estandar": self.spinDesviacion.value(),
            "rango_traslape": (self.spinTraslapeMinimo.value(), self.spinTraslapeMaximo.value()),
            "errores": self.extraer_probabilidades_errores()
        }

    # ------------------------------------------------------------------------------------------------------------------

    def extraer_probabilidades_errores(self):

        return {
            "sustituciones": self.spinSustitucion.value(),
            "inserciones": self.spinInsercion.value(),
            "deleciones": self.spinDelecion.value(),
            "inversiones": self.spinInversion.value(),
            "quimeras": self.spinQuimeras.value()
        }

    # ------------------------------------------------------------------------------------------------------------------

    def guardar_archivos_obtenidos(self, fragmentos, descripcion):

        archivo_fragmentos = os.path.join(self.txtDestino.text(), self.txtNombre.text() + ".txt")
        archivo_descriptivo = os.path.join(self.txtDestino.text(), self.txtNombre.text() + ".json")

        dao_shotgun = DAOShotgun()
        dao_shotgun.guardar_archivo_fragmentos(fragmentos, archivo_fragmentos)
        dao_shotgun.guardar_archivo_descriptivo(descripcion, archivo_descriptivo)

        ap = lambda x: os.path.abspath(x)
        return ap(archivo_fragmentos), ap(archivo_descriptivo)

    # ------------------------------------------------------------------------------------------------------------------

    def mostrar_archivos_obtenidos(self, *archivos):

        for archivo in archivos:
            os.popen(archivo)

    # ------------------------------------------------------------------------------------------------------------------

    def btn_abrir_fuente_clicked(self):

        open_dialog = QFileDialog()
        filename = open_dialog.getOpenFileName(self, "Abrir archivo", "../files")[0]
        if filename is not "":
            self.statusbar.setText("Archivo seleccionado: " + os.path.split(filename)[1])
            self.txtFuente.setText(filename)

    # ------------------------------------------------------------------------------------------------------------------

    def btn_abrir_destino_clicked(self):

        open_dialog = QFileDialog()
        dirname = str(open_dialog.getExistingDirectory(self, "Abrir directorio"))
        if dirname is not "":
            self.statusbar.setText("Directorio seleccionado: " + os.path.split(dirname)[1])
            self.txtDestino.setText(dirname)

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# ----------------------------------------------------------------------------------------------------------------------
