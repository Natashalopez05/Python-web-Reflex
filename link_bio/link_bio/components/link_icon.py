import reflex as rx # type: ignore
from link_bio.components.link_button import link_button
from link_bio.styles.styles import Size as Size



def links_icon(image: str, url: str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,
            weight = Size.MEDIUM.value,
            alt = alt
        ),
        href = url,
        is_external = True
    )