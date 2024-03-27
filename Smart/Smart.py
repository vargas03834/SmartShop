"""Welcome to Reflex!."""

#from Smart import styles

# Import all the pages.
from Smart.pages import *
from Smart.templates import template

import reflex as rx

@template(route="/begin", title="Menu", image="/github.svg")
def inicio() -> rx.Component:
    return rx.vstack(
        rx.heading("Lo mejor en ", 
                   style = {"position": "fixed", 
                            "top": "50%", 
                            "transform": "translateY(-300%)", 
                            "left": "250px", "fontSize": "2em", 
                            "marginBottom": "20px", 
                            "align": "start"}
        ),rx.vstack(
            rx.heading("Smartphone's", 
                   style ={"position": "fixed",
                           "top": "50%", "transform": "translateY(-100%)", 
                           "left": "250px", "fontSize": "4em", 
                           "marginBottom": "20px", 
                           "align": "start"}),
                rx.link("Explora Ahora", href="http://localhost:3000/settings/", 
                        style={"fontSize": "1.4em",
                            "position": "fixed", 
                            "bottom": "42%", 
                            "transform": "translateY(0%)", 
                            "left": "400px", 
                            "width": "150px", 
                            "height": "40px", 
                            "margin-top": "100px", 
                            "color": "white", 
                            "background-color": "black", 
                            "border": "none", 
                            "border-radius": "20px", 
                            "cursor": "pointer"}),  
        rx.hstack(
            rx.chakra.button_group(
                rx.button("Inicio", font_size="0.7em", color = "black",bg="#B8BBBE"),
                rx.button("Productos",font_size="0.7em", color = "black",bg="#B8BBBE"),
                rx.button("Sobre Nosotros",font_size="0.7em", color = "black",bg="#B8BBBE"),
                rx.button("Soporte",font_size="0.7em", color = "black",bg="#B8BBBE"),
                variant="link",
                spacing=8,
            ), 
            style={"position": "fixed", "top": "11%", 
                   "left": "400px", "transform": "translateY(-50%)", 
                   "widht": "100%", "fontSize": "2em"},
        ),rx.box(
            style={"position": "fixed", 
                   "top": "0", "right": "0", 
                   "width": "600px", 
                   "height": "100%", 
                   "background-color": "#B8BBBE"},
        ),rx.hstack(
            rx.input(placeholder="Buscar", 
                    height="30px", 
                    width="15%", 
                    bg="white",
                    style = {"position": "fixed",
                        "top":"9%", 
                        "right":"200px"}),
        ),rx.hstack(
            rx.chakra.icon(tag="search", 
                    style={"position": "fixed", 
                        "top": "10.5%", 
                        "right": "175px", 
                        "transform": "translateY(-40%)",
                        "widht": "100%"}),
        ),rx.hstack(
            rx.image(
                src="/celular.png",
                style={
                    "position": "fixed",
                    "top": "50%",
                    "transform": "translateY(-50%)",
                    "right": "350px",
                    "width": "auto",
                    "height": "auto"}))
            )
    )

app = rx.App()
app.add_page(inicio)
app.compile()
# Create the app.
#app = rx.App#(style=styles.base_style)
