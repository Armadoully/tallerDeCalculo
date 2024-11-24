import math
from decimal import Decimal, getcontext, Overflow
import time
import csv

# Configurar la precisión decimal
getcontext().prec = 50  # Ajusta la precisión según tus necesidades

# Iniciar el temporizador
start_time = time.time()

# Definir constantes
h = Decimal('6.626e-34')  # Constante de Planck
k = Decimal('1.38e-23')   # Constante de Boltzmann
t = Decimal( "35e13" );   # Temperatura
c = Decimal('3.1e8')      # Velocidad de la luz

# Calcular constantes
v3 = Decimal('34.328125e42')  # Asegúrate de que este valor sea correcto
c2 = c ** 2
constantes = h / c2# parte de hv**3 / c**2
exponente = (h * t) / k       # parte del exponente! e ** ( exponente / t )
# Calcular e usando la serie de Taylor
def calcular_euler(terminos):
    e = Decimal(0)
    for n in range(terminos):
        e += Decimal(1) / Decimal(math.factorial(n))
    return e

e = calcular_euler(100)  # Usar 100 términos para una buena aproximación

exponente = pow( e , exponente )

# Limitar el rango de t
rangeX = [0, 10000]  # Cambia el rango según sea necesario
nIteraciones = 10000;
step = rangeX[1] / nIteraciones;
step = int(step);
# Abrir un archivo CSV para escribir los resultados
name = f'outPy/grafica_min{rangeX[0]}_max{rangeX[1]}_nIteracion{nIteraciones}_.csv';

with open(name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['t', 'f(v)'])  # Escribir encabezados

    for i in range( rangeX[0], rangeX[1] + 1 , step ):
        v = Decimal(i)
        # se hace un pequeña aproximacion a 0
        if v == 0:
            v = Decimal("1e-2");
        if v != 0:  # Evitar división por cero
            try:            
                # Calcular el valor de y
                y = ( constantes * pow( v , 3 ) ) / ( pow( exponente , v )- 1)
                writer.writerow([v, y])  # Escribir los resultados en el archivo
            except Overflow:
                print(f"Overflow en t={v}, se omite este valor.")
        else:
            print("t es cero, se omite este valor.")

# Finalizar el temporizador
end_time = time.time()

# Calcular el tiempo total
elapsed_time = end_time - start_time

print(f"Tiempo total de ejecución: {elapsed_time:.6f} segundos")
print(f"Los datos se han guardado en '{name}'")