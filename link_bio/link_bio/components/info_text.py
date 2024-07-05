import reflex as rx # type: ignore
from link_bio.styles.styles import Size as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.chakra.span(title, font_weight="bold", color="blue"),
        body, font_size=Size.LARGE.value
        )
        
