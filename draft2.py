from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash(__name__)

df=pd.read_csv("./data/shinyMetadat.csv")
print(df.columns)
val=df.columns[0]
print(val)