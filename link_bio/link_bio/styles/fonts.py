import reflex as rx # type: ignore
from enum import Enum

class Font(Enum):
    LOGO = "Comfortaa"
    DEFAULT = "Poppins"
    TITLE = "Poppins"

class FontWeight(Enum):
    LIGHT = "300",
    MEDIUM = "500"