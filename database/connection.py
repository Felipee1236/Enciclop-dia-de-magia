from mysql.connector import MySQLConnection

HOST = 'localhost'
USER = 'root'
PASSWORD = '9831Lipe.'

def get_connection(database: str = 'enciclopediaMagias') -> MySQLConnection:
    try:
        connection = MySQLConnection(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=database
        )
        
        return connection
    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

