from asyncio.windows_events import NULL
from distutils.util import execute
from itertools import count
from pickle import NONE
from sqlite3 import Cursor
from typing import final
from numpy import empty, number, rint
import numpy as np
import pyodbc
import pandas as pd
from dash import *
from distutils.util import execute

# Verbindung mir der Datenbank##########################################################################
driver = "{ODBC Driver 17 for SQL Server}"  # Treiber
# virtueller machine - windows (microsoft) server - sql server wo die DB drauf ist
host = "vmwssql"
database = "db_Lohn"  # Name der DB
user = "sao"  # unser user (der Zugriff auf DB hat) - reiner DB-User
password = "sao"  # unser pw
connection = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + host +
                            ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)
########################################################################################################

#Variablen#############################################################################################
#cursor=connection.cursor()
cursor = connection.cursor()
cursor.execute("""SELECT @@VERSION as version""")
########################################################################################################

# 1 Connection Test#####################################################################################
def ConnectionTest_sql():
    if connection:
        print("Connection OK")
    else:
        print("Connect Error")
########################################################################################################

# 2 SELECT FirmenNr#####################################################################################
def select_FirmenNr():
    if connection:
        fields_notes_list = ['old_notes']
        cursor.execute("SELECT FirmenNr FROM Firmen")
        for row in cursor.fetchall():
            for x in range(1):
                #print(row[x])
                return("Firmen Nummer: ",row[x])
    else:
        print("Some error"),
########################################################################################################  

# 3 SELECT FirmenBezeich1###############################################################################
def select_Firbezeichnung_sql():
    if connection:
        fields_notes_list = ['old_notes']
        cursor.execute("SELECT FirmenBezeich1 FROM Firmen")
        for row in cursor.fetchall():
            for x in range(1):
                #print(row[x])
                return(row[x])
    else:
        print("Some error"),
########################################################################################################

# 4 SELECT AbrechnungsJahr #############################################################################
def select_AbrechnungsJahr_sql():
    if connection:
        cursor.execute("SELECT AbrechnungsJahr FROM Firmen")
        for row in cursor.fetchall():
            for x in range(1):
                #print(row[x])
                return("Abrechnungsjahr Jahr: " ,row[x])
    else:
        print("Some error"),
########################################################################################################

# 5 SELECT Nachname #############################################################################
def select_Nachname_sql():
    if connection:
        cursor.execute("""SELECT Nachname FROM Personal WHERE PersonalNr = 1""")
        for row in cursor.fetchall():
            for x in range(1):
                #print(row[x])
                return("Nachname: ", row[x])
    else:
        print("Some error"),
########################################################################################################

