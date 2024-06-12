import matplotlib.pyplot as plt
import numpy as np

# Ejemplo de datos de segmentos de línea (usaremos solo dos para simplicidad)
N = np.array([
    [-4, -3, -2, -4],
    [-2, -4, -2, -7],
])

# Dibujar cada línea
for segment in N:
    x_values = [segment[0], segment[2]]
    y_values = [segment[1], segment[3]]
    plt.plot(x_values, y_values)

# Mostrar el gráfico
plt.show()
