import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample fitness data (replace with your own data or fetch from database)
fitness_data = {
    "2025-04-01": "Morning Workout",
    "2025-04-03": "Yoga and Stretching",
    "2025-04-10": "Cardio - 30 mins",
    "2025-04-15": "Strength Training",
    "2025-04-20": "Rest Day"
}

# Define the layout of the Dash app
app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
            dbc.NavItem(dbc.NavLink("Calendar", href="/calendar", id='calendar-link', style={"color": "blue"}))
        ],
        brand="Fitness & Health Tracker",
        brand_href="/",
        color="primary",
        dark=True
    ),
    
    # Placeholder for the page content, which will change based on the link
    html.Div(id='page-content'),
])

# Calendar Page Layout
calendar_layout = html.Div([
    html.H2("Fitness Tracker Calendar", style={"textAlign": "center"}),
    dcc.DatePickerRange(
        id="fitness-calendar",
        start_date="2025-04-01",
        end_date="2025-04-30",
        display_format="YYYY-MM-DD",
        minimum_nights=1,
        month_format="MMMM YYYY",
        updatemode='singledate',
    ),
    html.Div(id="calendar-output", style={"textAlign": "center"}),
])

# Callback to change content when the calendar link is clicked
@app.callback(
    Output('page-content', 'children'),
    Input('calendar-link', 'n_clicks')
)
def display_calendar_page(n_clicks):
    if n_clicks:
        return calendar_layout
    return html.Div("Welcome to the Fitness & Health Tracker!")

# Display fitness event data on the selected date
@app.callback(
    Output('calendar-output', 'children'),
    Input('fitness-calendar', 'start_date'),
    Input('fitness-calendar', 'end_date')
)
def update_calendar(start_date, end_date):
    selected_dates = pd.date_range(start_date, end_date).strftime("%Y-%m-%d").tolist()
    events = []
    
    for date in selected_dates:
        if date in fitness_data:
            events.append(f"{date}: {fitness_data[date]}")
    
    if events:
        return html.Div([html.P(event) for event in events])
    return html.P("No fitness events for selected dates.")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
