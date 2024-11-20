# Descripción
 En este apartado se graficará la función de radiación de un cuerpo negro con "v" como constante y "t" siendo variable a lo largo de la ejecución del programa, al inicio se tiene pensado hacer, 200000 iteraciones, con un dominio discreto de [-100000,100000] con salto de iteración ++ (de a 1).

# ¿Cómo se guardan los datos?
 Se tiene pensado que los datos de la ejecución del programa se almacenen en una hoja de cálculo .xlsx (Excel)

# Librerías
 Se usarán las librerias: pandas (pequeña base de datos antes de pasarlo al Excel), math, decimal (mejora la precición de cálculos), y, time (mira el tiempo de ejecucion de iteración y evalua para su optimización, en conclusión se usa para el desarrollo del código)

# Bug 1 (19/11/2024) overflow
"ejercicio1__x_y.py" es aquel archivo que contiene los cálculos matemáticos de la función como tal, pero desborda siempre el exponente del euler, ya que es demasiado grande, es una burrada: 1.560471014E+14 para t = 1... Ni idea de cómo proseguir.
\\En la carpeta "ImagesOfDebug" se documentó el hecho, no se ha arreglado, lo cual retrasará el progreso del desarrollo