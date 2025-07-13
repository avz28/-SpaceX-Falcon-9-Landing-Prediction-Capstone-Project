import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX launch data into a pandas DataFrame
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Generate the list of launch site options for the dropdown
site_options = (
    [{'label': 'All Sites', 'value': 'ALL'}] +
    [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()]
)

# Create the Dash application
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Launch Site dropdown
    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),

    html.Br(),

    # TASK 2: Pie chart
    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    html.P("Payload range (Kg):"),

    # TASK 3: Payload range slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),

    # TASK 4: Scatter plot
    dcc.Graph(id='success-payload-scatter-chart'),
])

# TASK 2: Callback to update pie chart based on selected site
@app.callback(Output('success-pie-chart', 'figure'),
              Input('site-dropdown', 'value'))
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Filter for successful launches only
        df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(df, names='Launch Site',
                     title='Total Successful Launches by Site')
    else:
        # Filter for the selected site
        df = spacex_df[spacex_df['Launch Site'] == selected_site]
        fig = px.pie(df, names='class',
                     title=f'Total Success vs Failure for site {selected_site}')
    return fig

# TASK 4: Callback to update scatter plot based on selected site and payload range
@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'),
               Input('payload-slider', 'value')])
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

    title = ('Correlation between Payload and Success for All Sites'
             if selected_site == 'ALL' else
             f'Correlation between Payload and Success for {selected_site}')

    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category',
                     title=title)
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run()

