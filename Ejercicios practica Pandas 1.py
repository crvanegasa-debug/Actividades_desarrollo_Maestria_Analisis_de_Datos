# %% #Ejercicios practica Pandas 1
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv"
data = pd.read_csv(url)

data = data.rename(columns={'Tax 5%': 'Tax',
 'Cost of goods sold': 'Cogs',
 'Gross margin percentage': 'Gross margin pct',
 'Customer stratification rating': 'Rating'})
data.columns = (data.columns
 .str.strip()
 .str.lower()
 .str.replace(' ', '_'))

# %%
# 1 Dimensiones del DataFrame BÁSICO
# Complete la instrucción para conocer el número de filas y de columnas.
# print(data.___)
print(data.shape)
#Respuesta breve: ¿cuál de los dos números corresponde a los registros y cuál a las variables?
# el 1000 corresponde a la cantidad de filas y los 17 a las variables de columnas

# %%
# 2. Columnas, tipos y primeras filas 
print(data.columns)
print(data.dtypes)
data.head(3)

#  %%
#3.Seleccionar varias columnas
resultado = data[["invoice_id", "product_line", "total"]]
resultado.head()
print(resultado)   

# %%
#4.¿Series o DataFrame?
print(type(data['total']))
print(type(data[['total']]))
# en un solo corchete solo trae dtos, con el doble corchete trae como una tabla,
# con su nombre de tabla.


# %%
#5.loc y iloc sobre la misma celda
print(data.loc[7, 'product_line'])
print(data.iloc[7, 5])
# De acuerdo a los ejercicios y actividades que se desarrollaron el iloc, maneja 
# posicion para traer datos, es decir que la persona debe conocer extactamente que
# es lo que quiere visualizar, y si hay un nuevo orden o modificacion de la tabla 
# traera lo que alli se encuentre en esta nueva posicion, en comparacion con el LOC
# que busca con nombre de columna.


# %%
#6. Una sola condición
mascara = data['quantity'] >8
resultado = data[mascara]
print(resultado.shape[0])

# %%
# 7.Dos condiciones al tiempo
mascara = (data['branch'] == 'C' ) & (data['total'] > 300)
resultado = data[mascara]
print(resultado.shape)

# %%
# 8. Corregir un filtro por categorías 
# Instruccion incorrecta:
# mascara = data['product_line'] == 'Food and beverages'
# or 'Fashion accessories'
mascara = data['product_line'].isin(['Food and beverages', 'Fashion accessories'])
print(data[mascara].shape[0])

# %%
#9.Rango de valores y columnas elegidas 
mascara = (data['branch'].isin(['A', 'C'])) & (data['total'].between(200, 500))
resultado = data.loc[mascara, ['branch','product_line','quantity','total']]
resultado.head()
print(mascara)
print(resultado)
# Pandas extrae los datos que necesitamo de una sola vez, sin nesecidad de dos 
# (data['branch'] == 'A') | (data['branch'] == 'C')


# %%
#10.Valor de cada unidad vendida 
data['valor_unitario'] = data['total'] / data['quantity']
print(data['valor_unitario'].head(3).round(2))

# %%
#11.Clasificar cada venta
data['tipo_compra'] = np.where(data['quantity'] >= 6, 'volumen', 'menor')
print(data['tipo_compra'].value_counts())
# Lo que hace es etiquetar o clasificar cada una de las filas del DataFrame
# según se cumpla o no la condición

# %%
#12. ¿Cuánto ingreso genera cada sucursal?
resumen = (data
.groupby('branch')['total']
.sum())
print(resumen.round(2))


# %%
#13.¿Cuántas facturas registra cada método de pago?
resumen = (data
.groupby('payment')['invoice_id']
.count())
print(resumen)
# Cada fila del resultado representa un método de pago único junto con el 
# número total de facturas procesadas con ese método

# %%
#14.Varias métricas por método de pago 
resumen = (
data
.groupby('payment')
.agg(facturas=('invoice_id', 'size'),
unidades=('quantity', 'sum'),
ingreso=('total', 'sum'),)
.reset_index())
print(resumen.round(2))
print(resumen.loc[resumen['ingreso'].idxmax()]) #mayor ingreso
print(resumen.loc[resumen['ingreso'].idxmax(), 'payment'])
print(resumen.sort_values('ingreso', ascending=False))

# %%
#15. Agregar la zona de cada sucursal 
sucursales = pd.DataFrame({
    'branch': ['A', 'B', 'C'],
    'zona': ['Centro', 'Norte', 'Sur']
})

resultado = data.merge(
    sucursales,
    on='branch',
    how='left')

print(resultado.shape)
resultado[['branch', 'city', 'zona', 'total']].head()
# %%
# %%
# 16. La sucursal líder entre los clientes Member
# 1. Filtrar las ventas de clientes Member
mascara_member = data['customer_type'] == 'Member'
ventas_member = data[mascara_member]

# 2. Agrupar por sucursal: número de facturas e ingreso total
resumen_member = (
    ventas_member
    .groupby('branch')
    .agg(
        facturas=('invoice_id', 'count'),
        ingreso=('total', 'sum')
    )
    .reset_index()
)

# 3. Calcular la columna ticket_promedio
resumen_member['ticket_promedio'] = resumen_member['ingreso'] / resumen_member['facturas']

# 4. Ordenar de mayor a menor ingreso
resultado_final = resumen_member.sort_values(by='ingreso', ascending=False)

# Mostrar el resultado redondeado a 2 decimales
print(resultado_final.round(2))
#
# %%
