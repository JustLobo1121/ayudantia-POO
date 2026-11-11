from PyQt6 import QtWidgets

# Crear la aplicación Qt como tal
app = QtWidgets.QApplication([])

# Inicio de lógica

# Un widget es la base de todo

# Caja de texto
widget = QtWidgets.QWidget()
texto = QtWidgets.QLabel(widget)
texto.setText("esta es una prueba")

# Modificar tamaño de widget
widget.setFixedSize(400, 300)
# Más grande
# widget.setFixedSize(800, 600)

# Mostrar el widget
widget.show()

# Fin de lógica

# Ejecutar la aplicación
# Esto va al final.
app.exec()
