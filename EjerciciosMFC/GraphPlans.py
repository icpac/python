"""
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/tiago-peres/immersion/master/Platforms_dataset.csv')
fig = px.scatter_3d(df, x='Functionality ', y='Accessibility', z='Immersion', color='Platforms')

bright_blue = [[0, '#7DF9FF'], [1, '#7DF9FF']]
bright_pink = [[0, '#FF007F'], [1, '#FF007F']]
light_yellow = [[0, '#FFDB58'], [1, '#FFDB58']]

# need to add starting point of 0 to each dimension so the plane extends all the way out
zero_pt = pd.Series([0])
z = zero_pt.append(df['Immersion'], ignore_index = True).reset_index(drop = True)
y = zero_pt.append(df['Accessibility'], ignore_index = True).reset_index(drop = True)
x = zero_pt.append(df['Functionality '], ignore_index = True).reset_index(drop = True)

length_data = len(z)
z_plane_pos = 40*np.ones((length_data,length_data))

fig.add_trace(go.Surface(x=x, y=y, z=z_plane_pos, colorscale=light_yellow,  showscale=False))
fig.add_trace(go.Surface(x=x.apply(lambda x: 10), y=y, z = np.array([z]*length_data), colorscale= bright_blue, showscale=False))
fig.add_trace(go.Surface(x=x, y= y.apply(lambda x: 30), z =  np.array([z]*length_data).transpose(), colorscale=bright_pink, showscale=False))

fig.show()
"""

"""
import plotly.graph_objects as go
import pandas as pd
import numpy as np
# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))
fig.show()
"""
# x and y given as array_like objects
import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()