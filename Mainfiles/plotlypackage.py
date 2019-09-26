import os
import plotly.graph_objects as go
import io
from PIL import Image

def makeimage():
    fig = go.Figure(go.Bar(
        x=[8, 2],
        y=['yes', 'no'],
        orientation='h'))

    fig.show()

    if not os.path.exists("images"):
        os.mkdir("images")

    return fig.to_image(format="png")