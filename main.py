import math
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import typing
from PyQt5 import uic
from sympy import *
from numpy import *
from sympy.parsing.sympy_parser import parse_expr

#from PyQt5.uic import loadUi

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

        #Especiales
        self.btn_multiply.clicked.connect(lambda: self.ingresarValores('*'))
        self.btn_substract.clicked.connect(lambda: self.ingresarValores('-'))
        self.btn_sum.clicked.connect(lambda: self.ingresarValores('+'))
        self.btn_divide.clicked.connect(lambda: self.ingresarValores('/'))
        self.btn_leftbracket.clicked.connect(lambda: self.ingresarValores('('))
        self.btn_rightbracket.clicked.connect(lambda: self.ingresarValores(')'))
        self.btn_ln.clicked.connect(lambda: self.logaritmoNatural())
        self.btn_result.clicked.connect(lambda: self.ingresarValores('='))
        self.btn_root.clicked.connect(lambda: self.squaredRoot())
        self.btn_trapeze.clicked.connect(lambda: self.integralexacta())
        self.btn_trapeze.clicked.connect(lambda: self.integralTrapecio())
        self.btn_simpson.clicked.connect(lambda: self.integralSimsom())
        self.btn_cleaner.clicked.connect(lambda: self.limpiarTodo())

        # Definir la expresión regular para permitir solo 'x', números y los operadores +, -, *, /
        regex = QRegExp('[x0-9+\\-*/\\s()]+')
        validacion = QRegExpValidator(regex)
        self.entradadedatos.setValidator(validacion)
        self.txtLimite_Inferior.setValidator(validacion)
        self.txtLimite_Superior.setValidator(validacion)

        #Validar los datos que pongan en n
        regla = QRegExp('[0-9]')
        validacion2 = QRegExpValidator(regla)
        self.txtSubintervalos.setValidator(validacion2)

    #Creando la funcion para ingresar los datos
    def ingresarValores(self, tecla):
        if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.' or tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
            self.entradadedatos.setText(self.entradadedatos.text() + tecla)

        if tecla == '=':
            resultado = eval(self.entradadedatos.text())
            self.entradadedatos.setText(str(resultado))

    #Creando las operaciones cabronas  
    def squaredRoot(self):
        try:
            valor_entrada = float(self.entradadedatos.text())
            
            if valor_entrada < 0:
                self.entradadedatos.setText("Entrada inválida")  # Mostrar un mensaje de error para entradas negativas
            else:
                resultado = math.sqrt(valor_entrada)
                self.entradadedatos.setText(str(resultado))

        except ValueError:
            self.entradadedatos.setText("Entrada inválida")  # Mostrar un mensaje de error para entradas no numéricas

    #Creando la otra función para la calcular la integral por el trapecio
    def integralTrapecio(self):
        x = symbols('x') #declarar la variable simbolica x
        
        # Verificar si los campos de límites y subintervalos no están vacíos
        if not self.txtLimite_Inferior.text() or not self.txtLimite_Superior.text() or not self.txtSubintervalos.text():
            self.lbl_resultTrap.setText("Error: Ingrese todos los límites y el número de subintervalos.")
            return
        
        a = float(self.txtLimite_Inferior.text())
        b = float(self.txtLimite_Superior.text())
        n = int(self.txtSubintervalos.text())
        funcion_introducida = self.entradadedatos.text()

        # Convertir la función a una función numérica
        funcion = lambdify(x, funcion_introducida)

        # Calcular los puntos (x, y) para el método del trapecio
        puntos_x = [a + i * (b - a) / n for i in range(n + 1)]
        puntos_y = [funcion(x_val) for x_val in puntos_x]

        # Calcular la aproximación de la integral utilizando el método del trapecio
        aprox_integral_trap = trapz(puntos_y, puntos_x)
        self.lbl_resultTrap.setText(f"= {aprox_integral_trap:.4f}")


    # **! Modificación Alexander

    def integralSimsom(self):
        x = symbols('x')
        a = float(self.txtLimite_Inferior.text())
        b = float(self.txtLimite_Superior.text())
        n = int(self.txtSubintervalos.text())
        funcion_Introducida = self.entradadedatos.text()

        funcion = lambdify(x, funcion_Introducida)

        if n % 2 != 0:
            self.lbl_resultSimp.setText("Error!ld El número de subintervalos debe ser par para el método de Simpson.")
            return
        
        h = (b - a) / n
        x_vals = [a + i * h for i in range(n+1)]
        y_vals = [funcion(x_val) for x_val in x_vals]
    
        suma_pares = sum(y_vals[2:n-1:2])
        suma_impares = sum(y_vals[1:n:2])
    
        integral_aprox = (h / 3) * (y_vals[0] + 4 * suma_impares + 2 * suma_pares + y_vals[n])

        self.lbl_valorexacto.setText(f"{integral_aprox:.4f}")
        self.lbl_resultSimp.setText(f"= {integral_aprox:.4f}")
    

    # **!Creando función de lograritmo natural (ln)

    def logaritmoNatural(self):
        self.lbl_resultSimp.setText("Ln Conectado")
        return 0
    

    #Creando la funcion para la integral exacta
    def integralexacta(self):
        x = symbols('x') #declarar la x
        a = float(self.txtLimite_Inferior.text())
        b = float(self.txtLimite_Superior.text())
        funcion_introducida = self.entradadedatos.text()
        g = parse_expr(funcion_introducida)
        integral = integrate(g,(x,a,b))
        self.lbl_valorexacto.setText(f"{integral:.4f}")
    
    def limpiarTodo(self):
        self.txtLimite_Inferior.setText("")
        self.txtLimite_Superior.setText("")
        self.txtSubintervalos.setText("")
        self.entradadedatos.setText("")
        self.lbl_resultTrap.setText("=")
        self.lbl_resultSimp.setText("=")
        self.lbl_valorexacto.setText("")
        self.lbl_diference.setText("")

#Abre la interfaz gráfica de la calculadora
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Calculadora()
    GUI.show()
    sys.exit(app.exec_())