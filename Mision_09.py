# Autor: Luis Humberto Burgueño Paz
# Ejercicios con listas.


# Recibe como parámetro una lista de valores enteros y regresa una nueva lista que contiene solo los valores pares.
def extraerPares(lista):
   listaPares =[]
   for dato in lista:
       if dato % 2 == 0:
           listaPares.append(dato)
   return listaPares


# Recibe como parámetro una lista y regresa una nueva con los valores que son mayores a un elemento previo.
def extraerMayoresPrevio(lista):
   valoresMayores = []
   for k in range(1, len(lista)):
       if lista[k] > lista[k-1]:
           valoresMayores.append(lista[k])
   return valoresMayores


# Recibe una lista de valores y regresa una nueva lista con cada pareja de datos intercambiada
def intercambiarParejas(lista):
   parejasIntercambiadas = []
   if len(lista) == 0:
       return parejasIntercambiadas
   if len(lista)%2!=0:
       for k in range(0, len(lista)-1, 2):
           parejasIntercambiadas.append(lista[k+1])
           parejasIntercambiadas.append(lista[k])
       parejasIntercambiadas.append(lista[-1])
       return parejasIntercambiadas
   if len(lista)%2 == 0:
       for k in range(0, len(lista), 2):
           parejasIntercambiadas.append(lista[k+1])
           parejasIntercambiadas.append(lista[k])
       return parejasIntercambiadas


# Recibe una lista de valores e intercambia el valor menor y mayor, suponiendo que son valores únicos.
def intercambiarMM(lista):
   if len(lista) < 2:
       lista = []
   else:
       menor = min(lista)
       mayor = max(lista)
       inicialMenor = lista.index(menor)
       inicialMayor = lista.index(mayor)
       lista[inicialMenor] = mayor
       lista[inicialMayor] = menor
   return lista


# Recibe una lista de valores enteros y regresa el promedio 'centro'.
def promediarCentro(lista):
   if len(lista) <= 2:
       return 0
   menor = min(lista)
   mayor = max(lista)
   listaPromedio = lista[::]
   listaPromedio.remove(menor)
   listaPromedio.remove(mayor)
   promedioCentro = sum(listaPromedio) // len(listaPromedio)
   return promedioCentro


# Recibe una lista de números y regresa una dupla con la media y la desviación estándar.
def calcularEstadistica(lista):
    n = len(lista)
    if n == 0:
        return 0, 0
    suma = 0
    suma2 = 0
    for dato in lista:
        suma += dato
    promedio = suma/n
    if n== 1:
        return promedio, 0
    for k in range(len(lista)):
        termino = (lista[k]-promedio)**2
        suma2 += termino
    desviacion = (suma2/(n-1))**0.5
    return promedio, desviacion


# Recibe una lista y regresa la suma de los valores de la lista sin considerar los números que estén al lado de un 13, o que sean 13.
def calcularSuma(lista):
    suma = 0
    if len(lista) == 0:
        return suma
    if len(lista) == 1 and lista[0] != 13:
        suma+=lista[0]
        return suma
    for k in range(1, len(lista)-1):
        if lista[k-1] != 13 and lista[k+1]!= 13 and lista[k] != 13:
            suma += lista[k]
            print(lista[k])
    if lista[0] != 13 and lista[1] != 13:
        suma += lista[0]
    if lista[-1]!= 13 and lista[-2] != 13:
        suma += lista[-1]
    return suma





