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

# Here all the Settings will be Displayed ###########################################################
