from .connection import DBConnectionHandler

def test_get_engine_conection():
    db_connection_handler = DBConnectionHandler()
    engineConection = db_connection_handler.get_connection()
    print()
    print(engineConection)