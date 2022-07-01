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
from app import pre_def_cards, user_selected_cards

# Here Will all the Cards be Displayed ###########################################################

dashboard_layout = html.Div(
    children=[
        dcc.Link("Home > Dashbaords", href="/",style={"text-decoration":"none", "color":"#375A7F"}),
    ],
),

seite = list()

def GetCards():
    count = 1
    toggle = "cards.card_" + str(count)
    toggle_val = False
    toggle_label = "Karte ist nicht ausgewählt"
    for y in user_selected_cards:
        if(y in user_selected_cards):
            toggle_label = "Karte ist ausgewählt"
            toggle_val = True
        else:
            toggle_label = "Karte nicht ausgewählt"
            toggle_val=False
    for x in pre_def_cards: 
        print(len(pre_def_cards)),
        content = html.Div(
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
                        label=toggle_label,
                        labelPosition='bottom',
                        value=toggle_val,
                        ),
                    ],
                    className="card_select",
                ),
                html.Br(),
                html.Br(),
                html.Hr(), 
            ],
        )
        seite.append(content)
    count+=1
    print("Current card num:", count)
    seite_anzeigen()

def seite_anzeigen():
    for s in seite:
        html.Div(
            children=[
                s
            ],
        )