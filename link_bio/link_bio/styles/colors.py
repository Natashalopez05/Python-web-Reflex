import reflex as rx # type: ignore
from enum import Enum

class Color(Enum):
    PRIMARY = "    #e6b0aa   " #ROSA OSCURO
    SECONDARY = "#e5e7e9" #BLANCO 
    TERTIARY = " #f5b7b1 " #ROSA
    BACKGROUND = "  #000000 " #NEGRO
    NAVBAR = " #201F1F " #GRIS OSCURO
    CONTENT = "  #717d7e " #GRIS
    BUTTON = "#323131" #GRIS OSCURO-OSCURO


class TextColor(Enum):
    HEADER = "#fbeee6" #BLANCO
    BODYTITLE = "#ffffff" #BLANCO SUPER
    BODY = " #2c3e50 " #GRIS OSCURO
    FOOTER = "#1b2631" #NEGRO