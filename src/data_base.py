import pyodbc
from fastapi import HTTPException

DB_CONFIG = {
    "driver": "{PostgreSQL Unicode}",
    "server": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "Ps.2024$",
    "database": "Reservas_Hotel"
}

def get_db_connection():
    try:
        conn = pyodbc.connect(
            f"Driver={DB_CONFIG['driver']};"
            f"Server={DB_CONFIG['server']};"
            f"Port={DB_CONFIG['port']};"
            f"Database={DB_CONFIG['database']};"
            f"Uid={DB_CONFIG['user']};"
            f"Pwd={DB_CONFIG['password']};"
            "Sslmode=disable;"
        )
        print("Conexion con la base de datos exitoso")
        return conn
    except Exception as e:
        print("")
        #raise HTTPException(status_code=500, detail=f"Error al conectar con la base de datos: {e}")

def execute_query(query: str, params: tuple = ()):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        print("Creado correctamente")
        return cursor  # Devuelve el cursor para que sea gestionado después
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ejecutar la consulta: {e}")