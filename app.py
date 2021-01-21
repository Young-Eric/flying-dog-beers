import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

Plants = pd.read_excel('Plants_Plot_Data.xlsx', sheet_name='PlotData')
Plants.head(2)

########### Define your variables
beers=['Chained Stout', 'Snake Dog IPA', 'Imperial Porter', 'Does this work Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'

beer_fig = px.scatter_geo(Plants, 
#                      locations="iso_alpha",
                    lon = Plants['long'],
                    lat = Plants['lat'],
                    color="type", # which column to use to set the color of markers
                    hover_name="name", # column added to hover information
                    size="capacity", # size of markers
                    projection="natural earth")

#beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
