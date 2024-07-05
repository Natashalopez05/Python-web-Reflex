from enum import Enum
import reflex as rx # type: ignore
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font, FontWeight

# Constants
MAX_WIDTH = "550px"

# Sizes
STYLESHEET = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.8em"
    MEDIUM = "1em"
    LARGE = "2em"
    XLARGE = "40px"
    XXLARGE = "50px"
    XXXLARGE = "60px"

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,  
    "font_weight": FontWeight.LIGHT.value, 
    "background_color": Color.BACKGROUND.value,
    rx.heading:{
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button:{
        "width":"100%",
        "height":"100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.MEDIUM.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.BUTTON.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover":{
            "background_color": Color.PRIMARY.value,
           
        }
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    }
}

title_style = dict(
    width = "100%",
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    padding_top = Size.SMALL.value,
    color = TextColor.HEADER.value,
    style = {"text_align": "center"}
)

button_title_style = dict(
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.MEDIUM.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_family = Font.DEFAULT.value,
    font_weight = FontWeight.LIGHT.value,
    font_size = Size.SMALL.value,
    color = TextColor.BODYTITLE.value
)