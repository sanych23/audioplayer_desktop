from Events import EventsSongList, Events
from PySide6 import QtCore, QtWidgets
from vendor.database import DbORM
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QFileDialog, QComboBox


class SongAddWidget(QtWidgets.QWidget, EventsSongList, Events):
    database = DbORM()

    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        
        self.main_layout = QtWidgets.QFormLayout(self)
        self.hide()

    def load_music(self):
        self.loader_music = QFileDialog(self)
        self.loader_music.setFileMode(QFileDialog.AnyFile)
        self.main_layout.addWidget(self.loader_music)
        return self

    def input_artist_menu(self):
        self.input_artist = QComboBox()
        artists = self.database.get_all_artists()
        for artist in artists:
            self.input_artist.addItem(f"{artist["id"]}. {artist["stage_name"]}")
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
        button.clicked.connect(self.close_add_album)
        return self

    # def input_description(self):
    #     self.input_description = QTextEdit()
    #     name_label = QLabel("Описание альбома:")
    #     self.main_layout.addWidget(name_label)
    #     self.main_layout.addWidget(self.input_description)
    #     return self

    # def input_release(self):
    #     self.input_release = QLineEdit()
    #     name_label = QLabel("Релиз альбома:")
    #     self.input_release.setPlaceholderText("ДД.ММ.ГГГГ")
    #     self.main_layout.addWidget(name_label)
    #     self.main_layout.addWidget(self.input_release)
    #     return self

    # def button_add_album(self):
    #     button = QPushButton("Добавить альбом")
    #     self.main_layout.addWidget(button)
    #     button.clicked.connect(self.add_album)
    #     return self


