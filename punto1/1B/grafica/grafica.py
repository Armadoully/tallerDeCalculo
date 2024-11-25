import math
from decimal import Decimal, getcontext, Overflow
import time
import csv
import matplotlib.pyplot as plt

# Configurar la precisión decimal
getcontext().prec = 50  # Ajusta la precisión según tus necesidades

# Iniciar el temporizador
start_time = time.time()

# Definir constantes
h = Decimal('6.626e-34')  # Constante de Planck
k = Decimal('1.38e-23')   # Constante de Boltzmann
t = Decimal("35e2")       # Temperatura
c = Decimal('3.1e8')      # Velocidad de la luz

# Calcular constantes
c2 = pow(c, 2)
constantes = 2 * h / c2  # parte de hv**3 / c**2
exponente = h / (k * t)   # parte del exponente! e ** ( exponente / t )

# Calcular e usando la serie de Taylor
def calcular_euler(terminos):
    e = Decimal(0)
    for n in range(terminos):
        e += Decimal(1) / Decimal(math.factorial(n))
    return e

e = calcular_euler(100)  # Usar 100 términos para una buena aproximación

# Limitar el rango de t
rangeX = [-100000000000000000, 0]  # Cambia el rango según sea necesario
nIteraciones = 100000 # Cambiado a 100 para obtener 100 datos
step = (rangeX[1] - rangeX[0]) / nIteraciones

# Abrir un archivo CSV para escribir los resultados
name = f'outPy/grafica_min{rangeX[0]}_max{rangeX[1]}_nIteracion{nIteraciones}_.csv'

# Listas para almacenar los datos para la gráfica
v_values = []
y_values = []

with open(name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['v', 'f(v)'])  # Escribir encabezados

    for i in range(nIteraciones + 1):
        v = Decimal(rangeX[0] + i * step)
        # se hace un pequeña aproximacion a 0
        try:
            exponente_v = exponente * v
            y = "indeterminado"
            # Calcular el valor de y
            denominador = (pow(e, exponente_v) - 1)
            if denominador:
                y = constantes * pow(v, 3) / denominador
            else:
                print("El denominador es 0, por ende es una asintota")
            writer.writerow([v, y])  # Escribir los resultados en el archivo
            
            # Almacenar los valores para la gráfica
            v_values.append(float(v))
            y_values.append(float(y) if isinstance(y, Decimal) else None)

        except Overflow:
            print(f"Overflow en t={v}, se omite este valor.")

# Finalizar el temporizador
end_time = time.time()

# Calcular el tiempo total
elapsed_time = end_time - start_time

print(f"Tiempo total de ejecución: {elapsed_time:.6f} segundos")
print(f"Los datos se han guardado en '{name}'")

# Generar la gráfica
plt.figure(figsize=(10, 6))
plt.plot(v_values, y_values, label='f(v)', marker='o', color='blue')
plt.xlabel('v')
plt.ylabel('f(v)')
plt.title('Gráfica de f(v) vs v')
plt.legend()
plt.grid()
plt.savefig(f'outPy/grafica_rango({rangeX[0],rangeX[1]}_iteraciones{nIteraciones}).png')  # Guardar la gráfica como PNG
plt.show()  # Mostrar la gráfica