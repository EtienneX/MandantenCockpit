from asyncio.windows_events import NULL
from xml.sax.xmlreader import InputSource
from dash import Dash, html, dcc, Input, Output, dash, State
import dash_bootstrap_components as dbc 
import flask
import plotly.express as px
import pandas as pd
from Templates import sidenav
import dash_daq as daq
from dash_bootstrap_templates import ThemeSwitchAIO, template_from_url
from Templates import cards, content
import sql_queries
from app import pre_def_cards

# Here Will all the Cards be Displayed ###########################################################

dashboard_layout = html.Div(
    children=[
        dcc.Link("Home > Dashbaords", href="/",style={"text-decoration":"none", "color":"#375A7F"}),
    ],
),

def GetCards():
    for x in pre_def_cards: 
        return html.Div(
            children=[
                dcc.Link("Home > Dashbaords", href="/",style={"text-decoration":"none", "color":"#375A7F"}),
                html.Hr(),
                html.H1("Karte 1"),
                html.P(cards.card_1),
                html.Hr(), 
                html.H1("Karte 2"),
                html.P(cards.card_2),
                html.Hr(), 
                html.H1("Karte 3"),
                html.P(cards.card_3),
                html.Br(),
                html.Hr(), 
                html.H1("Karte 4"),
                html.P(cards.card_4),
                html.Hr(), 
                html.H1("Karte 5"),
                html.P(cards.card_5),
                html.Br(),
                html.Hr(), 
                html.H1("Karte 6"),
                html.P(cards.card_6),
                html.Hr(), 
                html.H1("Karte 7"),
                html.P(cards.card_7),
                html.Hr(), 
                html.H1("Karte 8"),
                html.P(cards.card_8),
                html.Hr(), 
                html.H1("Karte 9"),
                html.P(cards.card_9),
                html.Hr(), 
                html.H1("Karte 10"),
                html.P(cards.card_10),
                html.Hr(), 
                html.H1("Karte 11"),
                html.P(cards.card_11),
                html.Hr(), 
                html.H1("Karte 12"),
                html.P(cards.card_12),
                html.Hr(), 
                html.H1("Karte 13"),
                html.P(cards.card_13),
                html.Hr(), 
                html.H1("Karte 14"),
                html.P(cards.card_14),
                html.Hr(), 
                html.H1("Karte 15"),
                html.P(cards.card_15),
                html.Hr(), 
                html.H1("Karte 16"),
                html.P(cards.card_16),
                html.Hr(), 
                html.H1("Karte 17"),
                html.P(cards.card_17),
                html.Hr(), 
                html.H1("Karte 18"),
                html.P(cards.card_18),
                html.Hr(), 
                html.H1("Karte 19"),
                html.P(cards.card_19),
                html.Hr(), 
                html.H1("Karte 20"),
                html.P(cards.card_20),
            ],
        )