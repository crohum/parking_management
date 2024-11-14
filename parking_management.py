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
import tkinter
from tkinter import *
from datetime import datetime
from estilos import Color, TextColor, Fonts


def buscar_placa():
    global var_placa_text, ESTACIONADOS
    placa = str(var_placa_text.get())

    if placa in ESTACIONADOS.keys():
        salida_carro(placa)
    elif placa == '0':
        resumen_dia()
    else:
        entrada_carro(placa)


# Imprime el ingreso del carro
def entrada_carro(placa: str):
    global ESTACIONADOS
    ahorita = (datetime.now())
    tarifa = revisar_checks()

    if tarifa == 'stop':
        pass
    else:
        new_entry = [ahorita.strftime('%m/%d/%y %H:%M:%S'), tarifa]
        ESTACIONADOS[placa] = new_entry
        texto_final.delete(1.0, END)
        texto_final.insert(END, f'\n' + ('*' * 52) + ''
                                f'Fecha: {ahorita.strftime('%b/%d')}'
                                f'\n\t      PARKING MANAGEMENT'
                                f'\n' + ('*' * 52) + ''
                                f'\n\nHa ingresado el carro {placa} a las {ahorita.hour}:{ahorita.minute}'
                                f'\n\n' + ('*' * 52) + '')
        status_estacionamiento.delete(1.0, END)
        status_estacionamiento.insert(END, f'Actualmente hay {len(ESTACIONADOS)} vehiculos.')


def revisar_checks():
    indice = 0
    multiples = 0
    tarifa_selec: str = ''
    tipos_tarifas = ['Hrs', 'Half', 'Full', 'Owner']

    for c in cuadritos_tarifas:
        if cuadritos_tarifas[indice].get() == 1:
            multiples += 1
            tarifa_selec = tipos_tarifas[indice]
        else:
            pass
        indice += 1
    if multiples == 1:
        return tarifa_selec
    else:
        texto_final.delete(1.0, END)
        texto_final.insert(END, 'Debes seleccionar un tipo de tarifa')
        return 'stop'


# Imprime el recibo de salida.
def salida_carro(placa: str):
    global ESTACIONADOS
    ahorita = (datetime.now())

    ESTACIONADOS[placa].insert(1, ahorita.strftime('%m/%d/%y %H:%M:%S'))
    tiempo = ESTACIONADOS.get(placa)
    horas, monto = obtener_tiempo(tiempo)
    pasar_completos(placa, horas, monto)
    texto_final.delete(1.0, END)
    texto_final.insert(END, f'\n' + ('*' * 52) + ''
                            f'Fecha: {ahorita.strftime('%b/%d')}'
                            f'\n\t      PARKING MANAGEMENT'
                            f'\n' + ('*' * 52) + ''
                            f'\n\nHa salido el carro {placa} a las {ahorita.hour}:{ahorita.minute}'
                            f'\nestuvo durante {horas} horas'
                            f'\nel monto total es de: ${monto} USD'
                            f'\n\n' + ('*' * 52) + '')
    status_estacionamiento.delete(1.0, END)
    status_estacionamiento.insert(END, f'Actualmente hay {len(ESTACIONADOS)} vehiculos.')


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


def limpiar():
    texto_final.delete(1.0, END)
    placa_text_box.delete(0, END)
    tarifas.deselect()


# Cuenta la cantidad de carros por tipo de tarifa
def resumen_dia():
    global COMPLETOS
    ahorita = (datetime.now())
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

    texto_final.delete(1.0, END)
    texto_final.insert(END, f'\n' + ('*' * 52) + ''
                            f'Fecha: {ahorita.strftime('%b/%d')}'
                            f'\n\tPARKING MANAGEMENT'
                            f'\n' + ('*' * 52) + ''
                            f'\n\nHoy se han estacionado {carros_hrs + carros_half + carros_full} carros.'
                            f'\n\nde los cuales fueron:'
                            f'\n* {carros_hrs} por horas.' 
                            f'\n* {carros_half} por 1/2 jornada.'
                            f'\n* {carros_full} por jornada completa.'
                            f'\n\n' + ('*' * 52) + ''
                            f'\n\ngenerando un total de ${ingresos} USD')
    status_estacionamiento.delete(1.0, END)
    status_estacionamiento.insert(END, f'Actualmente hay {len(ESTACIONADOS)} vehiculos.')


ESTACIONADOS = {}
COMPLETOS = []


# iniciar tkinter
aplicacion = Tk()


# tamaño de la ventana
aplicacion.geometry('745x440')


# evitar maximizar
aplicacion.resizable(False, False)


# titulo
aplicacion.title('Parking Management')


# icono para la ventana
icono = tkinter.PhotoImage(file='icono.png')
aplicacion.iconphoto(True, icono)


# color de fondo de la ventana
aplicacion.config(bg=Color.PRIMARIO.value)


# panel superior
panel_superior = Frame(aplicacion,
                       bd=1,
                       relief=RAISED)
panel_superior.pack(side=TOP, pady=5)


# etiqueta del titulo
etiqueta_titulo = Label(panel_superior,
                        text='Sistema de Gestion del Estacionamiento',
                        fg=TextColor.DESTACADO.value,
                        font=(Fonts.TITULOS.value, 30),
                        bg=Color.DESTACADO.value,
                        width=31)
etiqueta_titulo.grid(row=0, column=0)


# panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        bg=Color.SECUNDARIO.value,
                        relief=FLAT)
panel_izquierdo.pack(side=LEFT, padx=5, pady=5)


# panel interior con indicaciones
panel_instrucciones = Frame(panel_izquierdo,
                            bd=1,
                            relief=FLAT)
panel_instrucciones.pack(side=TOP)


# indicaciones
indicaciones = Label(panel_instrucciones,
                     text='Ingresa el numero de Placa del carro,'
                          '\nsi  va ingresando  al estacionamiento,'
                          '\nselecciona  uno de los  tipos de tarifa.',
                     fg=TextColor.PRIMARIO.value,
                     font=(Fonts.TEXTO.value, 14),
                     bg=Color.SECUNDARIO.value,
                     width=30)
indicaciones.grid(row=0, column=0)


# panel ingreso de datos
panel_datos = Frame(panel_izquierdo,
                    bd=3,
                    bg=Color.SECUNDARIO.value,
                    relief=FLAT)
panel_datos.pack(side=TOP)


# cajas de texto
var_placa_text = StringVar()

etiqueta_placa = Label(panel_datos,
                       text='PLACA.',
                       fg=TextColor.PRIMARIO.value,
                       font=(Fonts.TEXTO.value, 16),
                       bg=Color.SECUNDARIO.value,
                       width=10)
etiqueta_placa.grid(row=0, column=0)


placa_text_box = Entry(panel_datos,
                       font=(Fonts.BOTONES.value, 16, 'bold'),
                       bd=3,
                       width=15,
                       textvariable=var_placa_text)
placa_text_box.grid(row=0, column=1, padx=2, pady=15)


# generar checks tarifa
tipos_tarifas = ['  Hrs  ', '  Half  ', '  Full  ', 'Owner']
cuadritos_tarifas = []
contador = 0
for tipo in tipos_tarifas:
    cuadritos_tarifas.append('')
    cuadritos_tarifas[contador] = IntVar()
    tarifas = Checkbutton(panel_datos,
                          text=tipo.title(),
                          font=(Fonts.TEXTO.value, 12, 'bold'),
                          bg=Color.SECUNDARIO.value,
                          onvalue=1, offvalue=0,
                          variable=cuadritos_tarifas[contador])
    tarifas.grid(row=contador+1, column=0, pady=5, padx=0)
    contador += 1


# botones inferiores
botones_abajo = ['LIMPIAR', 'RESUMEN', 'GENERAR']
boton_creado = []
filas = 0
for boton in botones_abajo:
    boton = Button(panel_izquierdo,
                   text=boton.title(),
                   font=(Fonts.BOTONES.value, 14, 'bold'),
                   fg=TextColor.PRIMARIO.value,
                   bg=Color.BOTONES.value,
                   bd=4,
                   width=9)
    boton.pack(side=RIGHT, padx=5, pady=10)
    boton_creado.append(boton)
    filas += 1


# acciones de los botones
boton_creado[0].config(command=limpiar)
boton_creado[1].config(command=resumen_dia)
boton_creado[2].config(command=buscar_placa)


# panel derecho
panel_derecho = Frame(aplicacion,
                      bd=1,
                      bg=Color.PRIMARIO.value,
                      relief=FLAT)
panel_derecho.pack(side=RIGHT)


# areas de texto
status_estacionamiento = Text(panel_derecho,
                              font=(Fonts.TEXTBOX.value, 12, 'bold'),
                              bd=3,
                              width=35,
                              height=1)
status_estacionamiento.grid(row=0, column=0, padx=5, pady=5)


texto_final = Text(panel_derecho,
                   font=(Fonts.TEXTBOX.value, 12, 'bold'),
                   bd=3,
                   width=35,
                   height=17)
texto_final.grid(row=1, column=0, padx=5, pady=5)


# evitar que la pantalla se cierre
aplicacion.mainloop()
