from ast import In
from asyncio.windows_events import NULL
from lib2to3.pytree import convert
from dash import Dash, html, dcc, Input, Output, dash
import dash_daq as daq
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO, template_from_url
from Templates import content, sidenav
from apps import dashboards
from app import app


template_theme1 = "minty"
template_theme2 = "darkly"
url1_theme1 = dbc.themes.MINTY
url1_theme2 = dbc.themes.DARKLY



SIDEBAR_STYLE_LIGHT={
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "color":"#008eac",
    "height":"100%",
}
SIDEBAR_STYLE_DARK={
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#375a7f",
    "color":"white",
}


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("LohnDialog GmbH", className="navtitle"),
        html.Hr(),
        html.P("Mandanten Cockpit", className="navdescription"),
        html.Hr(),
        dcc.Link("Home",href="/", className="navlink"),
        dcc.Link("Dashboards",href="/apps/dashboards",className="navlink"),
        dcc.Link("Einstellungen",href="/apps/settings",className="navlink"),
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content",children=[]),
        html.Br(),
        html.Hr(),
        html.P("Thema", className="navdescription"),
        html.Div(
            children=[
            dbc.Row(
                dbc.Col(
                    [
                    dbc.Button(
                        ThemeSwitchAIO(aio_id="theme",themes=[url1_theme1,url1_theme2]),
                    id="ThemeChangerBtn", n_clicks=0, value=False),
                    ], 
                ),
            className="LightDarkToggle"),
            ],
        ),
        html.Div(id="colout"),
        html.Hr(),
        html.A(className="fas fa-cog",id="open-centered-settings",style={"padding-right":"10px"}),
    ],
    style=SIDEBAR_STYLE_LIGHT
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

@app.callback(
    Output(component_id="page-content", component_property="children"),
    Input(component_id="url", component_property="pathname")
)

def render_page_content(pathname):
    if pathname == "/":
        return content.layout1,
    elif pathname == "/apps/dashboards":
        return html.P("This is the content of Dashboards. Yay!")
    elif pathname == "/apps/settings":
        return html.P("Oh cool, this is Settings!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
    


