from getCsv import cabecera, csvFile;
from funciones import Row, derivadaAdelanto, derivadaRetardo, derivadaCentral;
from decimal import Decimal, getcontext;

getcontext().prec = 50;

derivada = {
    "r": 0
    ,"a": 0
    ,"c": 0
    ,"min": 0
    ,"max": 0
};

indices = {
  'init': 0
 ,'end': csvFile[ -1 ].index
 ,"current": 0
};

rows = {
  "init": Row( *csvFile[ indices[ "init" ] ] )
 ,"end": Row( *csvFile[ indices[ "end" ] ] )
 ,"next": Row( *csvFile[ indices["init"] + 1 ] )
 ,"current": None
 ,"last": None
};

rows[ "last" ] = rows["current"] = rows["init"];

# Leer las filas
for fila in csvFile:
    
    if( indices["current"] ):
        rows["current"] = Row(*fila)
        rows["next"] = Row( *csvFile[ fila.index + 1 ] );
        rows["last"] = Row ( *csvFile[ indices["current"] - 1 ]);
    derivada["r"] = derivadaRetardo( indices["current"] , indices[ "end" ] , rows["current"].casos , rows["next"].casos , 1 );
    derivada["a"] = derivadaAdelanto( indices["current"] , indices[ "end" ] , rows["current"].casos , rows["next"].casos , 1 );
    derivada["c"] = derivadaCentral( indices["init"] , indices["current"] , indices[ "end" ] , rows["last"].casos , rows["next"].casos , 1 );
    indices["current"] += 1;