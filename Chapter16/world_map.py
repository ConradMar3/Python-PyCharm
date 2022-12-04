from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

eq_dict: object
for eq_dict in all_eq_dicts:

# Map the earthquakes.
    data = [Scattergeo(lon=lons, lat=lats)]
    my_layout = Layout(title='Global Earthquakes')
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes.html')