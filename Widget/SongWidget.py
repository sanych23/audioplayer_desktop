from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QScrollArea, QGridLayout, QHBoxLayout, QLabel,QVBoxLayout
from PySide6.QtCore import QFile, QSize,QRect
from Events import Events, EventsSongList
from Widget.MusicWidget import MusicWidget
from Widget.SongAddWidget import SongAddWidget


class SongWidget(QMainWindow, EventsSongList, Events):

    def __init__(self, parent, album_name, album_id):
        super().__init__()
        self.parent_window = parent
        self.album_id = album_id

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.top_layout = QHBoxLayout()
        self.back_button = QPushButton("Назад")
        self.back_button.setFixedSize(QSize(80, 30))
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.label = QLabel("Список песен")
        self.name_album = QLabel(album_name)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.setGeometry(QRect(0, 0, 500, 495))   
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.addLayout(self.top_layout)
        self.top_layout.addWidget(self.back_button)
       
        self.top_layout.addWidget(self.name_album)
        self.layout.addWidget(self.label)      
        self.layout.addWidget(self.scrollArea)

        self.add_song_button()

        self.back_button.clicked.connect(self.close_song_widget)
        self.get_song_list(album_id)

        self.resize(800, 600)

        # self.add_song_widget = SongAddWidget(self).input_song_name().input_artist_menu().load_music().button_add_music().button_close_widget()


    def add_song_button(self):
        button_add_song = QPushButton("Добавить песню")
        button_add_song.clicked.connect(self.display_widget_add_song)
        self.layout.addWidget(button_add_song)

    def get_song_list(self, album_id):
        data = self.database.querySelect(f"""SELECT 
                                                album.id AS album_id,
                                                album.name AS album_name,
                                                song.id AS song_id,
                                                song.name AS song_name,
                                                song.hash_name as hash_name
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
        print(data)
        if(not data):
            self.none_label = QLabel("Альбом пуст, добавте песни")
            self.gridLayout.addWidget(self.none_label)
        else:
            for item in data:
                self.song_item_widget = MusicWidget(item)
                self.song_item_widget.setFixedHeight(100)
                self.gridLayout.addWidget(self.song_item_widget)
                self.gridLayout.addStretch()
                



# app = QApplication(sys.argv)

# window = SongWidget()
# window.resize(800, 600)
# window.show()
# sys.exit(app.exec())