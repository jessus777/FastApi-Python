import pyodbc
class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection = self.__create_database_engine()
        pass


    def __create_database_engine(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLEXPRESS;'
            'DATABASE=test_database2;'
            'Trusted_Connection=yes;'
        )
        return conn
    
    def get_connection(self):
        return self.__connection