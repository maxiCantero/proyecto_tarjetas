# card_builder.py

import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from config import (
    CARD_WIDTH, CARD_HEIGHT,
    PHOTO_X, PHOTO_Y, PHOTO_WIDTH, PHOTO_HEIGHT,
    TEXT_COLOR,
    FONT_PATH, FONT_SIZE_NAME, FONT_SIZE_OTHER,
    NAME_X, NAME_Y,
    LEGAJO_X, LEGAJO_Y,
    DNI_X, DNI_Y,
    OUTPUT_DIR
)

def asegurar_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generar_nombre_archivo_pdf(nombre, legajo):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = nombre if nombre else "tarjeta"
    safe = "".join(c for c in base if c.isalnum() or c in " _-").strip()
    return os.path.join(OUTPUT_DIR, f"{safe}_{timestamp}.pdf")

def _crear_tarjeta_base(plantilla_path, foto_path, nombre, legajo, dni):
    # Plantilla o fondo blanco
    if plantilla_path and os.path.exists(plantilla_path):
        tarjeta = Image.open(plantilla_path).convert("RGBA")
        tarjeta = tarjeta.resize((CARD_WIDTH, CARD_HEIGHT))
    else:
        tarjeta = Image.new("RGBA", (CARD_WIDTH, CARD_HEIGHT), "white")

    draw = ImageDraw.Draw(tarjeta)

    # Foto opcional
    if foto_path and os.path.exists(foto_path):
        foto = Image.open(foto_path).convert("RGBA")
        foto = foto.resize((PHOTO_WIDTH, PHOTO_HEIGHT))
        tarjeta.paste(foto, (PHOTO_X, PHOTO_Y))

    # Fuentes
    font_name = ImageFont.truetype(FONT_PATH, FONT_SIZE_NAME)
    font_other = ImageFont.truetype(FONT_PATH, FONT_SIZE_OTHER)

    # Texto con formato solicitado
    if nombre:
        draw.text((NAME_X, NAME_Y), f"NOMBRE: {nombre}", fill=TEXT_COLOR, font=font_name)

    if legajo:
        draw.text((LEGAJO_X, LEGAJO_Y), f"LEGAJO: {legajo}", fill=TEXT_COLOR, font=font_other)

    if dni:
        draw.text((DNI_X, DNI_Y), f"DNI: {dni}", fill=TEXT_COLOR, font=font_other)

    return tarjeta

def generar_tarjeta(plantilla_path, foto_path, nombre, legajo, dni):
    asegurar_output_dir()
    tarjeta = _crear_tarjeta_base(plantilla_path, foto_path, nombre, legajo, dni)
    salida_pdf = generar_nombre_archivo_pdf(nombre, legajo)
    tarjeta.save(salida_pdf, "PDF", resolution=300.0)
    return salida_pdf

def generar_imagen_previa(plantilla_path, foto_path, nombre, legajo, dni):
    tarjeta = _crear_tarjeta_base(plantilla_path, foto_path, nombre, legajo, dni)
    return tarjeta
