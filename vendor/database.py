from config import HOST, PASSWORD, USER, DB_NAME
import psycopg2
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
        self.__cursor.execute (sql)


class DbORM(DataBaseConnector):
    def __init__(self) -> None:
        super().__init__()

    
