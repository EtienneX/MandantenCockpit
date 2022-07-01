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
from Templates import cards


#Pre-defined Layout #################################################################################################
#Will be displayed if the user doesnt have ans Configuration

layout_pre = html.Div(
    children=[
        #Row 1
        html.Div(
            	children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_2,
                ],
                className="DisplayFlex",
            ),
            html.Br(),
            #Row 2
        html.Div(
                children=[
                    cards.card_2,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
            html.Br(),
            #Row 3
                html.Div(
                children=[
                    cards.card_4,
                ],
                className="DisplayFlex",
            ),
            html.Div(
                children=[
                    cards.card_5,
                ],
                className="DisplayFlex",
            ),
            html.Div(
                children=[
                    cards.card_5,
                ],
                className="DisplayFlex",
            ),
            html.Br(),
            #Row 4
            html.Div(
                children=[
                    cards.card_9,
                ],
                className="DisplayFlex",
            ),
            html.Div(
                children=[
                    cards.card_10,
                ],
                className="DisplayFlex",
            ),
                        html.Div(
                children=[
                    cards.card_11,
                ],
                className="DisplayFlex",
            ),
            html.Br(),
            #Row 5
            html.Div(
                children=[
                    cards.card_9,
                ],
                className="DisplayFlex",
            ),
            html.Div(
                children=[
                    cards.card_12,
                ],
                className="DisplayFlex",
            ),
                        html.Div(
                children=[
                    cards.card_11,
                ],
                className="DisplayFlex",
            ),
            html.Div(
                children=[
                    cards.card_11,
                ],
                className="DisplayFlex",
            ),
    ],
)
#########################################################################################################

#User-defined Layout #################################################################################################
#Will be displayed if the user selected dashboards
user_def = html.Div(
    children=[

    ]
)
#########################################################################################################

card_display = html.Div(
    children=[
        html.Div(
            	children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_2,
                ],
                className="DisplayFlex",
            ),
            html.Br(),
        html.Div(
                children=[
                    cards.card_2,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Br(),
                        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_1,
                ],
                className="DisplayFlex",
            ),
        html.Div(
                children=[
                    cards.card_2,
                ],
                className="DisplayFlex",
            ),
            html.Br(),
                html.Div(
                children=[
                    cards.card_3,
                ],
                className="DisplayFlex",
            ),
                html.Div(
                children=[
                    cards.card_3,
                ],
                className="DisplayFlex",
            ),
                html.Div(
                children=[
                    cards.card_3,
                ],
                className="DisplayFlex",
            ),
                html.Div(
                children=[
                    cards.card_4,
                ],
                className="DisplayFlex",
            ),
                html.Div(
                children=[
                    cards.card_5,
                ],
                className="DisplayFlex",
            ),
    ],
)
#########################################################################################################