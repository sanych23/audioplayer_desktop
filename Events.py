from vendor.database import DbORM
from Helper.Validator import Validator
from PySide6.QtWidgets import QFileDialog
from datetime import datetime
import shutil

class Events:
    database = DbORM()

    def open_add_album(self):
        self.hide()
        self.add_album_wiget.show()

    def close_add_album(self):
        self.parent_window.show()
        self.hide()
    
    def close_song_widget(self):
        self.parent_window.show()
        self.hide()

    def add_album(self):
        name = self.input_name.text()
        description = self.input_description.toPlainText()
        release_date = self.input_release.text()

        if Validator.check_album_data({
            "name": name,
            "description": description,
            "release_date": release_date,
        }):
            self.database.add_album({
                "name": name,
                "description": description,
                "release_date": release_date,
            })
        self.hide()
        self.parent_window.album_list.addAlbumButtons()
        self.parent_window.show()


    def get_song_list(self, album_id):
        data = self.database.querySelect(f"""SELECT 
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


class EventsSongList:
    def display_widget_add_song(self):
        self.hide()
        self.add_song_widget.show()

    def get_file_name(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls);; Image File (*.png *.jpg)'
        # response = QFileDialog.getOpenFileName(
        #     parent=self,
        #     caption='Select a file',
        #     directory='C:/Users/PC/Desktop/projects/audioplayer_pyside/music',
        #     filter=file_filter,
        #     initialFilter='Excel File (*.xlsx *.xls)'
        # )
        # self.textbox.setText(str(response))
        worker = QFileDialog(self)
        # response.setFileMode(QFileDialog.ExistingFile)
        # print(response)
        # response.getSaveFileName(self, ("Save File"),()
        #                    "/home/jana/untitled.png",
        #                    ("Images (*.png *.xpm *.jpg)"))
        # self.textbox.setText(str(response))
        file_name = worker.getOpenFileName()
        self.hash_name = hash(datetime.now())
        # print(file_name)
        self.music_name = file_name[0].split('/')[-1].split('.')[0]
        # worker.saveFileContent(
        #     parent=self,
        #     caption=file_name[0],
        # )

        shutil.copyfile(file_name[0], f"music/{self.hash_name}.mp3")

        # print(self.music_name)


    # def close_song_widget(self):
    #     pass
