from decimal import Decimal, getcontext;
import math;

getcontext().prec = 100;

t_o = pow(  Decimal( 1180 ) , 2 );
t_n = Decimal( 0 ) ;

constante = ( Decimal("-566") / t_o );
constante2 = Decimal(6.6) / t_o;
for i in range( 10 ):
  fdet = constante * ( t_n - ( constante2 * pow( t_n , 3 ) ) );
  derivada = constante * ( 1 - ( 3 * constante2 * pow( t_n , 2 ) ) );
  t_n = t_n - ( fdet  / derivada );
  print( f"### Iteracion: {i} = \n### {t_n}" );
  