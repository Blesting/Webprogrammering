import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
'''
x = np.arange(10)

fig = go.Figure(data=go.Scatter(x=x, y=x**2))
fig.show()
'''

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
data = go.Scatter(
    x = random_x,
    y = random_y
)

tls.get_embed("https://plot.ly/~blaesting/0")

fig = go.Figure(data)
#fig.show()
