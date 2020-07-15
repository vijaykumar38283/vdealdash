import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
from fftcode import df1

df=df1
data1=['X_axis','Y_axis','Z_axis']
data2=['None','X_axis','Y_axis','Z_axis']




pageone=html.Div([html.Div(['This is Visualization Page'],style={'color':'white'}),
    
    html.Div([
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link(dbc.Button('Home',color='success',size='lg'), href='/',style={'display':'inline-block'}),
    dcc.Link(dbc.Button('Select Health Condition \n of System',size='lg',color='primary'), href='/page-2',style={'display':'inline-block'}),],style={'float':'right'}),


    html.H1(children='DATA VISUALIZATION',style={'color':'white'}),
    #html.Img(src=app.get_asset_url('vdeallogo.png'), style={'height':'10%', 'width':'10%','float': 'right','-webkit-stroke-width': '1.5px','-webkit-stroke-color': 'white','block-shadow': '-2px 2px 2px #999'}),
    
    html.Div([   
            html.H1(["Select Date:"],style={'color':'white'}),
    dcc.DatePickerRange(
        id='my-date',
        month_format='MMM-Y',
        min_date_allowed=dt(1994, 6, 20),
        max_date_allowed=dt(2030, 12, 31),
        initial_visible_month=dt(2019, 8, 1),
        start_date=str(dt(2019, 8, 2)),
        end_date=str(dt(2019, 8, 25)) 
        )]),
    html.Div([ html.P(["Select Graph Data"]),
               dcc.Dropdown(id='drop1',
                     options=[{'label': k, 'value': k} for k in data1],
                      value='X_axis'),
               ],
                     style={'width':'10%'}),
             
            
    html.Div([
    dcc.Graph(id='graph-1')],style={"padding":20,'width':'70%','height':'50%','position':'center'})
   
])
#page-1 end hear with dropdown and date picker