import reflex as rx # type: ignore
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.constants as constants

def links() -> rx.Component:
    return rx.vstack(
        title("Links de interés"),
        link_button("GitHub","Mis proyectos","icons/github.svg",constants.GITHUB_URL),
        link_button("Youtube de MoureDev","Donde aprendi hacer esta web","icons/youtube.svg", constants.YOUTUBE_MOURE),
        link_button("Reflex","Documentación de Reflex","icons/python.svg", constants.REFLEX_URL),
        link_button("Chakra UI","Documentación de Chakra UI","icons/python.svg", constants.CHAKRA_URL),

        title("Contacto"),
    
        link_button(
            "Email",
            constants.EMAIL,
            "icons/google.svg",
            f"mailto:{constants.EMAIL}"
        ),
        width = "100%",
        
        spacing = '3'

        

        
    )