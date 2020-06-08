"""
This module contains the layout for the second tab of the visualization.
It is being called by main.py.
"""
import os
import dash_html_components as html
import dash_core_components as dcc
from bingewatch import imdb

DATA_DIR = 'bingewatch/data'
PROCESSED_DIR = 'processed'
IMDB_FILE = 'imdb_df.csv'
GENRES_FILE = 'set_genres.pkl'
IMDB_PATH = os.path.join(DATA_DIR, PROCESSED_DIR, IMDB_FILE)
GENRES_PATH = os.path.join(DATA_DIR, PROCESSED_DIR, GENRES_FILE)
DF_IMDB = imdb.load_data(IMDB_PATH)
GENRES = imdb.load_genres(GENRES_PATH)


EXTERNAL_STYLESHEETS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

TAB2_LAYOUT = html.Div([
    html.Div([
        html.Label('Filter by:'),
        dcc.Checklist(
            id='filter-checklist',
            options=[
                {'label': 'Genre', 'value': 'Genre'},
                {'label': 'Year', 'value': 'Year'}],
            value=['Genre', 'Year'])],
             style={'margin-bottom': '50px', 'margin-left':'20px'}),
    html.Div(id='slider-wrapper', children=[
        html.Label('Year:'),
        dcc.Slider(
            id='year-slider',
            min=int(DF_IMDB['startYear'].min()),
            max=int(DF_IMDB['startYear'].max()),
            value=int(DF_IMDB['startYear'].max()),
            included=False,
            updatemode='drag',
            tooltip={'always_visible': True})],
             style={'margin-bottom': '50px',
                    'margin-left': '20px',
                    'margin-right': '20px',
                    'text-orientation': 'mixed'}),
    html.Div([
        html.Div([
            html.Label('Select the genre you would like to see:'),
            dcc.Dropdown(
                id='genre-dropdown',
                options=[{'label': i, 'value': i} for i in GENRES],
                placeholder='Select Genre',)],
                 style={'width': '48%',
                        'margin-bottom': '50px',
                        'margin-left':'20px',
                        'display': 'inline-block'}),
        html.Div([
            html.Label('Select the type of content you would like to see:'),
            dcc.RadioItems(
                id='title-type',
                options=[{'label': 'Movie', 'value' : 'movie'},
                         {'label' :'TV Series', 'value': 'tvSeries'}],
                value='movie',
                labelStyle={'display': 'inline-block', 'padding': '10px'})],
                 style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        ]),

    html.Div([
        dcc.Graph(style={'height': '400px',
                         'width': '1300px',
                         'margin-left':'auto',
                         'margin-right':'auto'},
                  id='graph-with-slider')])
    ])
