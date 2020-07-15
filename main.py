import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
import pandas as pd
import numpy as np
from datetime import datetime as dt
from math import sqrt
import scipy.fftpack as fft
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from piechart import fig
import alert
import fftcode
import index

from page1 import pageone

health=fftcode.syshealth
OVVB=fftcode.h
df=fftcode.df1
data1=['X_axis','Y_axis','Z_axis']
data2=['None','X_axis','Y_axis','Z_axis']

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=html.Div([
                        

                       dcc.Location(id='url'),
                       html.Div(id='page-content'),
                       
                       

                    ])

index_page=html.Div([html.Img(src=app.get_asset_url('/vdeallogo.png'), style={'position':'inline-block',
                            'top':30,
                            'left':30,
                            'height':'20%','width':'10%'}),
                            html.Img(src=app.get_asset_url('/iotpic.png'), style={'position':'inline-block',
                            'top':30,
                            'float':'right',
                            'height':'70%','width':'35%'}),
   index.indexpage,

],style={'background-image':'url("/assets/three.jpg")','background-repeat':'no-repeat','background-size':'1600px 1200px','padding':'10px'})


page_1_layout=html.Div([html.Img(src=app.get_asset_url('/vdeallogo.png'), 
                                style={'height':'10%','width':'10%','float':'right'}),
                            pageone,
                            ],style={'background-image':'url("/assets/three.jpg")','background-repeat':'no-repeat','background-size':'1600px 1200px','padding':'100px'})
#page-1 end hear with dropdown and date picker


#index_page=index_page1
#timer callback function
@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_date(n):
      return [html.P('' +str(dt.now().strftime('%H:%M:%S')))]

#timer division end here

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here
@app.callback(
    Output('graph-1', 'figure'),
    [Input('my-date', 'start_date'),
     Input('my-date', 'end_date'),
     Input('drop1', 'value')])

def update_output(start_date, end_date,axisone):
    
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    df2 = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    
    df3=df2
    
    
    return {'data':[
            {'x':df3['date'],'y':df3[axisone],'name':'Trace-1'}
                    ]
                    
            ,'layout':{'title':'Selected Data',
            
            'transition': {
                'duration': 500,
                'easing': 'cubic-in-out'
            }
            
            }
            }

#callback function End for date time and dropdown
@app.callback(
            Output("alert1","is_open"),
            [Input("input","value")])
def alert_data(nn):
    
    
   # print(nn)
    n=df.Overall_vibration.max()
    if n>=nn:
        return True
    else:
        return False
        



if __name__==("__main__"):
    app.run_server()