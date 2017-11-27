# ----------------------------------------------------------------------------------------------------------------------

from model.alg_shotgun import *
from model.alg_errores import *
from model.dao_shotgun import *

# ----------------------------------------------------------------------------------------------------------------------
# Abrir el archivo, sustituir saltos de linea por espacios

dao_shotgun = DAOShotgun()
texto = dao_shotgun.abrir_archivo(nombre_archivo="../files/entrada.txt")

# ----------------------------------------------------------------------------------------------------------------------
# Generacion de fragmentos

alg_shotgun = AlgShotgun()\
    .set_cantidad_fragmentos(5)\
    .set_promedio_tamanho(8)\
    .set_desviacion_estandar(4)\
    .set_rango_traslape((1,3))

fragmentos = alg_shotgun.generar_fragmentos(texto)
print("Fragmentos sin errores: \n" + str(fragmentos))

# ----------------------------------------------------------------------------------------------------------------------
# Agregar errores a los fragmentos

alg_errores = AlgErrores(texto, fragmentos)

fragmentos = alg_errores.aplicar_errores(porcentaje=50, funcion=alg_errores.sustitucion)
print("Fragmentos con sustituciones: \n" + str(fragmentos))

fragmentos = alg_errores.aplicar_errores(porcentaje=50, funcion=alg_errores.delecion)
print("Fragmentos con deleciones: \n" + str(fragmentos))

fragmentos = alg_errores.aplicar_errores(porcentaje=50, funcion=alg_errores.insercion)
print("Fragmentos con inserciones: \n" + str(fragmentos))

# ----------------------------------------------------------------------------------------------------------------------
