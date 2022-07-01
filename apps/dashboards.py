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
    count = 1
    toggle = "card_" + str(count)
    for x in pre_def_cards: 
        return html.Div(
            children=[
                dcc.Link("Home > Dashbaords", href="/",style={"text-decoration":"none", "color":"#375A7F"}),
                html.Hr(),
                html.Div(
                    children=[
                        html.H1("Karte")
                    ],
                    style={"padding-right":"10px"},
                    className="DisplayFlex",
                ),
                html.Div(
                    children=[
                        html.H1(str(count)),
                    ],
                    className="DisplayFlex",
                ),
                html.P(x),
                html.Div(
                    children=[
                        daq.ToggleSwitch(
                        id=toggle,
                        label='Karte ist nicht ausgewählt',
                        labelPosition='bottom'
                        ),
                    ],
                    className="card_select",
                ),
                html.Br(),
                html.Br(),
                html.Hr(), 
            ],
        )
    count+=1
    print("Current card num:", count),