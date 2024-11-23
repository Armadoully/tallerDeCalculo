import math;
import decimal as d;
import json;
import sys
import os

# Añadir la carpeta superior al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora puedes importar consts
import consts

# Ejemplo de uso
# print(consts.TU_CONSTANTE)  # Reemplaza TU_CONSTANTE con el nombre de la constante que quieras usar

d.getcontext().prec = 50

e = consts.calcular_euler( 50 );

# h / kT <=> despejado....
b = ( d.Decimal(3313) / d.Decimal( 2415 ) ) * d.Decimal("1e-15");

# Este es el despeje de -3b 
# b = (d.Decimal(3313) / d.Decimal( 2415 )) * d.Decimal("1e-15");
# acompañante = b * 3 (solo que lo despeje para hacer menos calculos)
acompañante = ( d.Decimal( "-3e15" ) * d.Decimal( 2415 ) ) / d.Decimal( 3313 ); 


ran = [ d.Decimal( -100 ) , d.Decimal( 100 ) ];
incrementador = d.Decimal( "1e-2" );
v = ran[ 0 ];

for i in range( 20000 ):
 
 v += incrementador;