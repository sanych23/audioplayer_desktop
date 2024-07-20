from vendor.database import DbORM

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

        self.database.add_album({
            "name": name,
            "description": description,
            "release_date": release_date,
        })
        self.hide()
        self.parent_window.album_list.addAlbumButtons()
        self.parent_window.show()

    # def open_song_list(self, album_id):
    #     self.data = self.get_song_list(self.sender().album_id)
    #     return self.data

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
