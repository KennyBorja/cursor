import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos_ventas.csv')

# Convierte la columna 'fecha' a tipo datetime
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad'] * d['precio']).sum())
ventas_por_mes = ventas_por_mes.sort_index()
print(ventas_por_mes)

ventas_por_mes.index = ventas_por_mes.index.astype(str)




df['ingresos'] = df['cantidad'] * df['precio']
ventas_por_producto = df.groupby('producto')[['cantidad', 'ingresos']].sum()


# 1. Crear la columna de ingresos
df['ingreso'] = df['cantidad'] * df['precio']

# 2. Agrupar todo de una vez (Lógica ganadora)
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
})

# 3. Extraer ganadores
mas_vendido = ventas_prod['cantidad'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()

# 4. Imprimir (usando tus f-strings que están perfectas)
print(f"Producto más vendido en unidades: {mas_vendido} ({ventas_prod.loc[mas_vendido, 'cantidad']} uds)")
print(f"Producto con mayores ingresos: {mayor_ingreso} ({ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f} €)")

plt.figure(figsize=(10, 6)) # Un poco más ancho para que quepan los meses
ventas_por_mes.plot(kind='bar', color='skyblue', edgecolor='black')

# 4. Personalización
plt.title("Total de Ingresos Mensuales (2025)", fontsize=14)
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Ingresos (€)", fontsize=12)
plt.xticks(rotation=45) # Rotamos las etiquetas para que no se amontonen
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 5. Guardar y mostrar
plt.savefig("ventas_por_mes.png")
plt.show()

# plot porductos mas vendidos
top5 = ventas_prod.nlargest(5, 'ingreso')
plt.figure(figsize=(6,4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos (€)")
plt.xlabel("Producto")
plt.tight_layout()
plt.savefig("top5_productos.png")
plt.show()

