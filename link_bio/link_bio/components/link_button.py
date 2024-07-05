import reflex as rx # type: ignore
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size

def link_button(title: str, body:str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,
                    width = styles.Size.LARGE.value,
                    height = styles.Size.LARGE.value,
                    margin = styles.Size.MEDIUM.value,
                    alt = title
                ),
                rx.vstack(
                    rx.text(title, style =styles.button_title_style),
                    rx.text(body, style = styles.button_body_style),
                    spacing = '3',
                    align_items = "flex-start",
                    margin = Size.ZERO.value

                ),
                width = "100%",
                align_items = "start"
                
            )
        ),
        href = url,
        is_external = True,
        width = "100%"
    )


    