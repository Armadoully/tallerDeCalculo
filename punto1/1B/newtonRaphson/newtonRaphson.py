# Import math Library
from decimal import Decimal, getcontext
from math import factorial
import csv
import os

# Configurar la precisión decimal
getcontext().prec = 1000

def calcular_euler(terminos):
    e = Decimal(0)
    for n in range(terminos):
        e += Decimal(1) / Decimal(factorial(n))
    return e

# Calcular e usando 1000 términos
e = calcular_euler(1000)

# Definir constantes físicas
h = Decimal("6.626e-34")  # Constante de Planck
c = Decimal("3.1e8")      # Velocidad de la luz
k = Decimal("1.38e-23")   # Constante de Boltzmann
t = Decimal("35e2")       # Temperatura

# Calcular u y b
u = pow(e, Decimal(3313) / Decimal('2415e15'))  # u = e^(b)
b = h / (k * t)  # b = h / (k * t)

# Inicializar v
v = Decimal(1)

# Crear la carpeta 'outPy' si no existe
os.makedirs('outPy', exist_ok=True)

# Definir el número de iteraciones
iteraciones = 200

# Nombre del archivo CSV
filename = f'outPy/aproximacion{iteraciones}.csv'

# Abrir el archivo CSV para escribir los resultados en formato UTF-8
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Iteración', 'v', 'Función', 'Derivada', 'aproximacion'])  # Escribir encabezados

    # Iterar para calcular la función y su derivada
    for i in range(iteraciones):
        uALaV = pow(u, v)  # u^v = e^(bv)
        
        # Calcular la primera derivada
        derivada1 = 3 - ((v * b * uALaV) / (uALaV - 1))
        
        # Calcular la segunda derivada
        fraccionSinb = uALaV / (uALaV - 1)
        parte1Derivada2 = b * fraccionSinb
        parte2Derivada2 = 1 + v * b * fraccionSinb
        derivada2 = parte1Derivada2 * parte2Derivada2
        
        # Actualizar v usando el método de Newton-Raphson
        vt = v - derivada1 / derivada2
        
        # Escribir los resultados en el archivo CSV
        writer.writerow([i, v, derivada1, derivada2, vt])
        
        # Imprimir resultados
        print(f"##iteración: {i} = Para v ={v} , la \"funcion\" es: {derivada1} y su \"derivada\" {derivada2}")
        print(f"\n\n##----Resultado: {vt}")
        
        # Actualizar v para la siguiente iteración
        v = vt