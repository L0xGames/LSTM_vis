import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
from django_plotly_dash import DjangoDash
import pandas as pd

df = pd.read_csv('/Users/kiandousti/Downloads/TSLA.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='Forecasting', children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='demo-dropdown',
                            options=[
                                {'label': 'Category: T-shirt', 'value': 'tshirt'},
                                {'label': 'Montreal', 'value': 'MTL'},
                                {'label': 'San Francisco', 'value': 'SF'}
                            ],
                            value='tshirt'
                        ),
                    ], className="three columns"),
                    html.Div([
                        html.Button(id='Forecast_Button', n_clicks_timestamp=0, children='Forecast')
                    ], className="one columns")
                ], className="row", style={"margin-left": "40%", "margin-top": 30, "margin-bottom": 30}),
                html.Div([
                    html.Div([
                        html.Button("Demand forecasting", id="demand", className="btn", style={"width": 230}),
                        html.Button("Avg. Price forecasting", id="avg", className="btn", style={"width": 230}),
                        html.Button("Stock Level forecasting", id="stock", className="btn", style={"width": 230}),
                    ], className="two columns", style={'margin-top': "10%", 'textAlign': 'center'}),
                    html.Div([
                        html.H1('Square Root Slider Graph'),
                        dcc.Graph(id='slider-graph',
                                  figure={
                                      'data': [
                                          go.Scatter(
                                              x=df.Date,
                                              y=df.Open,
                                              name='Manipulate Graph'
                                          )
                                      ],
                                      'layout': [
                                          go.Layout(
                                              paper_bgcolor='#27293d',
                                              plot_bgcolor='rgba(0,0,0,0)',
                                              xaxis=dict(range=[min([1, 2, 3, 4, 5, 6]), max([1, 2, 3, 4, 5, 6])]),
                                              yaxis=dict(range=[min([1, 2, 3, 4, 5, 6]), max([1, 2, 3, 4, 5, 6])]),
                                              font=dict(color='white'),

                                          )
                                      ]
                                  }
                                  , style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
                    ], className="five columns"),

                    html.Div([
                        html.H1('Square Root Slider Graph'),
                        dcc.Graph(id='slider-graph',
                                  figure={
                                      'data': [
                                          go.Scatter(
                                              x=df.Date,
                                              y=df.Open,
                                              name='Manipulate Graph'
                                          )
                                      ],
                                      'layout': [
                                          go.Layout(
                                              paper_bgcolor='#27293d',
                                              plot_bgcolor='rgba(0,0,0,0)',
                                              xaxis=dict(range=[min([1, 2, 3, 4, 5, 6]), max([1, 2, 3, 4, 5, 6])]),
                                              yaxis=dict(range=[min([1, 2, 3, 4, 5, 6]), max([1, 2, 3, 4, 5, 6])]),
                                              font=dict(color='white'),

                                          )
                                      ]
                                  }
                                  , style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
                    ], className="five columns"),
                ], className="row")

            ]),
            dcc.Tab(label='Retraining', children=[
                html.Div([
                    html.Div([
                        dcc.Upload(id="upload-data",
                                   children=html.Button('Upload Dataset', id='Upload_Button', n_clicks_timestamp=0))
                    ], className="three columns"),
                    html.Div([
                        html.Button(id='Retrain_Button', n_clicks_timestamp=0, children='Retrain')
                    ], className="two columns")
                ], className="row", style={"margin-left": "40%", "margin-top": 30, "margin-bottom": 30}),
                html.Div([
                    dcc.Textarea(style={"width": "95%", "margin-left": 40, "margin-right": 40, "height": 300},
                                 value="Log")
                ], className="row", style={"width": "100%"})
            ])])
    ], className="row"),

    html.Div([

    ], className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(
    #Output
    [],
    [Input('demand', 'n_clicks_timestamp'),Input('avg', 'n_clicks_timestamp'),Input('stock', 'n_clicks_timestamp'),Input('demo-dropdown', 'value'),
     Input('Forecast_Button', 'n_clicks_timestamp'),Input('Upload_Button', 'n_clicks_timestamp'),Input('Retrain_Button', 'n_clicks_timestamp') ,Input('upload-data', 'contents'),

     ],[State('upload-data', 'filename')])
def display_value(demand_f,avg_price_f,stock_f ,category_choice, forecast_btn,upload_btn,retrain_btn,list_of_contents, list_of_names):
    value=3
    x = []
    for i in range(value):
        x.append(i)

    y = []
    for i in range(value):
        y.append(i * i)

    graph = go.Scatter(
        x=x,
        y=y,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),

    )
    result = {'data': [graph], 'layout': layout}
    return None