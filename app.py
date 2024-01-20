from dash import Dash, html, dcc
from dash import callback, Input, Output
from layout import create_layout
#from layout1 import create_layout1
import dash_bootstrap_components as dbc
import dash.dependencies as dd
from callbacks import render as render_callback
import dash


def main() -> None:
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
    app.title = "Detector Tests"
    app.layout = create_layout(app)
    render_callback(app)
    app.run()

    

if __name__ == "__main__": 
    main()
    



"""


import pandas as pd
from SD import SD
from PTS import PTS
import matplotlib.pyplot as plt
import plotly.express as px
from dash.dependencies import Input, Output
import dash_html_components as html"""   