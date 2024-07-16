import sys
import random
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QDialogButtonBox, QGridLayout, QSlider
from Helper.FlowLayout import FlowLayout
from vendor.database import DataBaseConnector


class MainWindow(QtWidgets.QWidget):
    num_buttons = 15

    def __init__(self):
        super().__init__()
        self.__connect = DataBaseConnector()
        self.create_album_list_box()
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self._album_group_box)


    def create_album_list_box(self):
        albums = self.__connect.querySelect('SELECT id, name FROM public.album ORDER BY id')
        self._album_group_box = QGroupBox("Cписок альбомов")
        flow_layout = FlowLayout(self) # layout для переноса кнопок)
        for album in albums:
            button = QPushButton(f"{album['name']}")
            button.setFixedSize(QtCore.QSize(190, 80))
            flow_layout.addWidget(button)
        self._album_group_box.setLayout(flow_layout)

    def generateAlbumSong(self, album_id):
        data = self.__connect.querySelect(f"""SELECT 
                                                album.id AS album_id,
                                                album.name AS album_name,
                                                song.id AS song_id,
                                                song.name AS somg_name
                                            FROM
                                                public.album
                                            INNER JOIN
                                                public.song_album
                                            ON
                                                album.id = song_album.album_id
                                            INNER JOIN
                                                public.song
                                            ON
                                                song_album.song_id = song.id
                                            WHERE 
                                                album_id = {album_id}""")
        return data
    
app = QtWidgets.QApplication([])

widget = MainWindow()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec())
