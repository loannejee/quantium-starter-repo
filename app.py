# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import pandas
from dash import Dash, html, dcc, Input, Output

from plotly.express import line

# the path to the formatted data file
DATA_PATH = "./combined_and_cleaned_model.csv"
# 
COLORS = {
    "primary": "#FFEFF2",
    "secondary": "#ECF9FF",
    "font": "#522A61"
}

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# create the visualization
def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"],
        title_font_size=22,
    )
    return line_chart

visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data) # data from line 19
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "color": COLORS["font"],
        "font-family": "'Arial', Sans-serif",
        "padding-top": "20px"
    }
)

'''
Create radio button to filter sales by region

The first argument are the options: ["north", "east", "south", "west", "all"]. 
The second argument is the value property by default at: "north".
This value of region_picker can change based on your which button you select.

'''
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%",
        "padding-bottom": '20px'
    }
)


# Callback =======================================================================================================
'''
Define the region picker callback

Whenever an input property changes (value of region_picker), the function that the callback decorator wraps will get called automatically. 
Dash provides this callback function with the new value of the input property as its argument, and Dash updates 
the property of the output component with whatever was returned by the function: update_graph(region).

'''
@dash_app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
# The new value of the input property (region) gets passed into the function
def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    # generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# define the app layout ==========================================================================================
dash_app.layout = html.Div(
    [
        header,
        visualization,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
    }
)

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run_server()