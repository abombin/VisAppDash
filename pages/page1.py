from dash import Dash, dcc, html, Input, Output, callback

import plotly.express as px
import pandas as pd

df=pd.read_csv("./data/shinyMetadat.csv")
#print(list(df.columns))

layout= html.Div([
    dcc.Link('Go to Page 2', href='/page2'),
    html.H1('Meta Data Summary'),
    html.Div([
        dcc.Dropdown(id='dropdown',
        options= [ 
            {'label':'State', 'value':'State'},
            {'label':'Streptomycin', 'value':'Streptomycin'},
            ],
        value='State')]),
    dcc.Graph(id='Freq')

    ])



@callback(
    Output(component_id='Freq',component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
# '{}'.format(dropdown_value) makes sure to convert an input to a string

def update_output_div(dropdown_value):
    byGroup=df.groupby(dropdown_value).size()
    colName=dropdown_value
    byGroupDf=byGroup.reset_index()
    mapping = {byGroupDf.columns[0]: colName, byGroupDf.columns[1]: 'Freq'}
    byStateDfN=byGroupDf.rename(columns=mapping)
    fig=px.bar(byStateDfN, x=colName, y="Freq", title=colName, labels={colName: colName}, color=colName)
    return fig
