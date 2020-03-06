import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
	html.H1('Dash Tutorials'),
	dcc.Graph(id='example',
		figure={
		'data' : [{'x':[11,22,33,44,55],'y':[55,66,77,22,11],'type':'bar','name':'boats'},
				 {'x':[10,20,30,40,50],'y':[50,60,70,20,10],'type':'line','name':'cars'},
				 ],
				 'layout':{'title':'Basic Dash Example'}
		})
	])

app.layout = html.Div(children=[
	dcc.Input(id='input',value='Enter Something',type='text'),
	html.Div(id='output')
	])


@app.callback(
	Output(component_id='output',component_property='children'),
	[Input(component_id='input',component_property='value')])

def update_value(input_data):
	try:
		return str(float(input_data)**2)
	except:
		return "Some Error"


if __name__ == '__main__':
	app.run_server(debug=True)