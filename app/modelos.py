from collections import defaultdict


PAQUETE_PRECIO_ENVIO = 10


class Cliente:
    def __init__(self, cuit):
        self.cuit = cuit


class Paquete:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha


class Aerolinea:
    def __init__(self, nombre):
        self.nombre = nombre
        self._bodega = defaultdict(list)
        self._clientes = []
        self._paquete_precio_envio = PAQUETE_PRECIO_ENVIO

    def cliente_agregar(self, cliente):
        self._clientes.append(cliente)

    def paquete_agregar(self, paquete):
        if paquete.cliente not in self._clientes:
            raise Exception('El paquete es de un cliente desconocido')

        self._bodega[paquete.fecha].append(paquete)

    def reporte_paquetes_por_dia(self, fecha):
        paquetes = self._bodega[fecha]

        paquetes_cantidad = len(paquetes)
        recaudacion = self._paquete_precio_envio * paquetes_cantidad

        return (paquetes_cantidad, recaudacion)
