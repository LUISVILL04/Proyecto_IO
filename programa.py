from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

primera = uic.loadUi("\gui io\pantallaPrincipal.ui") # cargo las interfaces
valores = uic.loadUi("\gui io\ingresarvalores.ui")


def ventana1(): 
    primera.hide() #cerramos la ventana principal
    valores.show()  # abrimos la ventana de los valores
    
def suma(): # retorna la suma de dos numeros recibidos en los recuadros
    num1 = float(valores.textEdit.text()) #esto cuando recibe una caden vacia no lo puede convertir a un tipo numerico
    num2 = float(valores.textEdit_2.text())
    
    if len(num1) == 0 or len(num2) == 0:
        valores.mensaje.setText(" No seas cacorro, ingresa numeros!!!")
        
    return num1 + num2

def calcular():
    valor = str(suma()) # obtiene el valor que retorna la funcion suma y lo convierte a string
    valores.textEdit_3.setText(valor) # manda el valor que se convirtio en la linea anterior hacia el recuadro de la iterfaz

primera.boton1.clicked.connect(ventana1)  # cuando presiono el boton maximizar (boton prueba) hace el llamdado a la funcion ventana1
valores.calcular.clicked.connect(calcular) # cuando presiono el boton calcular, hace el llamado a la funcion calcular





primera.show() #mantiene la primera ventana abierta
app.exec()  # mantiene el rpograma ejecutandose en ciclo infinito hasta darle cerrar