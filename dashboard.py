# dashboard.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.read_csv('cleaned_weather_data.csv')

fig = px.line(df, x='datetime', y='energy_demand', title='Energy Demand Over Time')

app.layout = html.Div(children=[
    html.H1(children='Energy Demand Dashboard'),

    dcc.Graph(
        id='energy-demand-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
