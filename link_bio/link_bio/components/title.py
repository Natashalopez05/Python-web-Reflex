import reflex as rx # type: ignore
import link_bio.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size = '6',
        style = styles.title_style,
        align = 'center'
    )