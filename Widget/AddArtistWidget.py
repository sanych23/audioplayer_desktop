from PySide6 import QtCore, QtWidgets
from vendor.database import DbORM
from Events import EventsAddArtist
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QFileDialog, QComboBox, QCheckBox

class AddArtistWidget(QtWidgets.QWidget, EventsAddArtist):
    database = DbORM()

    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        self.main_layout = QtWidgets.QFormLayout(self)

    def input_stage_name(self):
        self.input_name = QLineEdit()
        name_label = QLabel("Введите имя артиста:")
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_name)
        return self

    def btn_add_artist(self):
        artist_button = QPushButton("Добавить")
        self.main_layout.addWidget(artist_button)
        artist_button.clicked.connect(self.new_artist)
        return self
