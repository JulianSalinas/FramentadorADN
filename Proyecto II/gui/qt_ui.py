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
        self.txtNombre.setText("salida.txt")

        self.spinCantidad.setValue(50)
        self.spinLongitud.setValue(6)
        self.spinDesviacion.setValue(2)

        self.spinTraslapeMinimo.setValue(1)
        self.spinTraslapeMaximo.setValue(8)

    # ------------------------------------------------------------------------------------------------------------------

    def btn_fragmentos_clicked(self):

        dao_shotgun = DAOShotgun()
        texto = dao_shotgun.abrir_archivo_fragmentos(self.txtFuente.text())

        alg_shotgun = AlgShotgun() \
            .set_cantidad_fragmentos(self.spinCantidad.value()) \
            .set_promedio_tamanho(self.spinLongitud.value()) \
            .set_desviacion_estandar(self.spinDesviacion.value()) \
            .set_rango_traslape((self.spinTraslapeMinimo.value(), self.spinTraslapeMaximo.value()))

        fragmentos = alg_shotgun.generar_fragmentos(texto)

        alg_errores = AlgErrores(texto, fragmentos)
        fragmentos = alg_errores.agregar_errores(
            self.spinSustitucion.value(),
            self.spinInsercion.value(),
            self.spinDelecion.value(),
            self.spinInversion.value(),
            self.spinQuimeras.value()
        )

        archivo_salida = os.path.join(self.txtDestino.text(), self.txtNombre.text())
        dao_shotgun.guardar_archivo(fragmentos, archivo_salida)

        archivo_salida = os.path.abspath(archivo_salida)
        os.popen(archivo_salida)

        self.statusbar.setText("Archivo de fragmentos generado como " + archivo_salida)

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
