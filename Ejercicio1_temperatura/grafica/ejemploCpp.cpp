#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <chrono>
#include <fstream>

// Definición de estructura para almacenar los datos de la gráfica
struct DataPoint {
    double t;
    double f_t;
};

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
    const double v3 = 34.328125e42; // Asegúrate de que este valor sea correcto

    // Calcular constantes
    double c2 = c * c;
    double constantes = (h * v3) / c2;    // Parte de hv^3 / c^2
    double exponente = (h * v) / k;       // Parte del exponente: e^(exponente / t)

    // Calcular e (número de Euler)
    double e = calcularEuler(100); // Usar 100 términos para una buena aproximación

    // Limitar el rango de t
    int rangeX[2] = {-10000, 10000};

    // Crear un vector para almacenar los datos
    std::vector<DataPoint> grafica;

    for (int i = rangeX[0]; i <= rangeX[1]; ++i) {
        double t = static_cast<double>(i);
        if (t != 0) { // Evitar división por cero
            try {
                double exponente_t = exponente / t;
                std::cout << "\tEl valor del exponente para t = " << t
                          << " es: " << exponente_t << "\n"; // Depuración

                // Verificar si el exponente es razonable
               // if (exponente_t < 10e4) {
                    // Calcular el valor de y
                    double y = constantes / (std::pow(e, exponente_t) - 1.0);
                    grafica.push_back({t, y});
                //} else {
                //    std::cout << "Exponente demasiado grande para t=" << t
               //               << ", se omite este valor.\n";
              //  }
            } catch (const std::exception &e) {
                std::cout << "Error en t=" << t << ": " << e.what() << "\n";
            }
        } else {
            std::cout << "t es cero, se omite este valor.\n";
        }
    }

    // Finalizar el temporizador
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_time = end_time - start_time;

    // Mostrar el tiempo total de ejecución
    std::cout << "Tiempo total de ejecución: " << elapsed_time.count() << " segundos\n";

    // Guardar los datos en un archivo CSV
    if (grafica.empty()) {
        std::cerr << "!!!!!ERROR: El vector de datos no posee elementos...\n";
        return 1;
    }

    std::ofstream file("grafica.csv");
    if (!file.is_open()) {
        std::cerr << "Error al abrir el archivo para escribir.\n";
        return 1;
    }

    file << "t,f(t)\n";
    for (const auto &point : grafica) {
        file << point.t << "," << point.f_t << "\n";
    }
    file.close();

    std::cout << "Los datos se han guardado en grafica.csv\n";

    return 0;
}