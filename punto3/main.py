from funciones import Row, derivadaAdelanto, derivadaRetardo, derivadaCentral;
from decimal import Decimal, getcontext;
from collections import deque;
import csv;

getcontext().prec = 50;

derivada = {
    "r": 0
    ,"a": 0
    ,"c": 0
    ,"min": 0
    ,"max": 0
};

with open("DB_COVIC.csv", mode='r', newline='', encoding='utf-8') as archivo:
    csvFile = csv.reader(archivo, delimiter=';')  # Especificar el delimitador

    # Leer la cabecera
    cabecera = next( csvFile );
    print( cabecera );
    
    for index, item in enumerate(csvFile):
      print(item);
      
      if index > 3:
        break;