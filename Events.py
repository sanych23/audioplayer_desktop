from vendor.database import DbORM
from Helper.Validator import Validator
from PySide6.QtWidgets import QFileDialog,QPushButton
from PySide6.QtCore import QSize, QUrl
import hashlib
from datetime import datetime
import shutil
import os


class Events:
    database = DbORM()
    def close_song_widget(self):
        self.parent_window.parent_window.show()
        if self.playing_music:
            self.playing_music.stop_btn()
        self.parent_window.show()
        self.destroy()
        
    def delete_song(self):
        self.song_id = self.sender().song_id 
        self.database.delete_song(self.song_id) 
        for item in self.parent_window.music_widgets: 
            print(item.player) 
            item.player = None 
        print("Stop playing music!") 
        hash_name = str(self.song_info["hash_name"])
        self.parent_window.destroy() 
        self.destroy() 
        os.remove(f"music/{hash_name}.mp3")
        self.parent_window.parent_window.open_album(self.song_info['album_id'], self.song_info['album_name'])


    def get_song_list(self, album_id):
        data = self.database.querySelect(f"""SELECT 
                                                album.id AS album_id,
                                                album.name AS album_name,
                                                song.id AS song_id,
                                                song.name AS song_name,
                                                song.hash_name AS hash_name
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

class EventsAlbumList:
    database = DbORM()
    def addAlbumButtons(self):
        row = 0
        column = 0
        albums = self.database.querySelect('SELECT id, name FROM public.album ORDER BY id')
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
        
    def open_album(self, album_id=None, album_name=None):
        from Widget.SongListWidget import SongListWidget
        if(not album_id or not album_name):
            self.album_id = self.sender().album_id
            self.album_name = self.sender().album_name
        else:
            self.album_id = album_id
            self.album_name = album_name
        self.song_list = SongListWidget(self, self.album_name, self.album_id)
        self.song_list.show()

    def open_add_album(self):
        self.hide()
        self.add_album_wiget.show()

    def close_add_album(self):
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


class EventsAddArtist:
    pass


class EventsSongList:
    def display_widget_add_song(self):
        if self.playing_music:
            self.playing_music.player.stop()
        from Widget.SongAddWidget import SongAddWidget
        self.add_song_widget = SongAddWidget(self).input_song_name().input_artist_menu().add_new_artist().load_music().button_add_music().button_close_widget()
        self.add_song_widget.resize(350, 250)
        self.close()

    def add_artist(self):
        self.hide()
        from Widget.AddArtistWidget import AddArtistWidget
        widget_add_artist = AddArtistWidget().input_stage_name().btn_add_artist()
        widget_add_artist.show()
        widget_add_artist.resize(350, 250)
        

    def get_file_name(self):
        self.worker = QFileDialog(self)
        self.file_name = self.worker.getOpenFileName()
        self.hash_name = hashlib.md5(repr(datetime.now()).encode()).hexdigest()
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
        self.parent_window.get_song_list(self.parent_window.album_id)
        self.file_name = self.worker.close()
        self.parent_window.parent_window.rerender_song_list()
        self.destroy()

    def close_add_music(self):
        self.hide()
        self.parent_window.show()

class EventMusicWidget:
    database = DbORM()
    def get_artist_list(self, song_id):
        artists = self.database.querySelect(f"""SELECT
                                                    song_artist.song_id AS song_id,
                                                    artist.stage_name AS artist_name
                                                FROM
                                                    public.song_artist
                                                INNER JOIN
                                                    public.artist
                                                ON
                                                     song_artist.artist_id = artist.id
                                                WHERE
                                                    song_artist.song_id = {song_id}""")
        
        if(len(artists) == 1):
            artist = artists[0]['artist_name']
            return artist
        artists_list = ", ".join([item['artist_name'] for item in artists])
        return artists_list
