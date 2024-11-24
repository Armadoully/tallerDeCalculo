import math;
from decimal import Decimal, getcontext;

getcontext().prec = 50;

class Row:
 def __init__(self, ano, localidad_residencia, grupos_edad_quinquennales, sexo, casos, muertes):
  self.ano = int(ano)  # Convertir a entero
  self.localidad_residencia = localidad_residencia
  self.grupos_edad_quinquennales = grupos_edad_quinquennales
  self.sexo = sexo
  self.casos = Decimal(casos)  # Convertir a entero
  self.muertes = int(muertes) if muertes else 0 # Convertir a entero
  
def derivadaAdelanto( i , iF , fo , fi , h ):
 if ( not i ):
  return ( fi - fo ) / h;
 return '*';

def derivadaRetardo( i , iF , fo , fi , h ):
 if ( i == iF ):
   return '*';
 return ( fo - fi ) / h;

def derivadaCentral ( iN , i , iF , fr , fa , h ):
 if ( i == iN or i == iF ):
  return '*';
 return ( fr - fa ) / ( h * 2 );