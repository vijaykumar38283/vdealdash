import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
#from page1 import *
from piechart import fig
from alert import *
import fftcode


health=fftcode.syshealth
OVVB=fftcode.h



indexpage=html.Div([
   html.Br(),
    
    dcc.Link(dbc.Button("Graph Visulization",color="primary",  size="lg",className="mr-1"),href='/page-1',style={'display':'inline-block'}),
    
   dcc.Link(dbc.Button("Health Condition Of System",color="primary",  size="lg"), href='/page-2',style={'display':'inline-block'}),
   html.Br(),
   html.H1(["Welcome to Data Visulization of Sensor"],style={'color':'white','display':'inline-block'}),
                       dcc.Graph(id='pie',figure=fig,style={'position':'relative',
                                                            'right':20,
                                                            'top':0,
                                                            'float':'right',
                                                            'display':'inline-block'}),
   html.Br(),html.Br(),
   html.Div([html.P(["IF U WANT TO CHANGE ALERT VALUE :"]),
   dcc.Input(id='input',type='number',value=0.8)],style={'color':'white'}),

                       alert,
                       html.P(['Overall Vib is ',OVVB,'mm/sec and Health is ',health,'% Good Condition'],style={'color':'white'}), 
                       html.Br(),html.Br(),
                       html.Div([
                       html.P(["Live Timer"],style={'color':'white','font-size':20}),html.Br(),
                       html.Div(id='live-update-text',
                                style={'color':'white','font-size': '40px',"border":"2px white solid",'width':'15%'}),
                       dcc.Interval(
                                    id='interval-component',
                                    interval=1*1000, # in milliseconds
                                    n_intervals=0
                                    )]),
   
   
   
   html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
#Timer Division start here   
html.Br(),html.Br(),html.Br(),html.Br(),html.Br()
])  
