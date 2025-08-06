# Análisis del Boston Housing Dataset

Este proyecto utiliza el dataset de viviendas de Boston para realizar un análisis básico de regresión lineal utilizando Python. Se descarga el conjunto de datos desde el repositorio original de CMU y se analiza la relación entre el número promedio de habitaciones por vivienda y el valor mediano de las viviendas.

## 📊 ¿Qué hace este script?

1. Descarga y procesa los datos del dataset de Boston desde:
   [https://lib.stat.cmu.edu/datasets/boston](https://lib.stat.cmu.edu/datasets/boston)
2. Convierte los datos en un DataFrame de `pandas` con 14 variables.
3. Utiliza regresión lineal por mínimos cuadrados ordinarios (MCO) para modelar la relación entre:
   - `RM`: Número promedio de habitaciones por vivienda
   - `MEDV`: Valor mediano de viviendas ocupadas por propietarios (en miles de USD)
4. Genera un gráfico de dispersión con la recta de regresión ajustada.

pip install -r requirements.txt

🧑‍💻 Autor

Desarrollado por Gus como parte de su aprendizaje en Python e IA.
