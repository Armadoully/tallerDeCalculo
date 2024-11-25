# ¿Qué pasa aquí?
Este es el punto 1.B de la función de radiación del cuerpo negro de Plank con la variable T constante descrita en el documento "Taller3Calculo.pdf" en la carpeta raiz del proyecto, especificamente para encontrar el punto critico (maximo de la frecuencia v "Hz") de la funcion con el algortimo de NewtonRaphson


# Limite
Se saco el limite de la función para saver si una discontinuidad es una asintota o una discontinuidad puntual, lo cual se catalogo como discontiudad puntual, esto se almaceno en "limite/outPy/limit.csv" tambien se tiene una grafica en la misma carpeta ""limite/outPy/grafica.png" donde se alcanza a visualizar la tendencia de este limite!

# Gráfica
Codigo .py el cual es un generador de csv y una grafica en png de los valores dados en la variable rangeX[min,max] y nIteracion dados en ese mismo código. Este funciona pues pasandole esos valores (un maximo, un minimo y el número de iteraciones que queramos hacer le a la función). Si le cambiamos la variable rangeX[min,max] y le cambiamos el nIteracion nos genera un cvs con nombre f"grafica_min{rangeX[0]}_max{rangeX[1]}_nIteracion{nIteraciones}_.csv" el cual pues es una tabla con valores de toda la ejecución y lo almacena en la carpeta "outPy/" de esa misma carpeta. Se almacena allí tambien, una grafica en .png generada con ese mismo código y se guarda con el nombre de: f"grafica_rango({rangeX[0],rangeX[1]}_iteraciones{nIteraciones}).png"

Con este código se evaluo la gráfica con valores negativos muy grandes al igual que positivos: limites al infinito y menos infinito

# limite
En este documento funciona igual que el anterior (grafica). Este evalua el limite de la funcion cuando se aproxima a 0 para ver donde tiende!

# newtonRaphson

Este codigo fuente funciona parecido que los anteriores, solo tienes que cambiar el numero de iteraciones que quieras para aproximar mas o menos el valor del punto crítico dentro del for. Este devuelve un csv con la tabla (no genera imagen) y tambien devuelve valores por consola. 