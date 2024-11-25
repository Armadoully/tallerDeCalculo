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

# Abrir un archivo CSV para escribir los resultados
name = 'outPy/limit.csv'
v = Decimal(1)  # valor inicial de v para empezar a tender a 0
vnegativo = Decimal(-1)

# Listas para almacenar los datos para la gráfica
v_values = []
y_values = []
vnegativo_values = []
ynegativo_values = []

with open(name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['v+', 'f(v)+', 'v-', 'f(v)-'])  # Escribir encabezados

    for i in range(36):
        # se hace un pequeña aproximacion a 0
        try:
            exponente_v = exponente * v
            exponente_vNegativo = exponente * vnegativo
            
            # Calcular el valor de y
            denominador = ( pow(e, exponente_v) - 1 )
            y = constantes * pow(v, 3) / denominador
            
            denominadorNegativo = (pow(e, exponente_vNegativo) - 1)
            yNegativo = constantes * pow(vnegativo, 3) / denominadorNegativo
            
            writer.writerow([v, y, vnegativo, yNegativo])  # Escribir los resultados en el archivo
            
            # Almacenar los valores para la gráfica
            v_values.append(float(v))
            y_values.append(float(y))
            vnegativo_values.append(float(vnegativo))
            ynegativo_values.append(float(yNegativo))

        except Overflow:
            print(f"Overflow en t={v}, se omite este valor.")
        
        v /= Decimal(10)
        vnegativo /= Decimal(10)

# Finalizar el temporizador
end_time = time.time()

# Calcular el tiempo total
elapsed_time = end_time - start_time

print(f"Tiempo total de ejecución: {elapsed_time:.6f} segundos")
print(f"Los datos se han guardado en '{name}'")

# Generar la gráfica
plt.figure(figsize=(10, 6))

# Gráfica para valores positivos
plt.plot(v_values, y_values, label='f(v)+', marker='o', color='blue')

# Gráfica para valores negativos
plt.plot([-v for v in vnegativo_values], ynegativo_values, label='f(v)-', marker='x', color='red')

# Configuración de escalas
plt.xscale('log')
plt.yscale('log')

# Etiquetas y título
plt.xlabel('v')
plt.ylabel('f(v)')
plt.title('Gráfica de f(v) vs v')
plt.legend()
plt.grid()

# Guardar la gráfica como PNG
plt.savefig('outPy/grafica.png')  
plt.show()  # Mostrar la gráfica