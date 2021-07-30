import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
    __name__, external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)


def get_img_path_list():
    m3u8_list = []
    for root, dirs_, files_ in os.walk('./static/data'):
        for file_ in files_:
            if os.path.splitext(file_)[-1] == '.m3u8':
                m3u8_list.append(os.path.join(root, file_).replace('\\', '/'))
    m3u8_list.sort(key=lambda x: os.path.basename(x))
    print(m3u8_list)
    return m3u8_list


app.layout = html.Div([
    html.Div(
        html.A("==> Player <==", href='./static/plyr_player.html', target='_blank'),
        style={'margin': '30px auto'}
    ),
    html.Div(
        html.Ul([], id='ul1')
    )
])


@app.callback(
    dash.dependencies.Output('nl1', 'children'),
    dash.dependencies.Input('ul1', 'n_clicks')
)
def refresh_m3u8_list(n_clicks):
    return [html.Li(html.A(os.path.basename(i), href=i)) for i in get_img_path_list()]


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=12345, debug=False)
