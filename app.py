from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df=pd.read_csv("./data/shinyMetadat.csv")
byState=df.groupby('State').size()
byStateDf=byState.reset_index()
mapping = {byStateDf.columns[0]: 'State', byStateDf.columns[1]: 'Freq'}
byStateDfN=byStateDf.rename(columns=mapping)

fig=px.bar(byStateDfN, x="State", y="Freq")

app.layout= html.Div(children=[
    html.H1(children='Viz app'),
    dcc.Graph(id='Freq', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)