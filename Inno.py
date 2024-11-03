"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from Inno.market import * 

class State(rx.State):
    """The app state."""







def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.flex(
            rx.vstack(
                rx.center(
                    market(), 
                    width="100%"
                ),
                skills_cards(),
                bg="rgb(56,68,77)",
                box_shadow="0 20px 30px -10px",
                background_image="linear-gradient(144deg,#8000ff,60%,#0A0136)",
                min_width="20em",
                height="auto",
                padding="0.8em",
                border_radius=rx.breakpoints(
                initial="1.5rem 1.5rem 0 0",
                sm="1.5rem 0 0 1.5rem"
                ),
                justify="center"
            ),
            rx.vstack(
                profile_description(),

                rx.flex(
                    rx.hstack(
                        contact_button(),
                        rx.spacer(),
                        rx.spacer(),
                        download_cv(),
                        
                    
                    ),
                    socials_links(),
                    width="100%",
                    align=rx.breakpoints(
                        initial="center",
                        xs="end"
                    ),
                    justify=rx.breakpoints(
                        initial="center",
                        xs="between"
                    ),
                    direction=rx.breakpoints(
                        initial="column",
                        xs="row"
                    ),
                ),
               padding="0.8rem"
                 
            ),
             bg="rgb(29,42,53)",
            box_shadow="0 20px 30px -10px",
            border_radius="1.5rem",
        ),
        
    )
    

 


def index2() -> rx.Component:
    return rx.mobile_only(
        rx.container(
        rx.flex(
            rx.vstack(
                rx.center(
                    market(), 
                    width="100%"
                ),
              
                skills_cards(),
                bg="rgb(56,68,77)",
                box_shadow="0 20px 30px -10px",
                background_image="linear-gradient(144deg,#8000ff,60%,#0A0136)",
                min_width="20em",
                height="auto",
                padding="0.8em",
                border_radius=rx.breakpoints(
                initial="1.5rem 1.5rem 0 0",
                sm="1.5rem 0 0 1.5rem"
                ),
                justify="center"
            ),
            rx.vstack(
                profile_description(),

                rx.flex(
                    rx.hstack(
                        contact_button(),
                        rx.spacer(),
                        rx.spacer(),
                        download_cv(),
                        
                    
                    ),
                    socials_links(),
                    width="100%",
                    align=rx.breakpoints(
                        initial="center",
                        xs="end"
                    ),
                    justify=rx.breakpoints(
                        initial="center",
                        xs="between"
                    ),
                    direction=rx.breakpoints(
                        initial="column",
                        xs="row"
                    ),
                ),
               padding="0.8rem"
                 
            ),
             bg="rgb(29,42,53)",
            box_shadow="0 20px 30px -10px",
        )
        )
        )
    


app = rx.App(
    style = {
        "background":"#232d4d",
        "color":"#fff",
    }
)
app.add_page(index)
app._compile()


           
        
    


