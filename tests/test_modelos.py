from datetime import date

import pytest

from app.modelos import Aerolinea, Cliente, Paquete


@pytest.mark.parametrize('cuit', ['20-31176355-6', '20-11222333-7'])
def test_cliente_crear_ok(cuit):
    cli = Cliente(cuit)
    assert cli.cuit == cuit


def test_cliente_crear_fail():
    with pytest.raises(TypeError):
        Cliente()


def test_paquete_crear_ok():
    cli = Cliente('20-31176355-6')
    fecha = date.today()
    paq = Paquete(cli, fecha)

    assert isinstance(paq.cliente, Cliente) is True
    assert isinstance(paq.fecha, date) is True


def test_aerolinea_enviar_paquete_cliente_inexistente():
    cli = Cliente('20-31176355-6')
    fecha = date.today()
    paq = Paquete(cli, fecha)

    aerolinea = Aerolinea('Pepito')

    with pytest.raises(Exception) as e:
        aerolinea.paquete_agregar(paq)

    assert str(e.value) == 'El paquete es de un cliente desconocido'


def test_aerolinea_enviar_paquete_ok():
    cli = Cliente('20-31176355-6')
    fecha = date.today()
    paq = Paquete(cli, fecha)

    aerolinea = Aerolinea('Pepito')
    aerolinea.cliente_agregar(cli)

    aerolinea.paquete_agregar(paq)

    assert len(aerolinea._bodega[fecha]) == 1


def test_aerolinea_reporte_ok():
    cli = Cliente('20-31176355-6')
    fecha = date.today()
    paq1 = Paquete(cli, fecha)
    paq2 = Paquete(cli, fecha)
    paq3 = Paquete(cli, fecha)

    aerolinea = Aerolinea('Pepito')
    aerolinea.cliente_agregar(cli)

    aerolinea.paquete_agregar(paq1)
    aerolinea.paquete_agregar(paq2)
    aerolinea.paquete_agregar(paq3)

    cantidad, ingresos = aerolinea.reporte_paquetes_por_dia(fecha)

    assert cantidad == 3
    assert ingresos == 30
