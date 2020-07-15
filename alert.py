import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input, State

alert=html.Div([ dbc.Alert(
                    "Please Check the System becuase an Alert was Raised",
                    id='alert1',
                    dismissable=True,
                    is_open=False,
                    fade=True,
                    #duration=30000,
                    style={'position':'fixed',
                            'color':'blue',
                            'font-size':20,
                            'width':500,
                            'border':'1px lightgrey',
                            'height':70,
                            'box-shadow': '8px 8px 8px lightgrey',
                            'top':70,
                            'right':20,
                            'font': '20px Arial, sans-serif'
                            
                            
                            },
                          
                )])