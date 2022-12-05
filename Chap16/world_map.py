from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

for eq_dict in all_eq_dicts:

# Map the earthquakes.
data = [Scattergeo(lon=eq_dict, lat=eq_dict)]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')