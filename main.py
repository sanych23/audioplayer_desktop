import sys
import random
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QDialogButtonBox, QGridLayout, QSlider
from vendor.database import DataBaseConnector
from Widget.AlbumListWidget import AlbumListWidget

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.__connect = DataBaseConnector()
        self.album_list = AlbumListWidget()
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.album_list)

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
