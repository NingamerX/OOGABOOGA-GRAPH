import pandas as p
import plotly.express as px

dataframe = p.read_csv("data.csv")

fig = px.scatter(dataframe, x="date",y="cases")

fig.show()