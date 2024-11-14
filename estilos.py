from enum import Enum


class Color(Enum):
    DESTACADO = '#778899'
    PRIMARIO = '#BC8F8F'
    SECUNDARIO = '#888888'
    BOTONES = '#B0C4DE'


class TextColor(Enum):
    DESTACADO = 'white'
    PRIMARIO = 'black'
    SECUNDARIO = 'dimgray'


class Fonts(Enum):
    TITULOS = "assets/Gugi-Regular.ttf"
    TEXTO = "assets/SourGummy-Regular.ttf"
    TEXTBOX = "assets/Tinos-Regular.ttf"
    BOTONES = ''
