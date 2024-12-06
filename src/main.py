from src import models, data_base

def agregar_cliente(cliente: models.Cliente):
    query = "INSERT INTO Clientes (nombre, email, telefono) VALUES (?, ?, ?) RETURNING idCliente;"
    cursor = data_base.execute_query(query, (cliente.nombre, cliente.email, cliente.telefono))
    try:
        return {"idCliente": cursor.fetchone()[0]}
    finally:
        cursor.close()  # Asegúrate de cerrar el cursor aquí

def agregar_servicio(servicio: models.Servicio):
    query = "INSERT INTO Servicios (descripcion, precio) VALUES (?, ?) RETURNING idServicios;"
    cursor = data_base.execute_query(query, (servicio.descripcion, servicio.precio))
    try:
        return {"idServicios": cursor.fetchone()[0]}
    finally:
        cursor.close()

def agregar_habitacion(habitacion: models.Habitacion):
    query = """INSERT INTO Habitaciones (numero, tipo, estado, precioPorNoche, precioPorDia)
               VALUES (?, ?, ?, ?, ?) RETURNING idHabitacion;"""
    cursor = data_base.execute_query(query, (habitacion.numero, habitacion.tipo, habitacion.estado, 
                                   habitacion.precio_por_noche, habitacion.precio_por_dia))
    try:
        return {"idHabitacion": cursor.fetchone()[0]}
    finally:
        cursor.close()

def agregar_reserva(reserva: models.Reserva):
    query = """INSERT INTO Reservas (idCliente, fechaReserva, duracionEstancia, estadoReserva, montoTotal)
               VALUES (?, ?, ?, ?, ?) RETURNING idReserva;"""
    cursor = data_base.execute_query(query, (reserva.id_cliente, reserva.fecha_reserva, reserva.duracion_estancia, 
                                   reserva.estado_reserva, reserva.monto_total))
    try:
        return {"idReserva": cursor.fetchone()[0]}
    finally:
        cursor.close()

def agregar_factura(factura: models.Factura):
    query = """INSERT INTO Facturas (numeroFactura, fechaEmision, monto, estadoPago, subtotal, total, idReserva)
               VALUES (?, ?, ?, ?, ?, ?, ?) RETURNING idFactura;"""
    cursor = data_base.execute_query(query, (factura.numero_factura, factura.fecha_emision, factura.monto,
                                   factura.estado_pago, factura.subtotal, factura.total, factura.id_reserva))
    try:
        return {"idFactura": cursor.fetchone()[0]}
    finally:
        cursor.close()

def agregar_pago(pago: models.Pago):
    query = """INSERT INTO Pagos (fechaPago, cantidad, idFactura) VALUES (?, ?, ?) RETURNING idPago;"""
    cursor = data_base.execute_query(query, (pago.fecha_pago, pago.cantidad, pago.id_factura))
    try:
        return {"idPago": cursor.fetchone()[0]}
    finally:
        cursor.close()
