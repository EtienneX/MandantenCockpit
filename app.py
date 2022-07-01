# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

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
from apps import dashboards, settings

#Font Awesome Icons#############################################################################
font_awesome = ['/assets/fontAwesome/font-awesome.min.css']
################################################################################################

#Bootstrap####################################################################################################
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.MINTY,dbc.themes.DARKLY, font_awesome])
##############################################################################################################



app = Dash(__name__,suppress_callback_exceptions = True,meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=2.0, maximum-scale=1.2, minimum-scale=0.5,'}])

# Pre-Defined cards list
pre_def_cards = [cards.card_1,cards.card_2,cards.card_3,cards.card_4,cards.card_5]
#############################

# User Configured layout list
user_conf_layout = list()
#############################

# Themes #############################
url1_theme1 = dbc.themes.MINTY
url1_theme2 = dbc.themes.DARKLY
######################################

sidebar = html.Div(
    [
        html.H2("LohnDialog GmbH", className="navtitle"),
        html.Hr(),
        html.P("Mandanten Cockpit", className="navdescription"),
        html.Hr(),
        dcc.Link("Home",href="/", className="navlink", style={"text-decoration":"none", "text-align":"left"}),
        dcc.Link("Dashboards",href="/apps/dashboards",className="navlink",style={"text-decoration":"none", "text-align":"left"}),
        dcc.Link("Einstellungen",href="/apps/settings",className="navlink",style={"text-decoration":"none", "text-align":"left"}),
        dcc.Location(id="url", refresh=False),
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
        dcc.Link("",className="fas fa-cog",href="/apps/dashboards",style={"padding-right":"10px", "font-size":"25px !important"}),
    ],
    className="SIDEBAR_STYLE_LIGHT",
)

app.layout = html.Div(children=[
#Website Content--------------------
    sidebar,
    html.Div(id="page-content",children=[], className="content-holder"),
    #sql_queries.ConnectionTest_sql()
#-----------------------------------
])

@app.callback(
    Output(component_id="page-content", component_property="children"),
    Input(component_id="url", component_property="pathname")
)


def render_page_content(pathname):
    if pathname == "/":
        #dashboards.GetCards(),
        return content.layout_pre,
    elif pathname == "/apps/dashboards":
        return dashboards.GetCards(),
    elif pathname == "/apps/settings":
        return "Nothing to show yet!",
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True,)


