
import os
import sys

from util.file import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("qt_ui.ui", self)
        self.show()
        self.assign_functions()
        self.statusbar.setText("Bienvenido")

    def assign_functions(self):
        self.btnColeccion.clicked.connect(self.btn_coleccion_clicked)
        self.btnFragmentos.clicked.connect(self.btn_fragmentos_clicked)
        self.btnAbrirFuente.clicked.connect(self.btn_abrir_fuente_clicked)
        self.btnAbrirDestino.clicked.connect(self.btn_abrir_destino_clicked)

    def btn_coleccion_clicked(self):
        self.statusbar.setText("Colección de archivos de fragmentos generada")

    def btn_fragmentos_clicked(self):
        self.statusbar.setText("Archivo de fragmentos generado")

    def btn_abrir_fuente_clicked(self):
        open_dialog = QFileDialog()
        filename = open_dialog.getOpenFileName(self, "Abrir archivo", "/home")[0]
        if filename is not "":
            self.statusbar.setText("Archivo seleccionado: " + os.path.split(filename)[1])
            self.txtFuente.setText(filename)

    def btn_abrir_destino_clicked(self):
        open_dialog = QFileDialog()
        dirname = str(open_dialog.getExistingDirectory(self, "Abrir directorio"))
        if dirname is not "":
            self.statusbar.setText("Directorio seleccionado: " + os.path.split(dirname)[1])
            self.txtDestino.setText(dirname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

