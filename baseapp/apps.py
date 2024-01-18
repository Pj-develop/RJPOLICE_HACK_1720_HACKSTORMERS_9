from django.apps import AppConfig


class BaseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baseapp'

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import base64
import io

# Create a Dash web application
app = dash.Dash(__name__)

# Define layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    dcc.Upload(
        id='upload-data',
        children=[
            html.Button('Select a File', style={'marginBottom': '10px'}),
            html.P('Drag and Drop or ', style={'marginBottom': '0px'}),
        ],
        multiple=False
    ),

    dcc.Graph(
        id='example-graph',
    )
])


# Callback to update the graph based on the uploaded file
@app.callback(
    Output('example-graph', 'figure'),
    [Input('upload-data', 'contents')]
)
def update_graph(contents):
    if contents is None:
        return px.bar(title='Upload a file to start')

    content_type, content_string = contents.split(',')
    decoded = io.StringIO(base64.b64decode(content_string).decode('utf-8'))

    # Assuming CSV format, you can modify this for PDF parsing if needed
    df = pd.read_csv(decoded)

    # Create a colored bar chart using Plotly Express
    fig = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[1],
                 title='Colored Bar Chart from Uploaded Data')

    return fig


# Run the application on port 8050
if __name__ == '__main__':
    app.run_server(port=8050)