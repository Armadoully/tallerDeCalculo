import pandas as pd
import math
from decimal import Decimal, getcontext
import time

# Configurar la precisión decimal
getcontext().prec = 50  # Ajusta la precisión según tus necesidades

# Iniciar el temporizador
start_time = time.time()

# Crear el DataFrame
grafica = pd.DataFrame({
    "t": [],
    "f(t) =": []
})

# Definir constantes
h = Decimal('6.626e-24')  # Constante de Planck
k = Decimal('1.38e-23')   # Constante de Boltzmann
v = Decimal('3.25e14')    # Frecuencia
c = Decimal('3.1e8')      # Velocidad de la luz

# Calcular constantes
v3 = Decimal('34.328125e42')  # Asegúrate de que este valor sea correcto
c2 = c ** 2
constantes = (h * v3) / c2    # parte de hv**3 / c**2
exponente = (h * v) / k       # parte del exponente! e ** ( exponente / t )

# Calcular e usando la serie de Taylor
def calcular_euler(terminos):
    e = Decimal(0)
    for n in range(terminos):
        e += Decimal(1) / Decimal(math.factorial(n))
    return e

e = calcular_euler(100)  # Usar 100 términos para una buena aproximación

# Limitar el rango de t
rangeX = [ 1 , 10 ]  # Cambia el rango según sea necesario

for i in range(rangeX[0], rangeX[1] + 1):
    t = Decimal(i)
    if t != 0:  # Evitar división por cero
        try:
            exponente_t = exponente / t;
            
            print(f"\tEl valor del exponente para t = {t} es: {exponente_t:.10}\n"); # debug of exponente
            # Verificar si el exponente es razonable
            if exponente_t < Decimal('10e4'):  # Ajusta este límite según sea necesario
                # Calcular el valor de y
                y = constantes / (e ** exponente_t - 1)
                grafica.loc[len(grafica)] = [t, y]
            else:
                print(f"Exponente demasiado grande para t={t}, se omite este valor.")
        except decimal.Overflow:
            print(f"Overflow en t={t}, se omite este valor.")
    else:
        print("t es cero, se omite este valor.")

# Finalizar el temporizador
end_time = time.time()

# Calcular el tiempo total
elapsed_time = end_time - start_time

print(f"Tiempo total de ejecución: {elapsed_time:.6f} segundos")


#  EXCEL ---------------------------------
# ----------------------------------------

# Manejo de la excepción...
if not len(grafica):
    print("\n\n!!!!!ERROR: El dataFrame no posee datos...\n\n");
    exit(1);
# Guardar el DataFrame en un archivo Excel
nombre_archivo = 'grafica.xlsx'
grafica.to_excel(nombre_archivo, index=False)
print(f"Los datos se han guardado en {nombre_archivo}")