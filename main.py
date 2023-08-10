import math
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import typing
from PyQt5 import uic
from sympy import *
from numpy import *
from sympy.parsing.sympy_parser import parse_expr

class Calculadora(QMainWindow):
    
    def __init__(self) -> None:
        super(Calculadora, self).__init__()
        uic.loadUi('segundaoportunidad.ui', self)

        #Llamando a los botones
        self.btn_nine.clicked.connect(lambda: self.ingresarValores('9'))
        self.btn_eight.clicked.connect(lambda: self.ingresarValores('8'))
        self.btn_seven.clicked.connect(lambda: self.ingresarValores('7'))
        self.btn_six.clicked.connect(lambda: self.ingresarValores('6'))
        self.btn_five.clicked.connect(lambda: self.ingresarValores('5'))
        self.btn_four.clicked.connect(lambda: self.ingresarValores('4'))
        self.btn_three.clicked.connect(lambda: self.ingresarValores('3'))
        self.btn_two.clicked.connect(lambda: self.ingresarValores('2'))
        self.btn_one.clicked.connect(lambda: self.ingresarValores('1'))
        self.btn_zero.clicked.connect(lambda: self.ingresarValores('0'))

        # Botones especiales
        self.btn_multiply.clicked.connect(lambda: self.ingresarValores('*')) # Boton multiplicar
        self.btn_substract.clicked.connect(lambda: self.ingresarValores('-'))
        self.btn_sum.clicked.connect(lambda: self.ingresarValores('+'))
        self.btn_divide.clicked.connect(lambda: self.ingresarValores('/'))
        self.btn_leftbracket.clicked.connect(lambda: self.ingresarValores('('))
        self.btn_rightbracket.clicked.connect(lambda: self.ingresarValores(')'))
        self.btn_result.clicked.connect(lambda: self.ingresarValores('='))
        self.btn_root.clicked.connect(lambda: self.squaredRoot())
        self.btn_trapeze.clicked.connect(lambda: self.integralexacta())
        self.btn_trapeze.clicked.connect(lambda: self.integralTrapecio())
        self.btn_simpson.clicked.connect(lambda: self.integralexacta())
        self.btn_simpson.clicked.connect(lambda: self.integralSimsom())
        self.btn_cleaner.clicked.connect(lambda: self.limpiarTodo()) # Boton C (limpiar)
        self.btn_squared.clicked.connect(lambda: self.cuadrado())
        self.btn_cubed.clicked.connect(lambda: self.cubo())
        self.btn_elevar.clicked.connect(lambda: self.elevado())
        self.btn_e.clicked.connect(lambda: self.exponencial())
        self.btn_x.clicked.connect(lambda: self.agregandoX())
        self.btn_cos.clicked.connect(lambda: self.funcionCos())
        self.btn_sin.clicked.connect(lambda: self.funcionSin())
        self.btn_tan.clicked.connect(lambda: self.funcionTan())
        self.btn_backspace.clicked.connect(lambda: self.borrarCaracter())
        self.btn_trapeze.clicked.connect(lambda: self.calcularDiferenciaTrapecio())
        self.btn_simpson.clicked.connect(lambda: self.calcularDiferenciaSimpson())
        self.btn_pi.clicked.connect(lambda: self.pi())
        self.btn_ln.clicked.connect(lambda: self.funcionLn('ln'))
        
        # Restricciones
        
        # Definir la expresión regular para permitir solo 'x', números y los operadores +, -, *, /    
        regex = QRegExp('[x0-9+\\-*/\\s().]+')
        validacion = QRegExpValidator(regex)
        self.entradadedatos.setValidator(validacion)
        self.txtLimite_Inferior.setValidator(validacion)
        self.txtLimite_Superior.setValidator(validacion)
        
        # Validar los datos que pongan en n
        regla = QRegExp('[0-9]+')
        validacion2 = QRegExpValidator(regla)
        self.txtSubintervalos.setValidator(validacion2)

# Creando las funciones de los botones  

    #Creando la funcion de limpiar todo los campos
    def limpiarTodo(self):
        self.txtLimite_Inferior.setText("")
        self.txtLimite_Superior.setText("")
        self.txtSubintervalos.setText("")
        self.entradadedatos.setText("")
        self.lbl_resultTrap.setText("=")
        self.lbl_resultSimp.setText("=")
        self.lbl_valorexacto.setText("")
        self.lbl_diference.setText("")
        self.lbl_Errores.setText("")

    # Creando la funcion de backspace
    def borrarCaracter(self):
        texto_actual = self.entradadedatos.text()
        nuevo_texto = texto_actual[:-1]  
        self.entradadedatos.setText(nuevo_texto)

    # Creando la funcion de X
    def agregandoX(self):
        text = "*x"
        self.entradadedatos.setText(self.entradadedatos.text() + text)

    # Creando la funcion de ln
    def funcionLn(self, funcion):
        texto = f"{funcion}("
        self.entradadedatos.setText(self.entradadedatos.text() + texto)

    # Creando la funcion de pi
    def pi(self):
        self.entradadedatos.setText(self.entradadedatos.text() + str(pi))

    # Creando la funcion de cos
    def funcionCos(self):
        texto = "cos("
        self.entradadedatos.setText(self.entradadedatos.text() + texto)

    # Creando la funcion de tan
    def funcionTan(self):
        texto = "tan("
        self.entradadedatos.setText(self.entradadedatos.text() + texto)

    # Creando la funcion de sin
    def funcionSin(self):
        texto = "sin("
        self.entradadedatos.setText(self.entradadedatos.text() + texto)

    #Creando la funcion del cuadrado
    def cuadrado(self):
        texto = "**2"
        self.entradadedatos.setText(self.entradadedatos.text() + texto)

    # Creando la funcion del cubo
    def cubo(self):
        texto = "**3"
        self.entradadedatos.setText(self.entradadedatos.text() + texto)
    
    # Creando la funcion del elevado a la n
    def elevado(self):
        texto = "**"
        self.entradadedatos.setText(self.entradadedatos.text() + texto)
    
    # Creando la funcion para ingresar los datos
    def ingresarValores(self, tecla):
        
        try:
            if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.' or tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
                self.entradadedatos.setText(self.entradadedatos.text() + tecla)

            if tecla == '=':
                resultado = eval(self.entradadedatos.text())
                self.entradadedatos.setText(str(resultado))
        except:
            self.lbl_Errores.setText("😔 No se pudo realizar la operacion.")

    # Creando la funcion del boton de raiz cuadrada
    def squaredRoot(self):
        
        texto = "np.sqrt("
        self.entradadedatos.setText(self.entradadedatos.text() + texto)
        
        """ try:
            valor_entrada = float(self.entradadedatos.text())
            
            if valor_entrada < 0:
                self.entradadedatos.setText("Entrada inválida 😡")  # Mostrar un mensaje de error para entradas negativas
            else:
                resultado = math.sqrt(valor_entrada)
                self.entradadedatos.setText(str(resultado))

        except ValueError:
            self.entradadedatos.setText("Entrada inválida 😡")  # Mostrar un mensaje de error para entradas no numéricas
 """
    
    # Creando la funcion del exponencial
    def exponencial(self):
        text = "exp("
        self.entradadedatos.setText(self.entradadedatos.text() + text)

    # Creando la otra función para la calcular la integral por el trapecio
    def integralTrapecio(self):
        
        x = symbols('x')  # declarar la variable simbólica x

        try:
            if not self.txtLimite_Inferior.text() or not self.txtLimite_Superior.text() or not self.txtSubintervalos.text():
                self.lbl_Errores.setText("⛔ Error! Ingrese todos los límites y el número de subintervalos.")
            
            else:
                a = float(self.txtLimite_Inferior.text())  # Limite inferior
                b = float(self.txtLimite_Superior.text())  # Limite Superior
                n = int(self.txtSubintervalos.text())  # Subintervalos
                funcion_introducida = self.entradadedatos.text()  # Asignando la función introducida desde la entrada de datos

                funcion = parse_expr(funcion_introducida)

                # Calcular los puntos (x, y) para el método del trapecio
                puntos_x = [a + i * (b - a) / n for i in range(n + 1)]
                puntos_y = [funcion.subs(x, x_val) for x_val in puntos_x]

                # Calcular la aproximación de la integral utilizando el método del trapecio
                aprox_integral_trap = trapz(puntos_y, puntos_x)
                self.lbl_resultTrap.setText(f"= {aprox_integral_trap:.4f}")
        
        except:
            self.lbl_Errores.setText("No se pudo calcular por Trapecio")

    # Creando la otra función para la calcular la integral por Simpson
    def integralSimsom(self):
        
        if not self.txtLimite_Inferior.text() or not self.txtLimite_Superior.text() or not self.txtSubintervalos.text():
            self.lbl_Errores.setText("⛔ Error! Ingrese todos los límites y el número de subintervalos.")
        
        else:
            
            x = symbols('x')
            a = float(self.txtLimite_Inferior.text())
            b = float(self.txtLimite_Superior.text())
            n = int(self.txtSubintervalos.text())
            funcion_Introducida = self.entradadedatos.text()

            funcion = parse_expr(funcion_Introducida)

            if n % 2 != 0:
                self.lbl_Errores.setText("⛔ Error! El número de subintervalos debe ser par para el método de Simpson.")
                return
            
            h = (b - a) / n
            x_vals = [a + i * h for i in range(n+1)]
            y_vals = [funcion.subs(x,x_val) for x_val in x_vals]
        
            suma_pares = sum(y_vals[2:n-1:2])
            suma_impares = sum(y_vals[1:n:2])
        
            integral_aprox = (h / 3) * (y_vals[0] + 4 * suma_impares + 2 * suma_pares + y_vals[n])
            self.lbl_resultSimp.setText(f"= {integral_aprox:.4f}")

    # Creando la funcion para la integral exacta
    def integralexacta(self):
        
        try:
            # Declaramos a x
            x = symbols('x') 
            
            # Limites de la integral
            a = float(self.txtLimite_Inferior.text())
            b = float(self.txtLimite_Superior.text())

            # Le pasamos lo que esta en el txt entradadedatos a una variable
            funcion_introducida = self.entradadedatos.text()

            g = parse_expr(funcion_introducida)

            # Calculamos la integral
            integral = integrate(g,(x,a,b))

            # Asignamos el valor de la integral a el label que mostrara el resultado
            result_text = f"{integral:.4f}" if integral.is_finite else "😶‍🌫️ La integral exacta no es un número finito."
            self.lbl_valorexacto.setText(result_text)
    
        except ValueError:
            self.entradadedatos.setText("⛔ Entrada inválida")
     
     # Creando la función para calcular la diferencia en trapecio
    
    # Creando la funcion para calcular la diferencia en cuanto al trapecio
    def calcularDiferenciaTrapecio(self):
        try:
            valor_exacto = float(self.lbl_valorexacto.text())
            resultado_trapecio = float(self.lbl_resultTrap.text()[1:])  # Se omite el primer caracter "="

            diferencia = abs(resultado_trapecio - valor_exacto)
            self.lbl_diference.setText(f"Trap: {diferencia:.4f}")
        
        except ValueError:
            self.lbl_diference.setText("")
    
    # Creando la funcion para calcular la diferencia en cuanto al Simpson
    def calcularDiferenciaSimpson(self):
        
        try:
            valor_exacto = float(self.lbl_valorexacto.text())
            resultado_simpson = float(self.lbl_resultSimp.text()[1:])  # Se omite el primer caracter "="

            diferencia = abs(resultado_simpson - valor_exacto)
            self.lbl_diference.setText(f"Simp: {diferencia:.4f}")
        
        except ValueError:
            self.lbl_diference.setText("")

# Abre y cierra la interfaz gráfica de la calculadora
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Calculadora()
    GUI.show()
    sys.exit(app.exec_())