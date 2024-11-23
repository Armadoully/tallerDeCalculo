import requests as r;
import json;
import csv;
import datetime;

url = "https://datos.gov.co/resource/gt2j-8ykr.json";

trama = {
 "departamento_nom":"BOGOTA"
 ,"$order": "fecha_diagnostico DESC"
 ,"$select": "id_de_caso as id, fecha_inicio_sintomas AS init, fecha_diagnostico AS diagnostic"
}

print("-Antes de la peticion");

respose = r.get(url,trama);
data = None;
print("Recibio la peticion");
if respose.status_code == 200:
  print("operacion exitosa",);
  data = respose.json();

if not data:
  exit("JSON VAcio")

with open("datos.csv", mode="w", newline='', encoding='utf-8') as database:
    writer = csv.writer(database);
    writer.writerow(["id","date_sintomas","date_diagnostic"]);
    print(data[1])
    cout = 0;
    for row in data:
      print(row)
    #   print(row["diagnostic"])

    #   writer.writerow([row.get("id"),]);
      if ( cout >= 200 ):
        break
      cout += 1;