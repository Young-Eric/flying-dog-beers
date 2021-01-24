import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

latitude=[-30,-32,-28]
longitude=[121,115,122]
facilities=['Kalgoorlie Smelter','Kwinana Refinery', 'Murrin Murrin']
process = ['Matte Smelter', 'Metal Refinery','Lat Leach']
capacity=[110,79,40]
          
#d = {'col1': [1, 2], 'col2': [3, 4]}
#df = pd.DataFrame(data=d)


Refine_fig = px.scatter_geo(
                    lon = longitude,
                    lat = latitude,
                    color=process, # which column to use to set the color of markers
                    hover_name=facilities, # column added to hover information
                    size=capacity, # size of markers
                    projection="natural earth")
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='NickelRefineries'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1('Refine'),
    dcc.Graph(
        id='flyingdog',
        figure=Refine_fig
    )]
)

if __name__ == '__main__':
    app.run_server()