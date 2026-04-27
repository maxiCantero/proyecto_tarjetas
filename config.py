# config.py

# Conversión mm → px a 300 DPI
MM_TO_PX = 11.811

# Tamaño físico deseado (ANCHO x ALTO)
CARD_WIDTH_MM = 54     # ancho real
CARD_HEIGHT_MM = 86    # alto real

CARD_WIDTH = int(CARD_WIDTH_MM * MM_TO_PX)     # ≈ 638 px
CARD_HEIGHT = int(CARD_HEIGHT_MM * MM_TO_PX)   # ≈ 1016 px

# Posición y tamaño de la foto
PHOTO_X = 40
PHOTO_Y = 200
PHOTO_WIDTH = 260
PHOTO_HEIGHT = 340

# Texto
TEXT_COLOR = "black"
FONT_PATH = "assets/fonts/arial.ttf"
FONT_SIZE_NAME = 40
FONT_SIZE_OTHER = 32

NAME_X = 40
NAME_Y = 580

LEGAJO_X = 40
LEGAJO_Y = 650

DNI_X = 40
DNI_Y = 720

# Carpeta de salida
OUTPUT_DIR = "output"
