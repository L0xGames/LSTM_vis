import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd

df=pd.read_csv('/Users/kiandousti/Downloads/TSLA.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)



app.layout = html.Div([
    html.Div([
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
        ], className="six columns"),

        html.Div([
            html.H1('Square Root Slider Graph'),
            dcc.Graph(id='slider-graph2', figure={
                          'data': [
                              go.Scatter(
                                  x=df.Date[:5],
                                  y=df.Open[:5],
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
                      }, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
        ], className="six columns"),
    ], className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})






# @app.callback(
#                [Output('slider-graph2', 'figure')],
#               [Input('slider-updatemode2', 'value')])
# def display_value(value):
#     x = []
#     for i in range(value):
#         x.append(i)
#
#     y = []
#     for i in range(value):
#         y.append(i*i)
#
#     graph = go.Scatter(
#         x=x,
#         y=y,
#         name='Manipulate Graph'
#     )
#     layout = go.Layout(
#         paper_bgcolor='#27293d',
#         plot_bgcolor='rgba(0,0,0,0)',
#         xaxis=dict(range=[min(x), max(x)]),
#         yaxis=dict(range=[min(y), max(y)]),
#         font=dict(color='white'),
#
#     )
#     result={'data': [graph], 'layout': layout}
#     return result