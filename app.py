from fastapi import FastAPI
from src import models, main
import uvicorn
import logging

logger = logging.getLogger("uvicorn.error")

app = FastAPI(debug=True)

try:
    @app.post("/clientes")
    def api_agregar_cliente(cliente: models.Cliente):
        return main.agregar_cliente(cliente)

    @app.post("/servicios")
    def api_agregar_servicio(servicio: models.Servicio):
        return main.agregar_servicio(servicio)

    @app.post("/habitaciones")
    def api_agregar_habitacion(habitacion: models.Habitacion):
        return main.agregar_habitacion(habitacion)

    @app.post("/reservas")
    def api_agregar_reserva(reserva: models.Reserva):
        return main.agregar_reserva(reserva)

    @app.post("/facturas")
    def api_agregar_factura(factura: models.Factura):
        return main.agregar_factura(factura)

    @app.post("/pagos")
    def api_agregar_pago(pago: models.Pago):
        return main.agregar_pago(pago)

    @app.get("/")
    def home():
        return {"message": "API para Reservas de Hotel funcionando ..."}
except Exception as e:
    print(f"Error en los enpoints, {e}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=9999, reload=True)