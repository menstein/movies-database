from psycopg2 import pool


class Database:
    __connection_pool = None

    @classmethod
    def initialize(cls,**kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1,10,**kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def put_connection(cls,connection):
        return cls.__connection_pool.putconn(connection)

    # Stops the commit from going thru to any connection and closes them all
    @classmethod
    def closeall_connection(cls):
        Database.__connection_pool.closeall()

class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.put_connection(self.connection)