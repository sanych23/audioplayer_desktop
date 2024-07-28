from Events import EventsSongList, Events
from Widget.AddArtistWidget import AddArtistWidget
from PySide6 import QtCore, QtWidgets
from vendor.database import DbORM
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QFileDialog, QComboBox, QCheckBox
from PySide6 import QtGui


class QCustomComboBox (QComboBox):
    select_data   = list()
    CHECK_QICON   = QtGui.QIcon.fromTheme('')
    UNCHECK_QICON = QtGui.QIcon.fromTheme('contact-new')

    def __init__(self, artists: list, *args, **kwargs):
        super(QCustomComboBox, self).__init__(*args, **kwargs)
        listsItem = artists
        for index in range(0, len(listsItem)):
            self.addItem(listsItem[index]['stage_name'], userData=listsItem[index])
            self.setItemIcon(index, self.UNCHECK_QICON)
        self.activated.connect(self.customActivated)

    def hidePopup (self):
        pass

    def customActivated (self, index):
        stateQIcon = self.itemIcon(index)
        newQIcon = {
            self.CHECK_QICON.name()   : self.UNCHECK_QICON,
            self.UNCHECK_QICON.name() : self.CHECK_QICON,
        } [stateQIcon.name()]
        self.setItemIcon(index, newQIcon)
        data = self.export()

        flag = True
        for item in data:
            for select_item in self.select_data:
                if select_item == item[2]:
                    self.select_data.remove(select_item)
                    flag = False

        if flag:
            self.select_data.append(data[0][2])

    def export (self):
        listsExportItem = []
        for index in range(0, self.count()):
            stateQIcon = self.itemIcon(index)
            state = {
                self.CHECK_QICON.name()   : True,
                self.UNCHECK_QICON.name() : False,
            } [stateQIcon.name()]
            listsExportItem.append([str(self.itemText(index)), state, self.currentData()])
        return listsExportItem
    
    def export_check_data(self):
        return self.select_data


class SongAddWidget(QtWidgets.QWidget, EventsSongList, Events):
    database = DbORM()

    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        self.add_artist_widget = AddArtistWidget(self).input_stage_name().btn_add_artist()
        self.add_artist_widget.hide()
        self.main_layout = QtWidgets.QFormLayout(self)
        self.show()
        

    def load_music(self):
        self.button_music = QPushButton("Выбрать песню")
        self.main_layout.addWidget(self.button_music)
        self.button_music.clicked.connect(self.get_file_name)
        return self

    def input_artist_menu(self, params=False):
        name_label = QLabel("Выберите исполнителя:")
        self.all_artists = self.database.get_all_artists()
        self.input_artist = QCustomComboBox(self.all_artists)
        if params:
            return self.input_artist
        self.main_layout.addWidget(name_label)
        self.main_layout.addWidget(self.input_artist)
        return self

    def add_new_artist(self):
        button = QPushButton("Добавить нового артиста")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.add_artist)
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
        self.button_add = QPushButton("Добавить песню")
        self.main_layout.addWidget(self.button_add)
        self.button_add.clicked.connect(self.add_music)
        self.button_add.hide()
        return self


