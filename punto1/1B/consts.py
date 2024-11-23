from decimal import Decimal , getcontext;
import math;
import json;

getcontext().prec = 50;

def calcular_euler(terminos):
 e = Decimal(0);
 for n in range(terminos):
  e += Decimal(1) / Decimal(math.factorial(n));
 return e

with open("./data.json", 'r') as archivo:
 datos = json.load(archivo);
    
print(datos);