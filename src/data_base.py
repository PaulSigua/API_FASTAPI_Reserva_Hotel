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

# Función para crear las tablas
# def create_tables():
#     try:

#         # Crear cada tabla
#         for table_name, create_query in TABLES.items():
#             cursor.execute(create_query)
#             print(f"Tabla '{table_name}' creada o ya existente.")

#         conn.commit()
#     except Exception as e:
#         print(f"Error al crear las tablas: {e}")
#     finally:
#         cursor.close()
#         conn.close()

# # Sentencias SQL para la creación de tablas
# TABLES = {
#     "clientes": """
#         CREATE TABLE IF NOT EXISTS Clientes (
#             idCliente SERIAL PRIMARY KEY,
#             nombre VARCHAR(100) NOT NULL,
#             email VARCHAR(100) NOT NULL,
#             telefono VARCHAR(15) NOT NULL
#         );
#     """,
#     "habitaciones": """
#         CREATE TABLE IF NOT EXISTS Habitaciones (
#             idHabitacion SERIAL PRIMARY KEY,
#             numero INT NOT NULL,
#             tipo VARCHAR(50) NOT NULL,
#             estado BOOLEAN NOT NULL,
#             precioPorNoche DOUBLE PRECISION NOT NULL,
#             precioPorDia DOUBLE PRECISION NOT NULL
#         );
#     """,
#     "servicios": """
#         CREATE TABLE IF NOT EXISTS Servicios (
#             idServicios SERIAL PRIMARY KEY,
#             descripcion VARCHAR(200) NOT NULL,
#             precio DOUBLE PRECISION NOT NULL
#         );
#     """,
#     "reservas": """
#         CREATE TABLE IF NOT EXISTS Reservas (
#             idReserva SERIAL PRIMARY KEY,
#             idCliente INT NOT NULL REFERENCES Clientes(idCliente),
#             fechaReserva DATE NOT NULL,
#             duracionEstancia INT NOT NULL,
#             estadoReserva CHAR(1) NOT NULL,
#             montoTotal DOUBLE PRECISION NOT NULL
#         );
#     """,
#     "reserva_servicios": """
#         CREATE TABLE IF NOT EXISTS Reserva_Servicios (
#             idReserva INT NOT NULL REFERENCES Reservas(idReserva),
#             idServicio INT NOT NULL REFERENCES Servicios(idServicios),
#             PRIMARY KEY (idReserva, idServicio)
#         );
#     """,
#     "facturas": """
#         CREATE TABLE IF NOT EXISTS Facturas (
#             idFactura SERIAL PRIMARY KEY,
#             numeroFactura BIGINT NOT NULL,
#             fechaEmision DATE NOT NULL,
#             monto DOUBLE PRECISION NOT NULL,
#             estadoPago VARCHAR(20) NOT NULL,
#             subtotal DOUBLE PRECISION NOT NULL,
#             total DOUBLE PRECISION NOT NULL,
#             idReserva INT NOT NULL REFERENCES Reservas(idReserva)
#         );
#     """,
#     "pagos": """
#         CREATE TABLE IF NOT EXISTS Pagos (
#             idPago SERIAL PRIMARY KEY,
#             fechaPago DATE NOT NULL,
#             cantidad DOUBLE PRECISION NOT NULL,
#             idFactura INT NOT NULL REFERENCES Facturas(idFactura)
#         );
#     """
# }