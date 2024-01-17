from django.shortcuts import render

# Create your views here.
from dash import Dash
import dash_html_components as html

def dash_plot(request):
    # Create a Dash app object
    app = Dash(__name__)

    # Define layout of the Dash app
    app.layout = html.Div(children=[
        html.H1(children='Dashboard'),
        # Add other components as needed
    ])

    # Run the Dash app
    return render(request, 'baseapp/index.html', {'baseapp': app})


def aichat(request):
    return render(request,'baseapp/aichat.html')

def addcase(request):
    return render(request,'baseapp/addcase.html')