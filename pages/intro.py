import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction 😃")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Welcome to Centralized Integrated Vendor Database"),
        html.Br(),html.Br(),
        "Click the buttons to get some insights!"      
    ]),
    

], className="bg-light p-4 m-2")
