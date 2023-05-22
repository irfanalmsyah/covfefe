import json
import pandas as pd
import plotly.express as px

colorscale = ["#ffffff", "#ece0d1", "#dbc1ac", "#967259", "#634832", "#38220f"]

with open("indonesia.geojson") as f:
    geojson = json.load(f)

df = pd.read_csv("covfefe.csv")
df_reshaped = df.melt(
    id_vars=["Provinsi"],
    var_name="Year",
    value_name="Produktivitas Kopi"
)

fig = px.choropleth(
    df_reshaped,
    geojson=geojson,
    locations="Provinsi",
    featureidkey="properties.state",
    animation_frame="Year",
    color="Produktivitas Kopi",
    color_continuous_scale=colorscale,
    labels={"Produktivitas Kopi": "Produktivitas Kopi (Kg/Ha)"},
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    title={
        "text": "Produktivitas Kopi di Indonesia",
        "xanchor": "center",
        "x": 0.5,
        "yanchor": "top",
        "y": 0.9,
    }
)
fig.show()
