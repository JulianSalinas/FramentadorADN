# ----------------------------------------------------------------------------------------------------------------------

import os

from gui.shell import *
from util.bye import *
from util.file import *
from util.timem import *


# ----------------------------------------------------------------------------------------------------------------------


class GUI(Shell):

    # ------------------------------------------------------------------------------------------------------------------

    def run(self):

        print(Font.BOLD + Font.DARKCYAN + "\nOpciones disponibles: " + Font.END + Font.END)
        print("alineamiento, tablas, optimo, listar, val")
        print("match, mismatch, gap, recursos, ayuda, salir \n")

        print(Font.BOLD + Font.DARKCYAN +
              "Para mostrar información detallada "
              "sobre cada opción anteponga la palabra 'ayuda' " +
              Font.END + Font.END)

        print("Ejemplo: >> ayuda fragmentos \n")
        super().run()

    # ------------------------------------------------------------------------------------------------------------------

    def listar(self, args):

        """
        Lista todos los algoritmos implementados en el programa.
        """

        print("\n" + Font.BOLD + Font.PURPLE + "Algoritmos implementados" + Font.END + Font.END)
        algorithms = list(self.algoritms.keys())
        for i in range(len(algorithms)):
            print(str(i) + ". " + str(algorithms[i]))
        print("")

    # ------------------------------------------------------------------------------------------------------------------

    def ayuda(self, args):

        """
        Muestra la ayuda para una función o un conjunto de estas.
        Sintaxis: ayuda [ funcion_1, funcion_2, ... funcion_N ]
        """

        if len(args) == 0:
            self.ayuda(["alineamiento"])

        for arg in args:
            print(Font.BLUE + self.exec_help(arg) + Font.END)

    # ------------------------------------------------------------------------------------------------------------------

    def salir(self, args):

        """
        Se termina la ejecución del programa. Se muestra la cantidad de recursos utilizados durante la ejecución y la
        información de los autores.
        """

        self.recursos(["total"])
        print(bye)
        print(info)
        sys.exit(0)

    # ------------------------------------------------------------------------------------------------------------------

    def recursos(self, args):

        """
        Muestra el consumo actual de memoria y de tiempo. Si se especifíca la palabra 'totales' se mostrará la sumatoria
        de recursos utilizados durante la ejecución de lo contrario se mostrará el consumo del último algoritmo usado.
        """

        print("\n" + Font.BOLD + Font.PURPLE +
              "Recursos utilizados" +
              Font.END + Font.END)

        print("tiempo: %.10f segundos" % Timem.last_time)
        print("memoria: %s bytes\n" % str(Timem.last_memory_usage))

        if args.__contains__("totales"):

            print(Font.BOLD + Font.PURPLE +
                  "Sumatoria de recursos utilizados durante la ejecución" +
                  Font.END + Font.END)

            print("tiempo: %.10f segundos" % (time() - Timem.start_time))
            print("memoria: %s bytes \n" % str(Timem.total_memory_usage))

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    gui = GUI()
    gui.run()

# ----------------------------------------------------------------------------------------------------------------------

