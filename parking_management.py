"""
Hacer un programa que calcule el total a pagar de varios clientes que usan el estacionamiento.

El programa debe de solicitar por teclado:
    - La placa del vehiculo.
    - Tipo de estacionamiento.

Los tipos de estacionamiento son:
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


# Imprime el ingreso del carro
def entrada_carro(placa: str):
    global ESTACIONADOS
    ahorita = (datetime.now())

    tarifa = input('ingresa la tarifa: Hrs, Half or Full')
    new_entry = [ahorita.strftime('%m/%d/%y %H:%M:%S'), tarifa]
    ESTACIONADOS[placa] = new_entry
    print(f'Fecha: {ahorita.strftime('%b/%d')}'
          f'\n\nHa ingresado el carro {placa} a las {ahorita.hour}:{ahorita.minute}')
    print(f'\n\nActualmente hay {len(ESTACIONADOS)} vehiculos en el estacionamiento')


# Imprime el recibo de salida.
def salida_carro(placa: str):
    global ESTACIONADOS
    ahorita = (datetime.now())

    ESTACIONADOS[placa].insert(1, ahorita.strftime('%m/%d/%y %H:%M:%S'))
    tiempo = ESTACIONADOS.get(placa)
    horas, monto = obtener_tiempo(tiempo)
    pasar_completos(placa, horas, monto)
    print(f'Fecha: {ahorita.strftime('%b/%d')}'
          f'\n\nHa salido el carro {placa} a las {ahorita.hour}:{ahorita.minute}'
          f'\nestuvo durante {horas} horas'
          f'\nel monto total es de: ${monto} USD')
    print(f'\n\nActualmente hay {len(ESTACIONADOS)} vehiculos en el estacionamiento')


# Calcula el tiempo que el carro estuvo estacionado.
def obtener_tiempo(tiempo):
    entrada = datetime.strptime(tiempo[0], '%m/%d/%y %H:%M:%S')
    salida = datetime.strptime(tiempo[1], '%m/%d/%y %H:%M:%S')
    duracion = salida - entrada
    horas = round(duracion.total_seconds()/60)
    monto = tarifa(horas, tiempo[2])
    return horas, monto


# Devuelve el monto total por tipo de estacionamiento.
def tarifa(horas, modalidad):
    monto = int
    if modalidad == 'Hrs':
        monto = horas * 3
        pass
    elif modalidad == 'Half':
        monto = horas * 3
        if monto < 15:
            monto = 15 * .95
            pass
    elif modalidad == 'Full':
        monto = horas * 3
        if monto < 30:
            monto = 30 * .90
            pass
    return round(monto, 2)


# Elimina el carro de estacionados y lo pasa al registro.
def pasar_completos(placa, horas, monto):
    global ESTACIONADOS, COMPLETOS
    temp = ESTACIONADOS.pop(placa)
    temp.insert(0, placa)
    temp.append(horas)
    temp.append(monto)
    COMPLETOS.append(temp)


# Cuenta la cantidad de carros por tipo de tarifa
def resumen_dia():
    global COMPLETOS
    carros_full: int = 0
    carros_half: int = 0
    carros_hrs: int = 0
    ingresos: int = 0

    for c in COMPLETOS:
        if c[3] == 'Hrs':
            carros_hrs += 1
        elif c[3] == 'Half':
            carros_half += 1
        elif c[3] == 'Full':
            carros_full += 1
        ingresos += c[5]

    print(carros_hrs + carros_half + carros_full)
    print(carros_full)
    print(carros_half)
    print(carros_hrs)
    print(ingresos)


# INICIA EL PROGRAMA AQUI.

ESTACIONADOS = {}
COMPLETOS = []
running = True


while running:
    PLACA = input('ingresa la placa del auto')

    if PLACA in ESTACIONADOS.keys():
        salida_carro(PLACA)
    elif PLACA == '0':
        resumen_dia()
    else:
        entrada_carro(PLACA)


# MAQUETADO
