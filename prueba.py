        
from sympy import symbols, lambdify, integrate, tan, parse_expr
from numpy import trapz

x = symbols('x')

# Ejemplo de entrada de datos con tan(3*x)
funcion_introducida = "tan(3*x)"

# Ejemplo de límites y subintervalos
a = 0
b = 2
n = 4

# Parsear la expresión introducida
expresion = parse_expr(funcion_introducida)

# Calcular los puntos (x, y) para el método del trapecio
puntos_x = [a + i * (b - a) / n for i in range(n + 1)]
puntos_y = [expresion.subs(x, x_val) for x_val in puntos_x]

# Calcular la aproximación de la integral utilizando el método del trapecio
aprox_integral_trap = trapz(puntos_y, puntos_x)
print(f"Aproximación con trapecio: {aprox_integral_trap:.4f}")

# Calcular la integral exacta
integral_exacta = integrate(expresion, (x, a, b))

# Verificar si la integral exacta es un número finito antes de imprimirlo con formato
if integral_exacta.is_finite:
    print(f"Integral exacta: {integral_exacta:.4f}")
else:
    print("La integral exacta no es un número finito. Por lo tanto, es divergente")


""" # Definir la variable simbólica x
x = symbols('x')

# Ejemplo de entrada de datos con tan(3*x)
funcion_introducida = "tan(3*x)"

# Ejemplo de límites y subintervalos
a = 0
b = 2
n = 4

# Parsear la expresión introducida
expresion = parse_expr(funcion_introducida)

# Imprimir la expresión parseada
print("Expresión parseada:", expresion)

# Calcular los puntos (x, y) para el método del trapecio
puntos_x = [a + i * (b - a) / n for i in range(n + 1)]
puntos_y = [expresion.subs(x, x_val) for x_val in puntos_x]

# Imprimir los puntos (x, y)
print("Puntos x:", puntos_x)
print("Puntos y:", puntos_y)

aprox_integral_trap = trapz(puntos_y, puntos_x)
print(f"= {aprox_integral_trap:.4f}")

###############  

x = symbols('x')

# Ejemplo de entrada de datos con tan(3*x)
funcion_introducida = "tan(3*x)"

# Ejemplo de límites y subintervalos
a = 0
b = 2


# Parsear la expresión introducida
expresion = parse_expr(funcion_introducida)

# Imprimir la expresión parseada
print("Expresión parseada:", expresion)

integral = integrate(expresion,(x,a,b))

# Verificar si la integral exacta es un número válido antes de imprimirlo
if integral.is_number:
    print(f"Integral exacta: {integral:.4f}")
else:
    print("La integral exacta no es un número válido.") """