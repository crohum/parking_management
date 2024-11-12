"""
Hacer un programa que calcule el total a pagar de carios clientes que usan el estacionamiento.

El programa debe de solicitar por teclado:
    - La placa del vehiculo.
    - Tipo de estacionamiento.

Los tios de estacionamiento son:
    * POR HORA, con un costo de $3USD por hora.
    * MEDIA JORNADA, con un costo fijo de $15USD por hora, pero con 5% de descuento.
    * JORNADA COMPLETA, con un costo fijo $30USD por hora, pero con 10% de descuento.

El programa debe calcular el monto a pagar para cada cliente en funcion del tipo de estacionamiento seleccionado,
y al finalizar, debe mostrar por pantalla:
    - Cantidad total de estacionados por hora.
    - Cantidad total de estacionados por 1/2 jornada.
    - Cantidad total de estacionados po jornada completa.
    * La suma total de ingresos en USD del dia.
"""
from datetime import datetime


def buscar_placa(placa: str):
    global ESTACIONADOS
    ahorita = (datetime.now())
    if placa in ESTACIONADOS.keys():
        ESTACIONADOS[placa].append(ahorita.strftime('%m/%d/%y %H:%M:%S'))
        tiempo = ESTACIONADOS.get(placa)
        horas, monto = obtener_tiempo(tiempo)
        pasar_completos(placa, horas, monto)
    else:
        tarifa = input('ingresa la tarifa: Hrs, Half or Full')
        new_entry = [ahorita.strftime('%m/%d/%y %H:%M:%S'), tarifa]
        ESTACIONADOS[placa] = new_entry
        print(f'Fecha: {ahorita.strftime('%b/%d')}'
              f'\nHa ingresado el carro {placa} a las {ahorita.hour}:{ahorita.minute}')
        print(f'\nActualmente hay {len(ESTACIONADOS)} vehiculos en el estacionamiento')


def obtener_tiempo(tiempo):
    entrada = datetime.strptime(tiempo[0], '%m/%d/%y %H:%M:%S')
    salida = datetime.strptime(tiempo[2], '%m/%d/%y %H:%M:%S')
    duracion = salida - entrada
    horas = round(duracion.total_seconds()/60)
    monto = tarifa(horas, tiempo[1])
    return horas, monto


def tarifa(horas, modalidad):
    monto = int
    if modalidad == 'Hrs':
        monto = horas * 3
        pass
    elif modalidad == 'Half':
        monto = horas * 3 * .95
        if monto < 15:
            monto = 15
            pass
    elif modalidad == 'Full':
        monto = horas * 3 * .95
        if monto < 30:
            monto = 30
            pass
    return monto


def pasar_completos(placa, horas, monto):
    global ESTACIONADOS, COMPLETOS
    # borrar del diccionario y pasar como lista a completos
    pass


ESTACIONADOS = {}
COMPLETOS = []
running = True
# open/create a txt file for records


while running:
    PLACA = input('ingresa la placa del auto')
    buscar_placa(PLACA)


'''
*guarde cada ticket en un diccionario {placa:[datetime_in, datetime_end]}

*guarde datos en un txt con nombre igual a la fecha al cerrar ticket
datatime
os?
 

'''