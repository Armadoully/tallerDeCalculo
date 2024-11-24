import csv;
from collections import deque;

with open("x.csv", mode='r', newline='', encoding='utf-8') as archivo:
    csvFile = csv.reader(archivo, delimiter=',')  # Especificar el delimitador
    
    # Almacena solo 3 objetos...
    array = deque(maxlen=3);
    
    # Leer la cabecera
    cabecera = next( csvFile );
    print( cabecera );
    
    # def agregarLosSig3 ():
    #   for 0 in range( 3 ):
    #    sig = next( csvFile );
    #    array.append(  ); 
    #leer fila por fila --------------------------------
    # ----------------------------------------
    # for row in csvFile:
      for x in range( 10 ):
       try:
        array
        print( x , next(csvFile) )
       except StopIteration:
        array.append('');
        break;