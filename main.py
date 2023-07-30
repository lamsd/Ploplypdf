import plotly.express as px
import pdfkit
import pandas as pd
from dash import dcc, html, Dash, Output, Input
from flask import Flask, render_template, make_response

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server

def export_to_pdfs():
    pdfkit.from_url('http://192.168.1.6:8056/', 'out.pdf')
    # rendered = render_template("index.html")
    # pdf = pdfkit.from_string(rendered, False)
    # response = make_response(pdf)
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

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
        ),
        html.Button("Export to PDF", id="export-button", n_clicks=0),
        html.Div(id='container-button-timestamp', children='Enter a value and press submit')
    ]
)

@app.callback(
    Output('container-button-timestamp', 'children'),
    Input("export-button", "n_clicks")
    # Input("export-button", "clicks"),
)
def export_to_pdf(n_clicks):
    if n_clicks > 0:
        export_to_pdfs()
        n_clicks = 0
    return n_clicks


if __name__ == '__main__':
    app.run_server(host="192.168.1.6", port=8056, debug=True)