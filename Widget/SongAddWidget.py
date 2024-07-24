from Events import EventsSongList, Events
from PySide6 import QtCore, QtWidgets
from vendor.database import DbORM
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QFileDialog, QComboBox, QCheckBox

class SongAddWidget(QtWidgets.QWidget, EventsSongList, Events):
    database = DbORM()

    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        
        self.main_layout = QtWidgets.QFormLayout(self)
        self.show()
        

    def load_music(self):
        button = QPushButton("Выбрать песню")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.get_file_name)
        return self

    def input_artist_menu(self):
        self.input_artist = QComboBox()
        # self.input_artist.activated()
        
        name_label = QLabel("Выберите исполнителя:")
        artists = self.database.get_all_artists()
        for artist in artists:
            self.input_artist.addItem(f"{artist["stage_name"]}", userData=artist)
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_artist)
        return self

    def input_song_name(self):
        self.input_name = QLineEdit()
        name_label = QLabel("Название песни:")
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_name)
        return self

    def button_close_widget(self):
        button = QPushButton("Назад")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.close_add_music)
        return self
    
    def button_add_music(self):
        button = QPushButton("Добавить песню")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.add_music)
        return self



