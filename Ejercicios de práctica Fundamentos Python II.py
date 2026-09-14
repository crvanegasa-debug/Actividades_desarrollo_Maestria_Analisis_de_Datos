# %% 1. Crear una lista de notas BÁSICO
# Complete la lista con cinco notas y muestre la cantidad de elementos.

notas = [3.5,3.9,4.2,4.5,1.5]
print(len(notas))
print(notas)
#5
# [3.5, 3.9, 4.2, 4.5, 1.5]

# %% Acceder por índice
# Use índices para imprimir la primera, la tercera y la última temperatura.

temperaturas = [18, 20, 19, 21, 22]
print(temperaturas[0])
print(temperaturas[2])
print(temperaturas[4])

# %% Actualizar un elemento BÁSIC
# Corrija la segunda venta, que fue registrada como 80 pero debía ser 85.

ventas = [120, 80, 200, 50]
ventas[1] = 85
print(ventas)

# %% Agregar y extraer datos BÁSICO

#Agregue una nueva nota y extraiga la última nota registrada.
notas = [3.5, 4.0, 2.8]
notas.append(4.6)
ultima = notas.pop(3)
print(ultima)
print(notas)


# %% Calcular promedio
# Complete el acumulador para calcular el promedio de una lista.
notas = [4.2, 3.8, 5.0, 2.9]
total = 0
for nota in notas:
 total = total + nota
promedio = total / len(notas)
print(round(promedio, 2))
# %% Contar aprobados
#Cuente cuántas notas son mayores o iguales a 3.0
notas = [4.2, 2.5, 3.0, 1.8, 4.7]
aprobados = 0
for nota in notas:
 if nota >= 3.0:
    aprobados = aprobados + 1
print(aprobados)

# %% Filtrar valores válidos
#Construya una lista con las temperaturas que estén entre -10 y 50 grados
lecturas = [18, 200, 21, -99, 19, 22]
validas = []
for t in lecturas:
 if t >= -10 and t <= 50:
    validas.append(t)
print(validas)

# %% Ordenar sin perder el original 
# Use sorted() para crear una lista ordenada sin modificar 
# la lista inicial.
montos = [120000, 85000, 210000, 50000]
ordenados = sorted(montos)
print(montos)
print(ordenados)

# %% Comprensión de listas
#Complete la comprensión para obtener los cuadrados de 
# los números pares.
numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrados_pares)

# %% Lista anidada
# Complete el doble ciclo para sumar todos los elementos de una 
# matriz.
matriz = [[1, 2, 3], [4, 5, 6]]
total = 0
for fila in matriz:
 for valor in fila:
    total += valor
print(total)
# Desde mi punto de vista una matriz puede tener varias filas y columnas 
# Esta matrix es de 2 filas y 3 columnas (3 dimensiones en cada fila)
# y se entiende que primero recorremos las filas con el for de la matriz 
# trayendo los numeros en el ciclo, 1,2,3,4,5,6 y el valor lo entiendo
# que valores hay o trajo de ese recuento de filas y despues lo suma

# %% Crear una tupla fija
# Defina una tupla con la latitud y la longitud de una sede.
ubicacion = (10.5, 20.5)
print(ubicacion)
print(type(ubicacion))

# %% Desempaquetar una tupla 
# Asigne los elementos de la tupla a variables con nombres 
# significativos.
registro = ("A01", "Laura", 4.6)
salon, nombre, nota = registro
print(nombre)
print(nota)


# %% Tupla de un solo elemento
# Complete la sintaxis correcta de una tupla que contiene un solo
# código.
codigo = ("A01",)
print(codigo)
print(type(codigo))

# %%  Convertir lista a tupla 
columnas = ["fecha", "monto", "cliente"]
columnas_fijas = tuple(columnas)
print(columnas_fijas)

# %% Retorno múltiple
# Complete una función que retorne el mínimo y el máximo como una tupla implícita.
def resumen(valores):
 menor = min(valores)
 mayor = max(valores)
 return mayor, menor
minimo, maximo = resumen([8, 3, 10, 5])
print(minimo, maximo)

# %% Reconocer inmutabilidad
#Ejecute mentalmente el código y explique qué error se produce.
punto = (10, 20)
punto[0] = 99
print(punto)
# Pues por los corchetes se sabe que es una tupla, y ella no deja 
# modificar los valores dentro de variable, es decir que tratar de colocar el
# 99 o asignarlo a la posicion 0 no va a dejar, desconozco el error
# que arroje pero si tendra falla o error al ejecutar este codigo

# %%  Tupla como clave
# Use una tupla como clave para almacenar una lectura por coordenada.
lecturas = {}
coordenada = (4.65, -74.05)
lecturas[coordenada] = 18.5
print(lecturas[(4.65, -74.05)])

# %% Combinar listas con zip
# Cree pares estudiante-nota usando zip() y conviértalos a lista.
nombres = ["Ana", "Luis", "Marta"]
notas = [4.2, 3.8, 5.0]
pares = list(zip(nombres, notas))
print(pares)

# %% C. Diccionarios
# Crear un diccionario 
# Complete las claves necesarias para representar a un estudiante.
estudiante = {"codigo": "A01",  "nombre": "Laura",  "nota ": 4.6}
print(estudiante)

# %% Acceso seguro con get()
# Use get() para consultar una clave que podría no existir.
cliente = {"nombre": "Carlos", "puntaje": 720}
saldo = cliente.get("saldo", 0)
print(saldo)

# %% Actualizar valores 
# Actualice el stock de un producto después de una venta de 3 unidades.
producto = {"codigo": "P01", "stock": 8}
producto["stock"] = producto["stock"] - 3
print(producto["stock"])

# %% Recorrer pares clave-valor 

