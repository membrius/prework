
import reflex as rx 

import asyncio 




PROFILE_INFO = [
    "Hello👋, A dynamic professional at the intersection of software development, data engineering, and cloud Technology, I bring a unique blend of skills and experience that drives digital transformation and fosters innovation. With a solid foundation in software development shaped through both academic studies and real world projects, i transitioned seamlessly into data engineering and AWS Cloud roles, where i have excelled in building scalable, resilient data solutions.🚀",
    "Data Engineering & Cloud Expertise: With hands on experience creating data pipelines on both Google Cloud and AWS, i am adept at constructing and optimizing cloud infrastructure that meets meets the varied modern enterprises, from designing robust data architectures to implementing DevOps and automation practices, i leverage a range of AWS and Google Cloud tools to drive efficiency, scalability, and reliability in data-driven applications  demand  data analysis, and software development.🌍", 
    "Passion for Innovation: My Journey in software development has fostered a passion innovation. I'm continuously exploring emerging technologies and industry trends to identify new optimization and enhancement opportunities, especially within data engineering including a prominent tech firm that has became very big.💻",


]

UI_TEXT = [
    "Skills:",
    "Contact",
    "Download CV"
]

SKILLS = ["Python", "Java", "C++","SQL", "NoSQL","AWS","Google Cloud","Solutions Architecture","Data Analysis & Visualization","Collaboration & Communication","Pipeline Monitoring & Maintenance", "Problem-Solving & Analytical Thinking"] 



class State(rx.State):
    skills = SKILLS.copy()
    profile_info = PROFILE_INFO.copy()
    ui_text = UI_TEXT.copy()


def market():
    return rx.center(
        rx.avatar(
            src="nosipho.webp",  
            radius="medium",
            size="9",
            gap="10px",
            width="55%",
            line_height="2rem",
        ),
        rx.heading("Nosipho Mncwango", margin_top="0.4rem", color="white"),
        rx.el.a("Data Engineer 👩‍💻"), 
        direction="column"
    )

def display_skills(skills: str):
    return rx.badge(skills, size="2", variant="outline", color="white", border_radius="5px")

def skills_cards():
    return rx.center(
        rx.text(State.ui_text[0], size="1"), 
        rx.flex(
            rx.foreach(State.skills, display_skills),
             width="80%",
            spacing="2",
            flex_wrap="wrap",
            align="center",
            justify="center",
            padding_top="0.2em",
        ),
         width="100%",
        direction="column",
        padding_top=rx.breakpoints(
            initial="1.4em",
            sm="2.2em"
    ),

    )





def display_profile_info(info: str):
    return rx.box(rx.markdown(info), color="white")





def profile_description():
    return rx.vstack(
        rx.foreach(State.profile_info, display_profile_info)
    )





def contact_button():
    return rx.link(
        rx.button(
            rx.icon(tag="mail", color="white"),
            State.ui_text[1],
            size=rx.breakpoints(
                initial="2",
                xs="3",
            ),
            variant="outline",
            cursor="pointer",
            color="white",
        
        
        ),
        href="mailto:fefc3898@gmail.com",
    )


def download_cv():
    return rx.button(
        rx.icon(tag="file-down"),
        State.ui_text[2], 
        on_click=rx.download(url='/CV.zip'), 
        size=rx.breakpoints(
                initial="2",
                xs="3"
         ),
        cursor="pointer",
   
    )



def social_icon(icon, link):
    return rx.link(
        rx.icon(icon, color="white", _hover={"color": "red"}),
        href=link,
        is_external=True,
        

    )



def socials_links():
    return rx.hstack(
        social_icon("facebook", "https://www.facebook.com/nosipho.mncwango.522?mibextid=ZbWKwL"),
        social_icon("linkedin", "https://www.linkedin.com/in/nosipho-mncwango-644615245/"),
        social_icon("instagram", "https://www.instagram.com/n_mncwa/"),
        spacing="2",
        padding=rx.breakpoints(
            initial="0.8em 0 0 0",
            xs="0.8em 0 0 0",
            sm="0 0.2em 0 0"
    
        ),
    )