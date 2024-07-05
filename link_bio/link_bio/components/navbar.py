import reflex as rx # type: ignore
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import Font, FontWeight


def navbar() -> rx.Component:
    return rx.hstack(
       rx.text(
           "Natasha's Web",
              font_size = Size.MEDIUM.value,
                font_weight = FontWeight.MEDIUM.value,
                font_family = Font.LOGO.value,
    
                color = TextColor.HEADER.value
        

       ),
       position = "sticky",
       background_color = Color.NAVBAR.value,
       padding_x = Size.MEDIUM.value,
       padding_y = Size.MEDIUM.value,
       z_index = "999",
       top = "0"
   )