import dash


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'https://fonts.googleapis.com/css?family=Roboto']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True



