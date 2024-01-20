from dash import Dash, html, dcc
# import drop_down
import ids
import dash_bootstrap_components as dbc



all_runs = ["Run 63", "Run 697"]


def create_layout1(app: Dash) -> html.Div:
    navbar = dbc.NavbarSimple(
        # Existing code...
    )

    page_content = html.Div(className="app-div", children=[
        navbar,
        html.Hr(),
        html.Div(
            className="dropdown-container",
            style={"padding" : "10px"},
            children=[
                # Dropdown for selecting runs...
                html.Div(
                    children=[
                        dbc.Row([
                            dbc.Col(
                                [
                                    html.H6("Runs"),
                                ],
                                width={"size": 1, "offset": 0},
                            ),
                            dbc.Col([
                                dbc.Select(
                                    all_runs,
                                    all_runs[0],
                                    id=ids.RUN_DROPDOWN,
                                    style={"width" : "100px"}
                                )
                            ],  width={"size": 4, "offset": 1},)
                        ])
                    ]
                ),
                # Additional feature on Page 2 (Graph, for example)...
                html.Div(
                    id=ids.RUN_63,  # Update the ID if needed
                    children=[
                        dcc.Graph(
                            id='example-graph',
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Page 2 Feature'},
                                ],
                                'layout': {
                                    'title': 'Page 2 Feature Graph'
                                }
                            }
                        )
                    ]
                )
            ]
        )
    ])

    return page_content
