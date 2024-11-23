import csv;

csvFile = None;
cabecera = None;

cambio = False;
año = 2020;
dias = {};

with open("DB_COVIC.csv", mode='r', newline='', encoding='utf-8') as archivo:
    csvFile = csv.reader(archivo, delimiter=';')  # Especificar el delimitador

    # Leer la cabecera
    cabecera = next(csvFile);

    for fila in csvFile:
     if int ( fila[ 0 ] ) == año :
      ekey = False;
      for key in dias.keys():
       if ( key == fila[ 1 ] ):
        ekey = True;
      if ( ekey ):
       dias[ fila[ 1 ] ] += 1;
      else:
       dias[ fila[ 1 ] ] = 0;
    #   print(fila)
     else:
      break;


# # print( csvFile );



print(f"En el año: {año} tiene:\n");
for [localidad , n] in dias.items():
  print(f" - {localidad} : {n}\n");
print("registros");