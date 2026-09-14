# %% Ejecucion de codigo por celdas Python
print("hola")

# %%  prueba de metodos de modificar listas
compras=["pan","leche"]

compras.append("huevos")
print(compras)
# ["pan", "leche", "huevos"]

compras.insert(0,"cafe")
compras.remove("leche")
print(compras)
# ['cafe', 'pan', 'huevos']

ultimo=compras.pop()
print(ultimo)
# huevos
print(compras)
# ["cafe", "pan"]

# %% Recorrer una lista con for
precios=[1200,950,3400]

# 1. Por elemento
for p in precios:
    print(p)

# 2. Por índice
for i in range(len(precios)):
    print(i, precios[i])
    
# EL 2 Y 3 buscan el mismo objetivo, pero mas entendible, rapido y fail es
# el enumerate, ya q pide la posicion y el valor. el otro pide recorrer con
# range las posiciones y luego mostrar el resultado

# 3. Con enumerate
for i, p in enumerate(precios):
    print(i, p)

# %% Tuplas: inmutables por diseño

colores_rgb=(255,128,0)
coordenada=(4.5,-2.1)

print(colores_rgb[1])
# 128
print(len(coordenada))
# 2

# Se puede recorrer igual que una lista
for c in colores_rgb:
    print(c)

# Tupla de un solo elemento: la coma es obligatoria
unica=(7,)
print(unica[0])

# %% Recorrer un diccionario

stock={"pan":12,"leche":5,"cafe":8}

for clave in stock:
    print(clave)

for valor in stock.values():
    print(valor)

for clave, valor in stock.items():
    print(clave, "->", valor)

# %% Cuál será la salida del siguiente código
datos={"a":[1,2],"b":[3]}

datos["a"].append(9)
datos["c"]=[4,5]

for clave,lista in datos.items():
    print(clave,len(lista))
# len es utilizado para medir o cuantificar la dimension de la lista o tupla o diccionario
# ejemplo en a hay 3 valores, en b hay uno solo y en c hay dos
# %% Inventario con listas y diccionarios

productos=[
{"nombre":"pan","precio":3500},
{"nombre":"leche","precio":4200},
{"nombre":"cafe","precio":12800}
]

total=0
caro=productos[0]

for p in productos:
    total = total + p["precio"]
if p["precio"] > caro["precio"]:
    caro = p

print("Total:", total)
print("Mas caro:", caro["nombre"])

# %%
