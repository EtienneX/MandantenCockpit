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
import sql_queries

#The Different cards will be declared here

#Card 1 #################################################################################################
card_1 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3(sql_queries.select_Firbezeichnung_sql()),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-body",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3("Settings"),
                                                        #html.A(className="fas fa-filter",id="",style={"padding-right":"10px","color":"white", "text-decoration":"none"}),
                                                        #html.A(className="fas fa-sync",id="",style={"padding-right":"10px","color":"white","text-decoration":"none"}),
                                                        #html.A(className="fa-solid fa-gears",id="",style={"padding-right":"10px", "color":"white","text-decoration":"none"}),
                                                        
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.H4("Primary card title", className="card-title"),
                                                        html.P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text"),
                                                    ],
                                                    className="card-body",
                                                ),
                                            ],
                                        className="card text-white bg-primary mb-3",
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 2########################################################################################################
card_2 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3(sql_queries.select_Firbezeichnung_sql()),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-body",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3("Settings"),
                                                        #html.A(className="fas fa-filter",id="",style={"padding-right":"10px","color":"white", "text-decoration":"none"}),
                                                        #html.A(className="fas fa-sync",id="",style={"padding-right":"10px","color":"white","text-decoration":"none"}),
                                                        #html.A(className="fa-solid fa-gears",id="",style={"padding-right":"10px", "color":"white","text-decoration":"none"}),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.H4("Primary card title", className="card-title"),
                                                        html.P("Some quick example text to build on the card title and make up the bulk of the card's content.", className="card-text"),
                                                    ],
                                                    className="card-body",
                                                ),
                                            ],
                                        className="card text-white bg-primary mb-3",
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card2",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 3 #################################################################################################
card_3 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                        children=[
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start active",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.H5("List group item heading", className="mb-1"),
                                                            html.Small("3 days ago"),
                                                        ],
                                                        className="d-flex w-100 justify-content-between",
                                                    ),
                                                    html.P("Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.", className="mb-1"),
                                                    html.Small("Donec id elit non mi porta."),
                                                ],
                                            ),
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start",
                                                children=[
                                                    html.Div(className="d-flex w-100 justify-content-between",
                                                        children=[
                                                          html.H5("List group item heading",className="mb-1"),  
                                                          html.Small("3 days ago", className="text-muted"),
                                                        ],
                                                    ),
                                                    html.P("Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.", className="mb-1"),
                                                    html.Small("Donec id elit non mi porta.", className="text-muted"),
                                                ],
                                            ),

                                        ],
                                        style={"text-align":"left"},
                                        className="list-group",
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                        children=[
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start active",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.H5("Settings", className="mb-1"),
                                                        #html.A(className="fas fa-filter",id="",style={"padding-right":"10px","color":"white", "text-decoration":"none"}),
                                                        #html.A(className="fas fa-sync",id="",style={"padding-right":"10px","color":"white","text-decoration":"none"}),
                                                        #html.A(className="fa-solid fa-gears",id="",style={"padding-right":"10px", "color":"white","text-decoration":"none"}),
                                                        ],
                                                        className="d-flex w-100 justify-content-between",
                                                    ),
                                                    html.P("Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.", className="mb-1"),
                                                    html.Small("Donec id elit non mi porta."),
                                                ],
                                            ),
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start",
                                                children=[
                                                    html.Div(className="d-flex w-100 justify-content-between",
                                                        children=[
                                                          html.H5("List group item heading",className="mb-1"),  
                                                          html.Small("3 days ago", className="text-muted"),
                                                        ],
                                                    ),
                                                   html.P("Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.", className="mb-1"),
                                                   html.Small("Donec id elit non mi porta.", className="text-muted"),
                                                ],
                                            ),

                                        ],
                                        className="list-group",
                                    ),

                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card2",
            ),
        ],
    ),
    ],

)
#########################################################################################################

#Card 4 #################################################################################################
card_4 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                        children=[
                                            html.Ul(
                                                children=[
                                                    html.Li(
                                                        children=[
                                                            html.P(sql_queries.select_Firbezeichnung_sql()),
                                                            html.Span("  ", className="badge bg-primary rounded-pill"),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P(sql_queries.select_AbrechnungsJahr_sql()),
                                                            html.Span("  ",className="badge bg-primary rounded-pill"),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P(sql_queries.select_Nachname_sql()),
                                                            html.Span("  ", className="badge bg-primary rounded-pill"),
                                                        ],
                                                        style={"height":"85px","background-color":"#78C2AD"},
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                ],
                                                style={"min-width":"500px", "min-height":"200px", "color":"black"},
                                                className="list-group",
                                            ),
                                            html.Br(),
                                        ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                        children=[
                                            html.Ul(
                                                children=[
                                                    html.Li(
                                                        children=[
                                                        html.H5("Settings"),
                                                        #html.A(className="fas fa-filter",id="",style={"padding-right":"10px","color":"white", "text-decoration":"none"}),
                                                        #html.A(className="fas fa-sync",id="",style={"padding-right":"10px","color":"white","text-decoration":"none"}),
                                                        #html.A(className="fa-solid fa-gears",id="",style={"padding-right":"10px", "color":"white","text-decoration":"none"}),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P("Dapibus ac facilisis in"),
                                                            html.Span("",className="badge bg-primary rounded-pill"),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P("Morbi leo risus"),
                                                            html.Span("", className="badge bg-primary rounded-pill"),
                                                        ],
                                                        style={"height":"85px"},
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                ],
                                                style={"min-width":"500px", "color":"black"},
                                                className="list-group",
                                            ),
                                            html.Br(),
                                        ],
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card2",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 5##################################################################################################
card_5 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                        children=[
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start active",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.H5(sql_queries.select_Firbezeichnung_sql(), className="mb-1"),
                                                        ],
                                                        className="d-flex w-100 justify-content-between",
                                                    ),
                                                    html.Small(sql_queries.select_AbrechnungsJahr_sql()),
                                                    html.Br(),
                                                    html.Small(sql_queries.select_Nachname_sql()),
                                                ],
                                                style={"height":"100px"},
                                            ),
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.H5(sql_queries.select_Firbezeichnung_sql(), className="mb-1"),
                                                        ],
                                                        className="d-flex w-100 justify-content-between",
                                                    ),
                                                    html.Small(sql_queries.select_AbrechnungsJahr_sql()),
                                                    html.Br(),
                                                    html.Small(sql_queries.select_Nachname_sql()),
                                                ],
                                                style={"height":"100px"},
                                            ),
                                        ],
                                        style={"text-align":"left", "height":"200px"},
                                        className="list-group",
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                        children=[
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start active",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                        html.H5("Settings", className="mb-1"),
                                                        #html.A(className="fas fa-filter",id="",style={"padding-right":"10px","color":"white", "text-decoration":"none"}),
                                                        #html.A(className="fas fa-sync",id="",style={"padding-right":"10px","color":"white","text-decoration":"none"}),
                                                        #html.A(className="fa-solid fa-gears",id="",style={"padding-right":"10px", "color":"white","text-decoration":"none"}),
                                                        ],
                                                        className="d-flex w-100 justify-content-between",
                                                    ),
                                                    html.Small(sql_queries.select_AbrechnungsJahr_sql()),
                                                    html.Small(sql_queries.select_Nachname_sql()),
                                                ],
                                                style={"height":"100px"},
                                            ),
                                            html.A(href="#", className="list-group-item list-group-item-action flex-column align-items-start",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.H5("Settings", className="mb-1"),
                                                        ],
                                                        className="d-flex w-100 justify-content-between",
                                                    ),
                                                    html.Small(sql_queries.select_AbrechnungsJahr_sql()),
                                                    html.Br(),
                                                    html.Small(sql_queries.select_Nachname_sql()),
                                                ],
                                                style={"height":"100px"},
                                            ),

                                        ],
                                        style={"text-align":"left"},
                                        className="list-group",
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 6 #################################################################################################
card_6 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                        children=[
                                            html.Ul(
                                                children=[
                                                    html.Li(
                                                        children=[
                                                            html.P(sql_queries.select_Firbezeichnung_sql()),
                                                            html.Span("  ", className="badge bg-primary rounded-pill"),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P(sql_queries.select_AbrechnungsJahr_sql()),
                                                            html.Span("  ",className="badge bg-primary rounded-pill"),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P(sql_queries.select_Nachname_sql()),
                                                            html.Span("  ", className="badge bg-primary rounded-pill"),
                                                        ],
                                                        style={"height":"85px","background-color":"#78C2AD"},
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                ],
                                                style={"min-width":"100px", "min-height":"200px", "color":"black"},
                                                className="list-group",
                                            ),
                                            html.Br(),
                                        ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                        children=[
                                            html.Ul(
                                                children=[
                                                    html.Li(
                                                        children=[
                                                            html.P("Settings"),
                                                            html.Span("", className="badge bg-primary rounded-pill"),
                                                        #html.A(className="fas fa-filter",id="",style={"padding-right":"10px","color":"white", "text-decoration":"none"}),
                                                        #html.A(className="fas fa-sync",id="",style={"padding-right":"10px","color":"white","text-decoration":"none"}),
                                                        #html.A(className="fa-solid fa-gears",id="",style={"padding-right":"10px", "color":"white","text-decoration":"none"}),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P("Dapibus ac facilisis in"),
                                                            html.Span("",className="badge bg-primary rounded-pill"),
                                                        ],
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                    html.Li(
                                                        children=[
                                                            html.P("Morbi leo risus"),
                                                            html.Span("", className="badge bg-primary rounded-pill"),
                                                        ],
                                                        style={"height":"85px"},
                                                        className="list-group-item d-flex justify-content-between align-items-center",
                                                    ),
                                                ],
                                                style={"min-width":"100px", "color":"black"},
                                                className="list-group",
                                            ),
                                            html.Br(),
                                        ],
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                style={"wisth":"100px"},
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 7 #################################################################################################
card_7 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H5(sql_queries.select_Firbezeichnung_sql()),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                    ],
                                                    className="card-body",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H5("Settings", className="mb-1"),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                    ],
                                                    className="card-body",
                                                ),
                                            ],
                                        className="card text-white bg-primary mb-3",
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card3",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 8 #################################################################################################
card_8 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3(sql_queries.select_Firbezeichnung_sql()),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),

                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-header",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3("Settings"),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),

                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-header",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card2",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 9 #################################################################################################
card_9 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H4(sql_queries.select_Firbezeichnung_sql(),className="card-title"),
                                                    html.H6(sql_queries.select_FirmenNr(),className="card-subtitle mb-2 text-muted"),
                                                    html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                    html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    html.A("Card link", href="#", className="card-link"),
                                                ],
                                                style={"color":"#008eac", "height":"200px"},
                                                className="card-body",
                                            ),
                                        ],
                                        style={"background-color":"white"},
                                        className="card",
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H4("Settings",className="card-title"),
                                                    html.H6(sql_queries.select_FirmenNr(),className="card-subtitle mb-2 text-muted"),
                                                    html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                    html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    html.A("Card link", href="#", className="card-link"),
                                                ],
                                                style={"color":"#008eac", "height":"200px"},
                                                className="card-body",
                                            ),
                                        ],
                                        style={"background-color":"white"},
                                        className="card",
                                    ),

                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 10 #################################################################################################
card_10 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H4(sql_queries.select_Firbezeichnung_sql(),className="card-title"),
                                                    html.H6(sql_queries.select_FirmenNr(),className="card-subtitle mb-2 text-muted"),
                                                    html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                    html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    html.A("Card link", href="#", className="card-link"),
                                                ],
                                                style={"color":"#008eac", "height":"200px"},
                                                className="card-body",
                                            ),
                                        ],
                                        style={"background-color":"white"},
                                        className="card",
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                        children=[
                                            html.Div(
                                                children=[
                                                    html.H4("Settings",className="card-title"),
                                                    html.H6(sql_queries.select_FirmenNr(),className="card-subtitle mb-2 text-muted"),
                                                    html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),
                                                    html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    html.A("Card link", href="#", className="card-link"),
                                                ],
                                                style={"color":"#008eac", "height":"200px"},
                                                className="card-body",
                                            ),
                                        ],
                                        style={"background-color":"white"},
                                        className="card",
                                    ),

                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card2",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 11 #################################################################################################
card_11 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3(sql_queries.select_Firbezeichnung_sql()),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),

                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-header",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H3("Settings"),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),

                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-header",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 12 #################################################################################################
card_12 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H6(sql_queries.select_Firbezeichnung_sql()),
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),

                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-header",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                    html.Div(
                                    children=[
                                        html.Div(style={"height": "200px"},
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.H6("Settings"),
                                                    ],
                                                   
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_AbrechnungsJahr_sql(),className="card-text"),

                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        
                                                        html.P(sql_queries.select_FirmenNr(),className="card-text"),
                                                        
                                                    ],
                                                    className="card-header",
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.P(sql_queries.select_Nachname_sql(),className="card-text"),
                                                    ],
                                                    className="card-header",
                                                ),
                                            ],
                                            className="card text-white bg-primary mb-3",
                                        ),
                                    ],
                                    ),
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card3",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 13 #################################################################################################
card_13 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 14 #################################################################################################
card_14 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 15 #################################################################################################
card_15 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 16 #################################################################################################
card_16 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 17 #################################################################################################
card_17 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 18 #################################################################################################
card_18 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 19 #################################################################################################
card_19 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################

#Card 20 #################################################################################################
card_20 = html.Div(
    children=[
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                [
                                    #Content of the Card Front

                                ],
                                className="flip-card-front",
                            ),
                            html.Div(
                                [
                                    #Content of the Card Back
                                ], 
                                className="flip-card-back",
                            ),
                        ],
                        className="flip-card-inner",
                    ),
                ],
                className="flip-card",
            ),
        ],
    ),
    ],
)
#########################################################################################################
