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
        from Widget.SongAddWidget import SongAddWidget
        self.add_song_widget = SongAddWidget(self).input_song_name().input_artist_menu().load_music().button_add_music().button_close_widget()
        self.add_song_widget.resize(350, 250)
        self.hide()

    def get_file_name(self):
        worker = QFileDialog(self)
        self.file_name = worker.getOpenFileName()
        self.hash_name = hash(datetime.now())
        self.music_name = self.file_name[0].split('/')[-1].split('.')[0]
        

    def add_music(self):
        data = {
            "name": self.input_name.text(),
            "hash_name": self.hash_name
        }
        
        self.database.insert_music(data)
        id = self.database.get_music_id_on_hash(data["hash_name"])
        author_id = self.input_artist.currentData()["id"]

        self.database.music_to_artist(id, author_id)
        self.database.music_to_album(id, self.parent_window.album_id)


        shutil.copyfile(self.file_name[0], f"music/{self.hash_name}.mp3")
        self.parent_window.rerender_music_list()
        # self.parent_window.parent_window.open_album()
        self.parent_window.show()
        self.close()



    # def close_song_widget(self):
    #     pass
