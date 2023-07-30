import plotly.express as px
import pandas as pd
from dash import dcc, html, Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server
df = pd.read_csv('myfile.csv')
df2 = pd.read_csv('myfile.csv')

eu_index = df2[ df2['Country'] == 'EU 28 Total' ].index
df.drop(eu_index, inplace = True)

colors = {
    'background': '#fffff5',
    'text': '#7FDBFF'
}

fig = px.bar(df2, x='Country', y='Vehicle ownership', title='EU Vehicle Ownership Per 1000', barmode='group')
fig.update_layout(
)

fig2 = px.bar(df2, x="Country", y=["Population density", "Vehicle ownership", "Total road deaths"],
              title="Ratio of Population density, Vehicle ownership and Total road deaths per country")

fig3 = px.pie(df2, values='Road deaths per Million Inhabitants', names='Country', title='Road deaths per Million Inhabitants')

app.layout = html.Div(
    children=[
        html.H1(children='European Union Road Safety Visualizations'),
        html.Div(children='For the Challenge'),
        dcc.Graph(
            id='chart',
            figure=fig
        ),
        dcc.Graph(
            id='chart2',
            figure=fig2
        ),
       dcc.Graph(
            id='chart3',
            figure=fig3
        )
    ]
)

if __name__ == '__main__':
    app.run_server(host="192.168.1.6", port=8056, debug=True)