# Visualización:

### Gráficos de Barras: Para comparar precios o ratings entre diferentes modelos.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


app = Dash(__name__)


fig = px.bar(df, x="Calificación", y="Precio(₹)", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)

### Diagramas de Caja: Para mostrar la distribución de precios y ratings.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Crear la aplicación de Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Distribución de Precios y Ratings'),

    dcc.Tabs(id="tabs", value='tab-precios', children=[
        dcc.Tab(label='Distribución de Precios', value='tab-precios'),
        dcc.Tab(label='Distribución de Ratings', value='tab-ratings'),
    ]),

    html.Div(id='tabs-content')
])

# Callback para actualizar el contenido de las pestañas
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-precios':
        fig = px.box(df, y='Precio(₹)', points="all", title="Distribución de Precios")
        return dcc.Graph(figure=fig)
    elif tab == 'tab-ratings':
        fig = px.box(df, y='Calificación', points="all", title="Distribución de Ratings")
        return dcc.Graph(figure=fig)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)


### Mapas de Calor: Para ver la relación entre diferentes características, como procesador y batería.

# Excluir columnas no numéricas
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Calcular la matriz de correlación
correlation_matrix = numerical_df.corr()

# Convertir la matriz de correlación en una figura de Plotly
fig = px.imshow(correlation_matrix,
                labels=dict(x="Características", y="Características", color="Correlación"),
                x=correlation_matrix.columns,
                y=correlation_matrix.columns,
                color_continuous_scale='RdBu_r',
                zmin=-1, zmax=1)
fig.update_layout(title="Mapa de Calor de Correlaciones entre Características de Teléfonos")

# Crear la aplicación de Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Análisis de Características de Teléfonos'),

    dcc.Graph(
        id='heatmap',
        figure=fig
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)