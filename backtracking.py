from funciones_auxiliares import *

def breakpointshackerBT(archivo:str,breakpoints:int,x:int,y:int,grilla_x,grilla_y,npuntos,solucion:list[tuple[float,float]],optima:list[tuple[float,float]],errorMinimo:float):
   error_parcial = errorSolucion(solucion,npuntos)
   #Poda para ver si no contiene a la grilla_x[0] en la solución luego de la primera iteracion
   #Poda por factibilidad
   if (len(solucion)==1) and (grilla_x[0] not in lista_x(solucion)):
       return errorMinimo, optima
   
   #si tengo una solucion factible y con la cantidad de breakpoints adecuada, se fija si tiene menor error que la ultima calculada como óptima. Si es mejor, optima se actualiza.
   elif (breakpoints==0 and x==len(grilla_x)):
        if (error_parcial<errorMinimo):
            optima=solucion.copy()
            errorMinimo=error_parcial
        return errorMinimo, optima
    
   #Si el error de la solucion sin terminar es mayor que el de la optima, no sigue completando esa solución.
   #Poda por optimalidad
   elif(error_parcial>errorMinimo):
      return errorMinimo, optima
    
    #Si tengo mas breakpoints que poner que puntos disponibles en X, no sigo completando la solucion
   elif(breakpoints > len(grilla_x)-x ):
      return errorMinimo, optima
    
   #Este if es para que no repita puntos de x
   elif x<len(grilla_x)and grilla_x[x] in lista_x(solucion):
       return errorMinimo, optima
   
   #para que no haya soluciones que no lleguen al punto final
   elif (breakpoints==0 and x!=len(grilla_x)):
        return errorMinimo, optima
   #para que no haya soluciones con menos puntos que los pedidos
   elif(breakpoints!=0 and x==len(grilla_x)):
       return errorMinimo, optima

  
   for j in range(0,len(grilla_y)+1):
       if j==len(grilla_y):
            errorMinimo,optima=breakpointshackerBT(archivo,breakpoints,x+1,j,grilla_x,grilla_y,npuntos,solucion,optima,errorMinimo)
       else:
        errorMinimo,optima=breakpointshackerBT(archivo,breakpoints-1,x+1,j,grilla_x,grilla_y,npuntos,solucion+[(grilla_x[x],grilla_y[j])],optima,errorMinimo)
    
   return errorMinimo,optima

def breakpointsBT(archivo:str,breakpoints:int,m1:int,m2:int):
    puntosEnX:list[float]=leer_datos(archivo)[0]
    puntosEnY:list[float]=leer_datos(archivo)[1]
    grilla_x:list[float]=armar_grilla(puntosEnX,puntosEnY,m1,m2)[0]
    grilla_y:list[float]=armar_grilla(puntosEnX,puntosEnY,m1,m2)[1]
    error:float=10e10

#llamamos a una funcion auxiliar que va a usar atributos adicionales además de los que el usuario ingresa
   

    return breakpointshackerBT(archivo,breakpoints,-1,-1,grilla_x,grilla_y,(puntosEnX,puntosEnY),[],[],error)
