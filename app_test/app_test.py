# 1. imports of your dash app
import dash
from dash import html
# 2. give each testcase a tcid, and pass the fixture
# as a function argument, less boilerplate

# MY ATTEMPT:
def test_header(dash_duo):
    # 3. define your app inside the test function
    dash_app = dash.Dash(__name__)
    dash_app.layout = html.Div(id="header")
    # 4. host the app locally in a thread, all dash server configs could be
    # passed after the first app argument
    dash_duo.start_server(dash_app)
    # 5. use wait_for_* if your target element is the result of a callback,
    # keep in mind even the initial rendering can trigger callbacks
    dash_duo.wait_for_text_to_equal("#header", "Pink Morsel Visualizer", timeout=4)
     # 6. use this form if its present is expected at the action point
    assert dash_duo.find_element("#header").text == "Pink Morsel Visualizer"

# ==================================================================================

def test_header_exists(dash_duo):
    dash_app = dash.Dash(__name__)
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_app = dash.Dash(__name__)
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_app = dash.Dash(__name__)
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region_picker", timeout=10)