import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pathlib
from dash import html, dcc, Input, Output, Dash

app = Dash(__name__)

# --- Nos imports des datas de traffic rapt 2018 à 2020 ---

# Ouverture panda du csv
currentPath = str(pathlib.Path(__file__).parent.absolute())
df = pd.read_csv(currentPath + "/trafic-annuel-entrant-par-station-du-reseau-ferre-2018-2020.csv", sep = ';')
df.head()

# --- Notre interface ---

app.layout = html.Div([

    # Titre
    html.H1("Traffic ratp par année", style={'text-align': 'center'}),
    html.Br(),
    html.Br(),

    # Sélection de l'année
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020}],
                 multi=False,
                 value=2018,
                 style={'width': "50%"}
                 ),

    # Affichage de l'année sélectionnée
    html.Div(id='année_sélectionnée', children=[]),
    html.Br(),

    # Carte correspondant à l'année
    dcc.Graph(id='carte_traffic', figure={}),

    # Histogramme
    dcc.Graph(id='histogramme_traffic', figure={})

])

# --- On va faire le lien entre nos données, interfaces et sélection afin de créer un affichage intéractif ---

# Le callback faisant 'l'interface' entre les données qui rentrent et qui sortent
@app.callback(
    [Output(component_id='année_sélectionnée', component_property='children'),
     Output(component_id='carte_traffic', component_property='figure'),
     Output(component_id='histogramme_traffic', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
# La fonction qui va être appelée et qui prend en paramètre l'année choisie par l'utilisateur
def maj_interface(année_choisie):
    '''Prend en paramètre l'année choisie par l'utilisateur (int). 
    Retourne: la phrase qui va confirmer l'année selectionnée (string), la carte du traffic (plotly.express.scatter_mapbox), et l'histogramme du traffic annuel sur 3 ans (plotly.express.bar).'''

    # Création de 'affichage de 'année séléctionnée
    container = "L'année sélectionnée est: {}".format(année_choisie)

    # Création de la carte

    # Nos données qui vont changer selon l'année
    map_color = []
    map_hover_data = []

    if année_choisie == 2018:
        map_color = df['trafic_2018']
        map_hover_data = ['correspondance_1' ,'correspondance_2', 'correspondance_3', 'correspondance_4', 'correspondance_5', 'trafic_2018']
    elif année_choisie == 2019:
        map_color = df['trafic_2019']
        map_hover_data = ['correspondance_1' ,'correspondance_2', 'correspondance_3', 'correspondance_4', 'correspondance_5', 'trafic_2019'] 
    else:
        map_color = df['trafic_2020']
        map_hover_data = ['correspondance_1' ,'correspondance_2', 'correspondance_3', 'correspondance_4', 'correspondance_5', 'trafic_2020']

    # La carte qu'on créer en fonction de nos données et de la demande utilisateur
    fig = px.scatter_mapbox(df,
                        lat = df['Latitude'],
                        lon = df['Longitude'],
                        color = map_color,
                        hover_name = df['Nom_Station'],
                        hover_data = map_hover_data,
                        size = map_color,
                        opacity = .8,
                        zoom = 10,
                        size_max = 20,
                        center= dict(lat = 48.85,
                                    lon = 2.34
                        ),
                        mapbox_style = 'carto-positron',
                        title = "Carte BubbleMap du Traffic RATP"
    )

    # Création de l'histogramme
    figH = px.bar(df,x='annee',y='traffic total',
    color='traffic total',
    title="Évolution du Traffic Annuel")
    figH.update_xaxes(type='category')

    # Les objets crées qu'on renvoie au callback
    return container, fig, figH


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    print('\nCtrl + Click sur le lien ci-dessous pour ouvrir le DashBoard dans votre navigateur:\n')
    app.run_server(debug=True)
