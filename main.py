import sys
import random
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()\
        
        
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.title =  QtWidgets.QLabel("Cписок альбомов",
                                     alignment=QtCore.Qt.AlignHCenter)
        self.main_layout.addWidget(self.title)

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec())

