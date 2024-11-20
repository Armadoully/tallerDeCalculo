#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <chrono>
#include <fstream>


// Función para calcular la constante e usando una serie de Taylor
double calcularEuler(int terminos) {
    double e = 0.0;
    double factorial = 1.0;
    for (int n = 0; n < terminos; ++n) {
        if (n > 0) factorial *= n;
        e += 1.0 / factorial;
    }
    return e;
}


int main() {
    // Iniciar el temporizador
    auto start_time = std::chrono::high_resolution_clock::now();

    // Definir constantes
    const double h = 6.626e-24; // Constante de Planck
    const double k = 1.38e-23;  // Constante de Boltzmann
    const double v = 3.25e14;   // Frecuencia
    const double c = 3.1e8;     // Velocidad de la luz
    const double v3 = 34.328125e42; // V^3 Constante

    // Calcular constantes
    double c2 = c * c;
    double constantes = (h * v3) / c2;    // Parte de hv^3 / c^2
    double exponente = (h * v) / k;       // Parte del exponente: e^(exponente / t)

    // Calcular e (número de Euler)
    double e = calcularEuler(100); // Usar 100 términos para una buena aproximación

    // Limitar el Dominio de t
    double rangeX[2] = {1e15,1e15+1e3};

    if ( rangeX[0] > rangeX[1] ) {
      std::cout << "\n Error: En el dominio de la función, se puso un valor mayor en minimo";
      double temp = rangeX[0];
      rangeX[0] = rangeX[1];
      rangeX[1] = rangeX[0];
      
    }
    // Archivo ---------
    std::ofstream file("grafica.csv"); // abrir 

     //Catch error
    if (!file.is_open()) {
        std::cerr << "Error al abrir el archivo para escribir.\n";
        return 1;
    }
    std::cout << "Inicio el programa\n";

    // registrar constantes....
    file << "Constantes:\n - h : " << h << "\n - v : " << v << "\n - c : " << c << "\n - k : " << k << "\n - v3 : " << v3 << "\n - c2 : " << c2  << "\n - (hv^3/c^2) : " << constantes  << "\n - (hv/k): " << exponente;
    file << "\n - Inicia en: " << rangeX[0] << ", termina en: " << rangeX[1];
    file << "\n\ntabla \n\nt,expresion variable exp(hv/kt),f(t)\n";
    std::cout << "\n se creo el archivo y se empezó a iterar";
    // iteración para calcular
    for (double i = rangeX[0]; i <= rangeX[1]; ++i) {
        double t = static_cast<double>(i);

        file << t << ",";// almacenó el valor de t
        if (t != 0) { // Evitar división por cero
            try {

                // cálculos 
                double exponente_t = exponente / t;
                if ( i == rangeX[1] ) std::cout << std::endl << exponente_t;
                double expo_F = std::pow(e, exponente_t);
                double y = constantes / ( expo_F- 1.0);
                file << expo_F << "," << y << "\n"; // almacenamiento del valor para cada t
            } catch (const std::exception &e) {
                file << ",,Error : " << e.what() << "\n"; // si no de puede operar almacena el error!!
                std::cout << "Error en t=" << t << ": " << e.what() << "\n"; 
            }

        } else {
            file << "indeterminado,indeterminado"; // catch error division por 0
            std::cout << "\n !!!!Excepcion: t es cero, se omite este valor.\n";
        }
    }

    // Finalizar el temporizador
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_time = end_time - start_time;

    // Mostrar el tiempo total de ejecución
    std::cout << "Tiempo total de ejecución: " << elapsed_time.count() << " segundos\n";

    file << "\n\n --- Tiempo de ejecución: " << elapsed_time.count(); // almacena tiempo de ejecución 

    file.close();

    std::cout << "Los datos se han guardado en grafica.csv\n";

    return 0;
}