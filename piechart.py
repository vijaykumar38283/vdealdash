
import plotly.graph_objects as go
from dash.dependencies import Output, Input, State
from fftcode import syshealth,f_stat



#for pie chart example started here 
fig=go.Figure(go.Pie(labels=['Good Condition', 'Faulty Condition'], values=[syshealth,f_stat], name='Health Condition'))
fig.update_traces(hole=.4, hoverinfo="label+percent+name")
fig.update_layout(
    title=dict(text="Health Status of Machine(Example) ", font=dict(size=36,color='white')),
    paper_bgcolor = "rgba(0, 0, 0, 0)",
    annotations=[dict(text='Health<br>Status of<br> Machine', font_size=15, font_color='white', showarrow=False)])