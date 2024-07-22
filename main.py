import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import (QAction,QFont,QIcon)
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QTextEdit
from vendor.database import DataBaseConnector
from Widget.AlbumListWidget import AlbumListWidget
from Events import Events
import Lib.Interface.resources


class MainWindow(QtWidgets.QWidget, Events):
    def __init__(self):
        super().__init__()
        
        self.__connect = DataBaseConnector()
        self.album_list = AlbumListWidget()
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.album_list)

        self.button_open_add_album()
        self.widget_add_album()


    def widget_add_album(self):
        self.add_album_wiget = AddAlbumWindow(self).input_album_name().input_description().input_release().button_add_album().button_close_widget()
        self.add_album_wiget.hide()
        self.add_album_wiget.resize(400, 400)


    def button_open_add_album(self):
        button = QPushButton("Добавить альбом")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.open_add_album)


class AddAlbumWindow(QtWidgets.QWidget, Events):
    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        self.main_layout = QtWidgets.QFormLayout(self)
        

    def input_album_name(self):
        self.input_name = QLineEdit()
        name_label = QLabel("Имя альбома:")
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_name)
        return self

    def button_close_widget(self):
        button = QPushButton("Назад")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.close_add_album)
        return self

    def input_description(self):
        self.input_description = QTextEdit()
        name_label = QLabel("Описание альбома:")
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_description)
        return self

    def input_release(self):
        self.input_release = QLineEdit()
        name_label = QLabel("Релиз альбома:")
        self.input_release.setPlaceholderText("ДД.ММ.ГГГГ")
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_release)
        return self

    def button_add_album(self):
        button = QPushButton("Добавить альбом")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.add_album)
        return self


app = QtWidgets.QApplication([])

widget = MainWindow()
widget.resize(1000, 600)
widget.show()

sys.exit(app.exec())
