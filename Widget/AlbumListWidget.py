import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QScrollArea, QGridLayout, QHBoxLayout, QLabel,QVBoxLayout
from PySide6.QtCore import QFile, QSize,QRect, Slot
from Events import EventsAlbumList
from vendor.database import DataBaseConnector
from Widget.SongListWidget import SongListWidget

class AlbumListWidget(QMainWindow, EventsAlbumList):
    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
       
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.label = QLabel("Список альбомов")
        
        self.scrollAreaWidgetContents = QWidget()
        self.buttons = []
                 
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.setGeometry(QRect(0, 0, 500, 495))     
        
        self.layout = QVBoxLayout(self.centralwidget)   
        self.layout.addWidget(self.label)      
        self.layout.addWidget(self.scrollArea)

        self.addAlbumButtons()
        
        
    def addAlbumButtons(self):
        self.__connect = DataBaseConnector()
        row = 0
        column = 0
        albums = self.__connect.querySelect('SELECT id, name FROM public.album ORDER BY id')
        for album in albums:
            self.buttons.append(
                {
                    'id': album['id'],
                    'btn': QPushButton(album['name'])
                }
            )
            
            self.buttons[-1]['btn'].setFixedSize(QSize(170, 80))
            self.gridLayout.addWidget(self.buttons[-1]['btn'] ,row,column)
            self.buttons[-1]['btn'].album_id = album["id"]
            self.buttons[-1]['btn'].album_name = album["name"]
            column = column + 1
            if (column == 4):
                column = 0
                row = row + 1
            self.buttons[-1]['btn'].clicked.connect(self.open_album)


    def open_album(self):
        self.album_id = self.sender().album_id
        self.album_name = self.sender().album_name
        self.song_list = SongListWidget(self, self.album_name, self.album_id)
        self.song_list.show()

    