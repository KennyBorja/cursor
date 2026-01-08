import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("libro1.csv", delimiter=";", header=None)

media = datos[0].mean()
mediana = datos[0].median()
desviacion = datos[0].std()
print(f"Columna 1 - Media: {media}, Mediana: {mediana}, Desviación: {desviacion}")

media = datos[1].mean()
mediana = datos[1].median()
desviacion = datos[1].std()
print(f"Columna 2 - Media: {media}, Mediana: {mediana}, Desviación: {desviacion}")

plt.scatter(datos[0], datos[1])
plt.show()