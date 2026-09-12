# %%
# 1. La función se crea una vez y se usa muchas veces
# Definir una función 
# Complete la palabra clave que define una función.
def saludar():
 print("Hola")
saludar()

# %%
#2. Llamar a la función BÁSICO
#Complete la línea que ejecuta la función ya definida.
def bienvenida():
 print("Bienvenido al curso")
bienvenida()

# %%
# 3.Predice el orden de ejecución BÁSICO
#Sin ejecutar, determine en qué orden aparecen los mensajes.
def uno():
 print("A")
print("B")
uno()
print("C")
# Se define la funcion uno, que todavia no tiene algo por proceder o calcular, pero que
# cuando llame a la funcion uno debe imprimir o mostrar "A". Deduciendo esto el codigo
# esta diciendo imprima B luego imprima la funcion uno que es A y luego imprima C


# %%
# 4. Corrige el orden INTERMEDIO
# El programa falla porque la función se llama antes de existir. Reescriba el bloque completo
#en el orden correcto.
#saludar("Ana")
#def saludar(nombre):
#print("Hola,", nombre)
#Correcion
def saludar(nombre):
 print("Hola,", nombre)
saludar("Ana")

# %%
# 5 Función con un parámetro
# Complete el parámetro que recibe la función.
def saludar(nombre):
 print("Hola,", nombre)
saludar("Ana")

# %%
# 6 Función con dos parámetros 
# Complete los parámetros necesarios para calcular el área.
def area(base, altura):
 return base * altura
print(area(3, 4))

# %%
# 7 Completa la llamada 
# Complete los argumentos para obtener exactamente el resultado
# indicado.
def area(base, altura):
 return base * altura
print(area(5,5)) # 25.0

# %%
# 8 Reutilizar la misma función 
# Llame tres veces a la misma función con precios distintos.
def con_iva(precio):
 return precio * 1.19
print(con_iva(100000))
print(con_iva(52000))
print(con_iva(3900))

# %%
# 9 Parámetro o argumento 
# Observe la definición y la llamada, y distinga cada uno 
# de los dos nombres.
def doble(n):
 return n * 2
resultado = doble(5)

# Respuesta breve: ¿cuál es el parámetro y cuál es 
# el argumento?
# El argumento es la variable independiente o que se introduce
# y el parametro es la variable donde se guardara esa variable

# %%
# 10 Argumentos por posición 
# Complete la llamada para que se imprima: Ana 20 Bogota
def perfil(nombre, edad, ciudad):
 print(nombre, edad, ciudad)
perfil("Ana", 20 , "Bogota")

# %%
# 11 Argumentos por nombre 
# Complete los nombres de los parámetros para que el 
# orden deje de importar.
def perfil(nombre, edad, ciudad):
 print(nombre, edad, ciudad)
perfil(edad=20, nombre="Ana", ciudad="Bogota")

# %%
# 12 Valor por defecto 
# Complete el valor por defecto del parámetro saludo.
def saludar(nombre, saludo="buen dia"):
 print(saludo, nombre)
saludar("Ana")

# %%
#13 Reemplazar el valor por defecto 
# Complete el argumento que sustituye al saludo por defecto.
def saludar(nombre, saludo="Hola"):
 print(saludo, nombre)
saludar("Luis", "buen dia")

# %%
# 14 Orden de los parámetros 
# El siguiente encabezado produce un error. Reescriba la 
# definición completa de forma correcta.
def registrar(producto, cantidad="1"):
  print(producto, cantidad)
registrar("cable",)
 
# %%
#15 Una lista como argumento
# Complete el recorrido para sumar todos los precios
# recibidos.
def total(precios):
 suma = 0
  # Recorremos directamente cada elemento (precio) de la lista
 for p in precios:
  suma = suma + p
 return suma
print(total([1200, 950, 3400]))

# %%
# Lo que la función entrega al programa
#16 Devolver un valor 
# Complete la palabra clave que entrega el resultado.
def doble(n):
 return n * 2
print(doble(5))

# %%
# 17 Usar el valor devuelto 
# Complete la llamada para guardar el resultado y operar con él.
def doble(n):
 return n * 2
resultado = doble(6)
print(resultado + 1)

# %%
#18 Función sin return
#Sin ejecutar, determine qué imprimen las dos últimas líneas.
def saludo(nombre):
 print("Hola,", nombre)
x = saludo("Ana")
print(x)

#  imprimi primero Hola nombre   y despues debe imprimir "Ana" y 
# deberia imprimir x lo guardado en x.

# %%
# 19 print o return
# La suma falla. Corrija la función para que el resultado
# pueda seguir usándose y escriba la versión corregida.
def doble(n):
 return n * 2 
total = doble(5) + 3
print(total)

# %% 
# 20 return dentro de una condición
# Complete la instrucción que devuelve el segundo resultado.
def signo(n):
 if n < 0:
  return "negativo"
 return "positivo"
print(signo(-4))
print(signo(7))

# %%
# 21 return termina la función
# Sin ejecutar, determine qué se imprime y qué línea nunca se ejecuta.
def prueba(n):
 if n > 0:
  return "positivo"
 print("linea intermedia")
 return "otro"
print(prueba(5))
# Se ejecuta la linea prueba(5) mirando que la 5 e smayor que
# 0 da o entregara como resultado positivo, deteninedose hasta
#hay el codigo

# %%
#22 Devolver dos valores
# Complete la función para que entregue el mínimo y el máximo.
def resumen(valores):
 return min(valores), max(valores)
menor, mayor = resumen([8, 3, 10, 5])
print(menor, mayor)

# %%
# 22 Devolver dos valores 
# Complete la función para que entregue el mínimo y el máximo.
def resumen(valores):
 return min(valores), ___(valores)
menor, mayor = resumen([8, 3, 10, 5])
print(menor, mayor)

# %%
#23 Encadenar funciones 
#Complete la llamada interna para calcular el precio con IVA
# redondeado.
def con_iva(p):
 return p * 1.19
def redondear(valor):
 return round(valor, 2)
print(redondear(con_iva(1200)))


# %%
# 24 Variable local y global 
# Sin ejecutar, determine qué imprime cada una de las dos llamadas.
mensaje = "global"
def prueba():
 mensaje = "local"
 print(mensaje)
prueba()
print(mensaje)
# local , global, como se la primera llamada es print(mensaje)
#y hace referencia a la funcion def prueba es decri esta dentro de
#un primera burbuja, y cuando hacemos un segundo llamdo con
# print, esta buscando la variable mensaje por fuera de 
# esa primera burbuja o definicion

# %% 25 Evitar las variables globales 
# Reescriba la función para que reciba el IVA como parámetro
# y no dependa de una variable externa.
# iva = 0.19
#def con_iva(precio):
#return precio * (1 + iva)
def con_iva(precio, iva):
 return precio * (1+iva)
resultado = con_iva(1000,0.19)
print(resultado)

# %%
# 26 No modificar el original
# Complete la función para que devuelva una lista nueva sin alterar la
# que recibe.
def agregar(lista):
 nueva = lista + [3]
 return nueva
datos = [1, 2]
print(agregar(datos))
print(datos)

# %%
# 27 Función que recibe una lista
# Complete la función que calcula el promedio de una lista de notas.
def promedio(notas):
 total = 0
 for n in notas:
  total = total + n
 return total / len(notas)
print(promedio([3.5, 4.2, 2.8]))

# %%
# 28 Función que recibe un diccionario
# Complete las claves para mostrar el nombre y la nota del estudiante.
def describir(alumno):
 print(alumno["nombre"], alumno["nota"])
describir({"nombre": "Laura", "nota": 4.6})

# %%
#29 Función que devuelve una lista 
#Complete el método que agrega elementos y el valor que se devuelve.
def aprobados(estudiantes):
 resultado = []
 for e in estudiantes:
  if e["nota"] >= 3.0:
   resultado.append(e["nombre"])
 return resultado
datos = [{"nombre": "Ana", "nota": 4.2}, {"nombre": "Luis", "nota": 2.8}]
print(aprobados(datos))
# %%
# 30 Reporte de notas con funciones
# Complete el programa que calcula el promedio de un estudiante, decide si aprueba y
# muestra el reporte usando tres funciones.
def promedio(notas):
 total = 0
 for n in notas:
  total = total + n
 return total / len(notas)
def aprueba(prom, minimo = 3.6):
 return prom >= minimo
def reporte(nombre, notas):
 prom = promedio(notas)
 print(nombre, round(prom, 2))
 if aprueba(prom):
  print("Aprobado")
 else:
  print("No aprobado")
reporte("Laura", [3.5, 4.2, 2.8])
reporte("cris",[3.0, 2.2, 2.8])
# %%
