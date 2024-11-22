#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
using namespace std;

double 
  h = 6.626e-34
 ,k = 3.18e-23
 ,v = 3.25e14
 ,c = 3.1e8
 ,h2 = pow( h , 2 )
 ,v4 = pow( v , 4 )
 ,c2 = pow( c , 2 );


int main() {
 double z = 1;
 double a1 = h2 * v4,
        b = c2 * k,
        cons = a1 / b,
        a2;

 ofstream file("/out/grafica.csv"); // abrir 

 //Catch error
 if (!file.is_open()) {
  cerr << "Error al abrir el archivo para escribir.\n";
  return 1;
 }

 file << "Limite de z(h^2*v^4) / (c^2*k)" 
 << endl  << " - h^2 : " << h2
 << endl  << " - v^4 : " << v4
 ;
 
 for (  ; z > 0 ; z /= 10 ) {
  a2 = z * a1;
  cout << "El resutado de " << z << '\t' <<  a2 << '/' << b << " es = " << cons << endl;
  
 }
 
 system("PAUSE");
 return 0;
}