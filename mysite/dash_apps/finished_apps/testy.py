app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Square Root Slider Graph'),
            dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
            dcc.Slider(
                id='slider-updatemode',
                marks={i: '{}'.format(i) for i in range(20)},
                max=20,
                value=2,
                step=1,
                updatemode='drag',
            ),
        ], className="six columns"),

        html.Div([
            html.H1('Square Root Slider Graph'),
            dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
            dcc.Slider(
                id='slider-updatemode',
                marks={i: '{}'.format(i) for i in range(20)},
                max=20,
                value=2,
                step=1,
                updatemode='drag',
            ),
        ], className="six columns"),
    ], className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})