# Import math Library
from decimal import Decimal, getcontext;
from math import factorial;
import pandas as pd;

getcontext().prec = 1000;

def calcular_euler(terminos):
    e = Decimal(0)
    for n in range(terminos):
        e += Decimal(1) / Decimal(factorial(n))
    return e
e = calcular_euler(1000);

# Print the value of Euler e
# print ( e )


h = Decimal( "6.626e-34" );
c = Decimal( "3.1e8" );
k = Decimal( "1.38e-23" );
t = Decimal( "35e2" );



# derivada 1 

# u = e ^ ( b ) faltaria u^v
u = pow( e , Decimal( 3313 ) / Decimal('2415e15') );
# 3 / b   ->  b = h/kt
bpor3inverso = Decimal( "7245E15" ) / Decimal( 3313 );
# b = h/kt
b = h / ( k * t );


# derivada2 

# h / c^2
a = (2 * h) / pow( c , 2 );

# b ^ 2
b2 = pow( b , 2 );

bu =  u * b;

b2por3 = b2 * 3;
b2por2 = b2 * 2;

u2 = pow( u , 2 );

v = Decimal(1);

for i in range( 200 ):
  # print( f"u={u}")
  uALaV = pow( u , v ); # u = e^b ||| u^v = e^(bv)
  
  derivada1 =  uALaV * ( v - bpor3inverso ) + bpor3inverso;
  
   #cosas para la derivada 2 depende de "v"
  v2 = pow( v , 2 ); # v ^ 2
  v3 = v2 * v; # v ^ 3
   # e^(bv) - 1
  eMenos1 = uALaV - Decimal( 1 ); # u^v - 1 = e^(bv) - 1
  
  # Derivadas y formulas en las fotos.... de ahi sale todo :D
  parte1Derivada2 = ( 3 * v * ( 2 * ( eMenos1 ) - b * uALaV * v2 ) ) / pow( eMenos1 , 2 );
  parte2Derivada2 = ( uALaV*b2 * ( 3*uALaV - 2 * v3 ) ) / pow( eMenos1 , 3 );
  derivada2 = a * ( parte1Derivada2 - parte2Derivada2 );
  vt = v - derivada1 / derivada2; 
  print( f"##iteración: {i} = Para v ={v} , la \"funcion\" es: {derivada1} y su \"derivada\" {derivada2}" );
  print( f"\n\n##----Resultado: {vt}" )
  v = vt;