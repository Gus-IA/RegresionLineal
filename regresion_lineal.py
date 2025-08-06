import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

# descargar los datos desde la URL
url = "https://lib.stat.cmu.edu/datasets/boston"
raw_data = requests.get(url).text

# procesar el texto
# El archivo tiene las 13 variables en un formato raro: cada observación está en 2 líneas
lines = raw_data.split('\n')[22:]  # Saltamos encabezados

# cada observación usa dos líneas: la primera tiene 6 números, la segunda tiene 8
data = []
for i in range(0, len(lines) - 1, 2):
    try:
        line1 = list(map(float, lines[i].split()))
        line2 = list(map(float, lines[i+1].split()))
        row = line1 + line2
        data.append(row)
    except:
        continue  # Evita errores por líneas vacías

# crear el DataFrame
columns = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE",
           "DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"]
df = pd.DataFrame(data, columns=columns)

# formula minimizar el error cuadrático medio (MCO): $\beta = (X^{T}X)^{-1}X^{T}Y$

# mostramos el gráfico con el precio medio y el número medio de habitaciones por vivienda
X = np.array(df["RM"])
Y = np.array(df["MEDV"])

plt.scatter(X, Y, alpha=0.3)

# añadimos la columna de 1s para término independiente
X = np.array([np.ones(506), X]).T

# la fórmula del error cuadrático medio
B = np.linalg.inv(X.T @ X) @ X.T @ Y

# pintamos la línea en los valores añadidos y de color rojo
plt.plot([4, 9], [B[0] + B[1] * 4, B[0] + B[1] * 9], c="red")
plt.show()