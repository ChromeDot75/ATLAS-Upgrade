from dash import Dash, html, dcc
from dash import callback, Input, Output
from dash.dependencies import Input, Output
from typing import List
import ids 
from IV import fig as graphIV
from IV import fig2 as graphIV2
from SD import fig as SDfig
from SD import fig2 as SDfig2 
from PTS import fig as PTSfig
from PTS import fig2 as PTSfig2
from error_TS import fig as errorTs_fig
from TS import TS_func
import dash_bootstrap_components as dbc


def render(app: Dash) -> html.Div: 
    
        # @app.callback(
    #     Output(ids.RUN_DROPDOWN, "value"),
    #     Input(ids.SELECT_ALL_RUNS_BUTTON, "n_clicks" )
    # )
      
    # def select_all_runs(n_clicks: int) -> List[str]:
    #     return all_runs


    @app.callback(  
            Output(ids.RUN_63, "children"),
            Input(ids.RUN_DROPDOWN, "value"),
            Input(ids.MODULE_DROPDOWN, "value"),
            Input(ids.STREAM_DROPDOWN, "value")
            
        ) 
    def render_63(value, module, stream):
        if value == "Run 63":
            div = html.Div([
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=graphIV),
                    ], width=6),
                    dbc.Col([
                        dcc.Graph(figure=SDfig),
                    ], width=6)
                ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=PTSfig),
                    ], width=6),
                    dbc.Col([
                        dcc.Graph(figure=errorTs_fig),
                    ], width=6),
                ]),
                   dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=TS_func(module, stream)),
                    ], width=12),
                ]),

            ])
            return div
        if value == "Run 697":
            div = html.Div([
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=graphIV2),
                    ], width=6),
                    dbc.Col([
                        dcc.Graph(figure=SDfig2),
                    ], width=6)
                ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=PTSfig2),
                    ], width=6),
                    dbc.Col([
                        dcc.Graph(figure=errorTs_fig), #change for the run 697.
                    ], width=6)
                ]),
                
            ])
            return div
        else:
            return None





