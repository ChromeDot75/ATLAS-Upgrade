from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import json
import numpy as np 
import matplotlib.pyplot as plt

class read_JSON:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def read_json(self):
        with open(self.filename, 'r') as file:
            self.data = json.load(file)

    def extract_numbers(self, keyword):
        if self.data is None:
            raise ValueError("JSON data not loaded. Call read_json() first.")

        numbers = []
        for item in self.data:
            if keyword in item:
                ps_current_value = item[keyword]
                if isinstance(ps_current_value, (int, float)):
                    numbers.append(ps_current_value)

        return numbers

# Example Usage
json_reader = read_JSON('your_json_file.json')
json_reader.read_json()

ps_current_numbers = json_reader.extract_numbers('PS_CURRENT')

# Convert the list to a numpy array for easier manipulation
ps_current_array = np.array(ps_current_numbers)


app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)