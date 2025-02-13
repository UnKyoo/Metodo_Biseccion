#   Codigo que implementa el esquema numerico 
#   del metodo de biseccion
# 
#           Autor:
#   Mendez Cervera Gilbert Alexander
#   mendezgilbert222304@outlook.com
#   Version 1.01 : 12/02/2025
#


import numpy as np # import de la libreria numpy para operaciones
import matplotlib.pyplot as plt # importe para la libreria de gráficas matplot

#Creación del metodo para 
# Definir la función que va introducirse en
# el esquema del metodo de biseccion
def f(x):
    return np.cos(x) - x #Función

# Algoritmo numerico del
# Método de Bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    #Verificar si el método de bisección es aplicable en el intervalo.
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None
    
    iteraciones = [] #Lista para almacenar las iteraciones 
    errores_abs = [] #Lista para almacenar los errores absolutos
    errores_rel = [] #Lista para almacenar los errores relativos
    errores_cua = [] #Lista para almacenar los errores cuadráticos 
    c_old = a  # Para calcular errores
    #Encabezado de la tabla iteraciones en consola
    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |     Error_abs     |     Error_rel     |     Error_cua     ")
    print("-" * 85)
    #Iteración del método de bisección
    for i in range(max_iter):
        c = (a + b) / 2 #Calcular el punto medio
        iteraciones.append(c) #Almacenar el valor de c en la lista

        # Cálculo de errores
        error_abs = abs(c - c_old) #Error absoluto
        error_rel = error_abs/c #Error relativo
        error_cua = (c - c_old)**2 #Error cuadrático

        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cua.append(error_cua)


        #Imprimir valores en cada iteración
        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error_abs:.8e} | {error_rel:.8e} | {error_cua:.8e}")
        #Condición de parada si f(c) es menor que la tolerancia o el error absoluto es menor que la tolerancia

        # Decidir el nuevo intervalo basado en el signo de f(a) * f(c)
        if abs(f(c)) < tol or error_abs < tol:
            break

        if f(a) * f(c) < 0:
            b = c # La raíz está en el intervalo [a, c]
        else:
            a = c # La raíz está en el intervalo [c, b]

        c_old = c  # Actualizar el valor anterior de c

    return iteraciones, errores_abs, errores_rel, errores_cua #retornar valores

# Parámetros iniciales
# se introduce el intervalo [a, b]
a, b = 0, 1
#a, b = 0, 1.5
#a, b = -2, -1
# Ejecutar el método de bisección
iteraciones, errores_abs, errores_rel, errores_cua = biseccion(a, b)

# Crear la figura
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y la convergencia de iteraciones del método de bisección
x = np.linspace(a - 1, b + 1, 400)
y = f(x)

ax[0].plot(x, y, label=r'$f(x) = \cos(x) - x', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)  # Línea en y=0
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica de errores de cada iteración
ax[1].plot(range(1, len(errores_abs)+1), errores_abs, label = "Error Absoluto" , marker='o', linestyle='-', color='r')
ax[1].plot(range(1, len(errores_rel)+1), errores_rel, label = "Error Relativo" , marker='s', linestyle='-', color='b')
ax[1].plot(range(1, len(errores_cua)+1), errores_cua, label = "Error Cuadrático" , marker='^', linestyle='-', color='y')
ax[1].set_yscale("log")  # Escala logarítmica
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Errores")
ax[1].set_title("Errores de cada Iteración")
ax[1].legend()
ax[1].grid()

# Guardar la figura
plt.savefig("biseccion_convergencia.png", dpi=300)
plt.show() #Mostrar la gráfica en pantalla

