from pathlib import Path
import json
import plotly.express as px
px.colors.named_colorscales()

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

all_eq_dicts=all_eq_data['features']
#print(len(all_eq_dicts))

mags,lons,lats,eq_titles=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    lon =eq_dict['geometry']['coordinates'][0]
    lat =eq_dict['geometry']['coordinates'][1]
    eq_title=eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
print(mags[:10])
print(lats[:5])
print(lons[:5])

title='Global Earthquakes'
fig= px.scatter_geo(lat=lats,lon=lons,title=title,size=mags,color=mags,color_continuous_scale='aggrnyl',labels={'color':'magnitude'},projection='natural earth',hover_name=eq_titles)
fig.show()