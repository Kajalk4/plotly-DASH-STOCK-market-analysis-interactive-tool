import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import os
import pandas as pd

path = r"D:\Training\kajal\20200711"
l = [os.path.join(path, f) for f in os.listdir(path)]
# File=[os.path.join(l,s)for s in os.listdir()]
l1=[ f for f in os.listdir(path)]
for s in l:
    symbols = [f.replace(".csv", "") for f in os.listdir(s)]

app = dash.Dash(__name__)
app.layout = html.Div(
	children=[
        html.H1("SYMBOL_GRAPH"),
        dcc.Dropdown(id="Date_dropdown",
		             options=[{"label": val, "value": val} for val in l1],
		             value=l1[0],
		             style={
			             "margin": "10px"
		             }),
		dcc.Dropdown(id="symbol_dropdown",
					options=[{"label": val, "value": val} for val in symbols],
		             value=symbols[0],
		             style={
			             "margin": "10px"
		             }),
        html.H1("Graph"),
		dcc.Graph(id='symbol_graph'),

	]
)

# @app.callback(Output(component_id='symbol_dropdown', component_property='options'),
#               [Input('Date_dropdown', 'value')]
#               )


@app.callback(Output(component_id='symbol_graph',component_property='figure'),
			   [Input('Date_dropdown', 'value'),
   				Input('symbol_dropdown', 'value')])

def update_Symbol_graph(Date,symbol):
	for Date in l:
		df = pd.read_csv(os.path.join(path,Date,symbol+".csv"), index_col=False)
		# fig = px.line(df, x="TimeStamp", y="Close", title=symbol)
	fig = go.Figure(data=go.Ohlc(x=df['TimeStamp'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close']))
	return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=5000)
