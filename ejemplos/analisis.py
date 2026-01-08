import pandas as pd
import matplotlib.pyplot as plt
#leer el archivo de datos delimitado por ;
datos = pd.read_csv("libro1.csv", delimiter=";", header=None)

#calcular media, mediana, desviación estándar por cada columna
#calculo de la primera columna (índice 0)
media = datos[0].mean()
mediana = datos[0].median()
desviacion = datos[0].std()
print(f"Columna 1 - Media: {media}, Mediana: {mediana}, Desviación: {desviacion}")
#calculo de la segunda columna (índice 1)
media = datos[1].mean()
mediana = datos[1].median()
desviacion = datos[1].std()
print(f"Columna 2 - Media: {media}, Mediana: {mediana}, Desviación: {desviacion}")

#grafico de dispersion de la columna 1 vs la columna 2
plt.scatter(datos[0], datos[1])
plt.show()