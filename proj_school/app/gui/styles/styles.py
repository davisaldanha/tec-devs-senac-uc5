'''
Estilos e configurações globais da aplicação
'''

from .colors import *
from .fonts import *

# Configurações de tema 
CTK_APPEARANCE = 'dark'
CTK_COLOR_THEME = 'blue'

# Padding e margins padrão
PADDING_XS = 5
PADDING_SM = 10
PADDING_MD = 15
PADDING_LG = 20
PADDING_XL = 30

#Tamanhos de componentes
BUTTON_HEIGHT = 40
ENTRY_HEIGHT = 35
LABEL_HEIGHT = 30
FRAME_CORNER_RADIUS = 10
BUTTON_CORNER_RADIUS = 8
ENTRY_CORNER_RADIUS = 8

# Estilos de dicionários para componentes
BUTTON_STYLE = {
    'fg_color': BUTTON_BG,
    'text_color': BUTTON_FG,
    'hover_color': BUTTON_HOVER,
    'corner_radius': BUTTON_CORNER_RADIUS,
    'font': FONT_BUTTON,
    'height': BUTTON_HEIGHT
}

BUTTON_DANGER_STYLE = {
    'fg_color': BUTTON_DANGER_BG,
    'text_color': BUTTON_FG,
    'hover_color': BUTTON_DANGER_HOVER,
    'corner_radius': BUTTON_CORNER_RADIUS,
    'font': FONT_BUTTON,
    'height': BUTTON_HEIGHT
}

ENTRY_STYLE = {
    'fg_color': ENTRY_BG,
    'text_color': ENTRY_FG,
    'border_color': ENTRY_BORDER,
    'corner_radius': ENTRY_CORNER_RADIUS,
    'font': FONT_ENTRY,
    'height': ENTRY_HEIGHT
}

FRAME_STYLE = {
    'fg_color': FRAME_BG,
    'corner_radius': FRAME_CORNER_RADIUS
}

LABEL_STYLE = {
    'text_color': LABEL_FG,
    'font': FONT_LABEL
}

MIN_WINDOW_WIDTH = 1200
MIN_WINDOW_HEIGHT = 700
SIDEBAR_WIDTH = 200
CONTENT_PADDING = 20