from Events import EventsAddArtist
from PySide6 import QtCore, QtWidgets
from vendor.database import DbORM
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QFileDialog, QComboBox, QCheckBox

class AddArtistWidget(EventsAddArtist):
    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        
        self.main_layout = QtWidgets.QFormLayout(self)
        self.show()

    def input_stage_name(self):
        self.input_name = QLineEdit()
        name_label = QLabel("Введите имя артиста:")
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_name)
        return self

    def btn_add_artist(self):
        button = QPushButton("Добавить")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.add_artist)
        return self
