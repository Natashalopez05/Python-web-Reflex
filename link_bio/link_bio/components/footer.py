import reflex as rx # type: ignore
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.styles import TextColor as TextColor
from link_bio.styles.styles import Color as Color
import link_bio.constants as constants

def footer() -> rx.Component:
    return rx.vstack(
        rx.chakra.hstack(

            rx.chakra.avatar(name = "Natasha López",
                size = "sm",
                color = TextColor.HEADER.value,
                background_color = TextColor.FOOTER.value,
                padding = "2px",
                border = "4px",
                border_color = Color.TERTIARY.value)
        ),
        rx.link(
            
                f"© {datetime.date.today().year} Natasha López",
                color = TextColor.HEADER.value,
            href = constants.GITHUB_URL,
            is_external = True,
            font_size = Size.SMALL.value
        ),
        rx.text(
            "Hecho con amor y Reflex / Logo sacado de Design.com",
            font_size = Size.SMALL.value,
            color = TextColor.HEADER.value,
            margin_top = Size.ZERO.value
        ),
        margin_bottom = Size.SMALL.value,
        padding_bottom = Size.SMALL.value,
        padding_x = Size.SMALL.value,
        justify_content = "center",
        width = "100%",
        padding = Size.SMALL.value,
        style = {"align_items": "center"}
       
    )