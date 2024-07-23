from config import HOST, PASSWORD, USER, DB_NAME
import psycopg2
from datetime import datetime
import psycopg2.extras


class DataBaseConnector:
    __connection: psycopg2.connect = None
    __cursor = None

    def __init__(self) -> None:
        self.__connection = psycopg2.connect(
            dbname=DB_NAME,
            user=USER, 
            password=PASSWORD, 
            host=HOST
        )
        self.__connection.autocommit = True
        self.__cursor = self.__connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
    def querySelect(self, sql):
        self.__cursor.execute(sql)
        data = self.__cursor.fetchall()
        result = []
        for row in data:
            result.append(dict(row))
        return result

    def query(self, sql):
        self.__cursor.execute(sql)


class DbORM(DataBaseConnector):
    def __init__(self) -> None:
        super().__init__()

    def add_album(self, params: dict):
        sql = "INSERT INTO public.album "
        name_row = "("
        value_row = "("
        for key in params.keys():
            name_row += key + ","
            value_row += "'" + str(params[key])+ "'" + ","
        name_row = name_row[:-1] + ")"
        value_row = value_row[:-1] + ")"
        sql += name_row + " VALUES " + value_row
        self.query(sql)
    
    def delete_song(self, song_id: int):
        sql = f"DELETE FROM public.song WHERE song.id={song_id}; DELETE FROM public.song_album WHERE song_album.song_id={song_id};"
        self.query(sql)

    def get_all_artists(self):
        sql = "SELECT * FROM public.artist"
        data = self.querySelect(sql)
        return data
    
    def insert_music(self, params: dict):
        sql = "INSERT INTO public.song "
        name_row = "("
        value_row = "("
        for key in params.keys():
            name_row += key + ","
            value_row += "'" + str(params[key])+ "'" + ","
        name_row = name_row[:-1] + ")"
        value_row = value_row[:-1] + ")"
        sql += name_row + " VALUES " + value_row
        self.query(sql)

    def get_music_id_on_hash(self, hash_name):
        sql = f"SELECT id FROM public.song WHERE hash_name='{hash_name}'"
        return self.querySelect(sql)[0]["id"]
    
    def music_to_album(self, music_id, album_id):
        sql = f"INSERT INTO public.song_album (song_id, album_id) VALUES ({music_id}, {album_id})"
        self.query(sql)

    def music_to_artist(self, music_id, artist_id):
        sql = f"INSERT INTO public.song_artist (song_id, artist_id) VALUES ({music_id}, {artist_id})"
        self.query(sql)
