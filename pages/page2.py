from dash import Dash, dcc, html, Input, Output, callback

import plotly.express as px
import pandas as pd
from pandas.api.types import is_numeric_dtype

df=pd.read_csv("./data/bactopia-report.txt", sep='\t')
#print(list(df.columns))
#print(is_numeric_dtype(df['final_read_min']))
valName=df.columns[1]

colNames=list(df.columns)

layout= html.Div([
    html.H1('Bactopia sumary'),
    html.Div([
        dcc.Link('Go to Page 1', href='/page1'),
        html.Br(),
        dcc.Dropdown(id='bactOption',
        options= colNames, value=valName)
        ]),
    dcc.Graph(id='sumBact')

    ])

@callback(
    Output(component_id='sumBact',component_property='figure'),
    Input(component_id='bactOption', component_property='value')
)

def update_output_div(colOption):
    if is_numeric_dtype(df[colOption])== True:
        fig = px.histogram(df, x=colOption) 
    else:
        byGroup=df.groupby(colOption).size()
        byGroupDf=byGroup.reset_index()
        mapping={byGroupDf.columns[0]: colOption, byGroupDf.columns[1]: 'Freq'}
        freqDf=byGroupDf.rename(columns=mapping)
        fig=px.bar(freqDf, x=colOption, y='Freq', title=colOption, \
            labels={colOption: colOption}, color=colOption)
    return fig