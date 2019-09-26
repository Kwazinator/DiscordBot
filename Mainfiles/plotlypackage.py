import os
import plotly.graph_objects as go
import io
from PIL import Image

def makeimage():
    fig = go.Figure(go.Bar(
        x=[8, 2],
        y=['yes', 'no'],
        orientation='h'), layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(family='Courier New, monospace', size=30, color='#000000')))

    #fig.show()

    if not os.path.exists("images"):
        os.mkdir("images")

    return Image.open(io.BytesIO(fig.to_image(format="png")))
