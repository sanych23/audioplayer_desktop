import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QScrollArea, QGridLayout, QHBoxLayout, QLabel,QVBoxLayout
from PySide6.QtCore import QFile, QSize,QRect, Slot
from Events import EventsAlbumList

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
        
        
    