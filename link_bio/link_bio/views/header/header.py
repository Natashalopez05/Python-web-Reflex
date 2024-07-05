import reflex as rx # type: ignore
from link_bio.components.link_icon import links_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.constants as constants
from link_bio.styles.fonts import Font, FontWeight

def header() -> rx.Component:
    return rx.vstack(
        
        rx.chakra.hstack(

            rx.chakra.avatar(
                name = "Natasha López",
                size = "xl",
                src = "logo.png",
                color = TextColor.BODY.value,
                background_color = TextColor.FOOTER.value,
                padding = "2px",
                border = "4px",
                border_color = Color.TERTIARY.value
            ),
            
            
            rx.vstack(
                rx.heading("Natasha López ",
                        size = '6',
                        font_family = Font.LOGO.value,
                        font_weight = "FontWeight.MEDIUM.value"
                ),

                rx.text(
                    "@Natashalop05",
                    margin_top = Size.ZERO.value,
                    font_family = Font.LOGO.value,
                ),
                rx.hstack(
                links_icon("icons/github.svg", constants.GITHUB_URL, "GitHub"),
                links_icon("icons/python.svg",constants.REFLEX_URL, "Python"),
                links_icon("icons/python.svg", constants.CHAKRA_URL, "Python"),
                style = {"align_items": "center"}
                ),
                
                width = "100%",
                align_items = "flex-start"
            
            )


        ),
         rx.text("""Soy estudiante de la carrera de Ingeniería en Ciencias y Computación. 
                 Me gusta la programación y el diseño web. 
                 Puedes ver mis proyectos en mi página de GitHub."""),
                 
                 color = TextColor.HEADER.value,
                 spacing =  '7',
                 font_family = Font.LOGO.value,
                 padding_x = Size.SMALL.value,
                 style = {"align_items": "center"}
         
      
    )
