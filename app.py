from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash(__name__)

df=pd.read_csv("./data/shinyMetadat.csv")
print(list(df.columns))

app.layout= html.Div([
    html.H1('Viz app'),
    html.Div([
        dcc.Dropdown(id='dropdown',
        options= [ 
            {'label':'State', 'value':'State'},
            {'label':'Streptomycin', 'value':'Streptomycin'},
            ],
        value='State')]),
    dcc.Graph(id='Freq')

    ])

from dash import Dash, dcc, html, Input, Output 

@app.callback(
    Output(component_id='Freq',component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def update_output_div(dropdown_value):
    byGroup=df.groupby('{}'.format(dropdown_value)).size()
    byGroupDf=byGroup.reset_index()
    mapping = {byGroupDf.columns[0]: 'State', byGroupDf.columns[1]: 'Freq'}
    byStateDfN=byGroupDf.rename(columns=mapping)
    fig=px.bar(byStateDfN, x="State", y="Freq")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)