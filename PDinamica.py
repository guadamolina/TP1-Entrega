from funciones_auxiliares import *

#función auxiliar solo para programación dinámica
def minimo(superdict, x: int, largo_y, k: int):
  min = 10e10
  y_ultima: int = 0
  for y in range(largo_y): #dado que sabemos que la solución óptima está en el diccionario guardada con la clave x=len(grilla_x)-1 y breakpoints=(breakpoints pedidos)-1, busca la mínima por todo el rango y.
    if superdict[(x, y, k)][0] < min:
      min = superdict[(x, y, k)][0]
      y_ultima = y
  return min, superdict[(x, y_ultima, k)][1], y_ultima


def breakpointsAuxPD(breakpoints, grillax, grillay, superdiccionario, npuntos):

  #Cargamos los errores de los primeros puntos, de esta manera vamos a poder caclcular el minimo de crear una línea entre el breakpoint anterior y el próximo que resulte en el error mínimo. Es para cuando ponemos un 2ndo breakpoint.
  reconstruir_aux = []
  for y in range(len(grillay)):
    errorInicial = abs(npuntos[1][0] - grillay[y])
    superdiccionario[(0, y, 0)][0] = errorInicial
  a = 0
  b = 0
  for k in range(1, breakpoints):
    for x in range(1, len(grillax)):
      for y in range(len(grillay)):
        min_error = 1e10
        for xi in range(0, x):
          for yi in range(len(grillay)):
            error_aux = error((grillax[xi], grillay[yi]), (grillax[x], grillay[y]), npuntos)
            error_total = error_aux + superdiccionario[(xi, yi, k - 1)][0]
            if error_total < min_error:
              min_error, a, b = error_total, xi, yi
              reconstruir_aux = superdiccionario[(xi, yi, k - 1)][1]
          superdiccionario[(x, y, k)] = [min_error, reconstruir_aux[:] + [(a, b)]]

  #reconstruir_aux[x,y,k] = (xi, yi)
  #Buscamos el mínimo del superdiccionario. Sabemos que el mínimo optimo tiene que estar en la posición x = len(grillax)-1 ya que si o si debe haber un breakpoint en la ultima posicion de la grillax. Además, sabemos que ese valor debe estar en breakpoints-1 (el -1 ya que consideramos breakpoints como posiciones) dentro del diccionario ya que significa que es el valor donde tengo todos mis breakpoints y también estoy al final de la grilla x. Entonces solo debemos iterar en las ys para encontrar cuál es la que contiene el ultimo breakpoint.

  posiciones_solucion = minimo(superdiccionario,len(grillax) - 1, len(grillay), breakpoints - 1)
  solucion = []

  for elem in posiciones_solucion[1]:

    solucion.append((grillax[elem[0]], grillay[elem[1]]))

  solucion.append((grillax[-1], grillay[posiciones_solucion[2]]))

  return posiciones_solucion[0], solucion

#esta función llena todas las posiciones que vamos a usar del diccionario con un error muy grande y listas vacias
def inicializar(breakpoints: int, m1: int, m2: int):
  superdiccionario = {}
  inf: float = 10e10
  for k in range(breakpoints):
    for i in range(m1):
      for j in range(m2):
        superdiccionario[(i, j, k)] = [inf, []]
  return superdiccionario


def breakpointsPD(archivo: str, breakpoints: int, m1: int, m2: int):
  puntosEnX: List[float] = leer_datos(archivo)[0]
  puntosEnY: List[float] = leer_datos(archivo)[1]
  grilla_x: List[float] = armar_grilla(puntosEnX, puntosEnY, m1, m2)[0]
  grilla_y: List[float] = armar_grilla(puntosEnX, puntosEnY, m1, m2)[1]
  superdiccionario = inicializar(breakpoints, m1, m2)

  return breakpointsAuxPD(breakpoints, grilla_x, grilla_y, superdiccionario,
               (puntosEnX, puntosEnY))
