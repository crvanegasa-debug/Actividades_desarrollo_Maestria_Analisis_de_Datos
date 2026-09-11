# %%
# La función se crea una vez y se usa muchas veces
# Definir una función BÁSICO
# Complete la palabra clave que define una función.
def saludar():
 print("Hola")
saludar()

# %%
#Llamar a la función BÁSICO
#Complete la línea que ejecuta la función ya definida.
def bienvenida():
 print("Bienvenido al curso")
bienvenida()
# %%
#Predice el orden de ejecución BÁSICO
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
# Corrige el orden INTERMEDIO
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
