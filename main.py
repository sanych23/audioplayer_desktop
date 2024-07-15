import sys
import random
from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        
        

        self.layout = QtWidgets.QVBoxLayout(self)
        

    def init_button(self):
        self.button = QtWidgets.QPushButton("Click me!")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    def init_textarea(self):
        self.layout.addWidget(self.text)
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

    def magic(self):
        self.text.setText(random.choice(self.hello))
        
        



app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec())
