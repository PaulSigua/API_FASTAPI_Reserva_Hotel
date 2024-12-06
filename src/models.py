from pydantic import BaseModel
from datetime import date

class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: str

class Habitacion(BaseModel):
    numero: int
    tipo: str
    estado: bool
    precio_por_noche: float
    precio_por_dia: float

class Servicio(BaseModel):
    descripcion: str
    precio: float

class Reserva(BaseModel):
    id_cliente: int
    fecha_reserva: date
    duracion_estancia: int
    estado_reserva: str
    monto_total: float

class Factura(BaseModel):
    numero_factura: int
    fecha_emision: date
    monto: float
    estado_pago: str
    subtotal: float
    total: float
    id_reserva: int

class Pago(BaseModel):
    fecha_pago: date
    cantidad: float
    id_factura: int
