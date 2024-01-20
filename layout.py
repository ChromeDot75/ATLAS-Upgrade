from dash import Dash, html, dcc
# import drop_down
import ids
import dash_bootstrap_components as dbc



all_runs = ["Run 63", "Run 697"]



def create_layout(app: Dash) -> html.Div:
    

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand=app.title,
        brand_href="#",
        color="primary",
        dark=True,
    )
    return html.Div(className="app-div", children=[navbar, html.Hr(),
    html.Div(
        className="dropdown-container",
        style={"padding" : "10px"},
        children=[
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
            # drop_down.render(app),
    html.Div(
        id = ids.RUN_63
    )
        ]
    
    )])
   