import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QScrollArea, QGridLayout, QHBoxLayout
from PySide6.QtCore import QFile, QSize,QRect
from vendor.database import DataBaseConnector

class AlbumListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
       
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        
        self.scrollAreaWidgetContents = QWidget()                  
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.setGeometry(QRect(0, 0, 500, 495))     
        
        self.layout = QHBoxLayout(self.centralwidget)        
        self.layout.addWidget(self.scrollArea)
        self.addAlbumButtons()
        
        
    def addAlbumButtons(self):
        self.__connect = DataBaseConnector()
        row = 0
        column = 0
        albums = self.__connect.querySelect('SELECT id, name FROM public.album ORDER BY id')
        for item in albums:
            button = QPushButton(item['name'])
            button.setFixedSize(QSize(170, 80))
            self.gridLayout.addWidget(button ,row,column)
            column = column + 1
            if (column == 4):
                column = 0
                row = row + 1 

# app = QApplication(sys.argv)

# window = AlbumListWidget()
# window.resize(800, 600)
# window.show()
# sys.exit(app.exec())