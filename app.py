import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

Plants_df = pd.read_excel('Plants_Plot_Data.xlsx')
# latitude=[-30,-32,-28]
# longitude=[121,115,122]
# facilities=['Kalgoorlie Smelter','Kwinana Refinery', 'Murrin Murrin']
# process = ['Matte Smelter', 'Metal Refinery','Lat Leach']
# capacity=[110,79,40]
          
#d = {'col1': [1, 2], 'col2': [3, 4]}
#df = pd.DataFrame(data=d)


Refine_fig = px.scatter_geo(data_frame= Plants_df,
                    lon = 'long',
                    lat = 'lat',
                    color='type', # which column to use to set the color of markers
                    hover_name='name', # column added to hover information
                    size='capacity', # size of markers
                    projection="natural earth")
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='NickelRefineries'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1('Global Nickel Processors by Location and Capacity. \Click on legend item to remove process type, \double click to isolate process type'),
    dcc.Graph(
        id='flyingdog',
        figure=Refine_fig
    )]
)

if __name__ == '__main__':
    app.run_server()