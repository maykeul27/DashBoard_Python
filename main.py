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

@app.callback(
    [Output(component_id='année_sélectionnée', component_property='children'),
     Output(component_id='carte_traffic', component_property='figure'),
     Output(component_id='histogramme_traffic', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def maj_interface(année_choisie):

    # Création de 'affichage de 'année séléctionnée
    container = "L'année sélectionnée est: {}".format(année_choisie)
    
    # df['text'] = ''

    # if année_choisie == 2018:
    #     df['text'] = 'Station' + df['Nom_Station'] + '<br>Ligne(s): ' + str(df['correspondance_1']) + ', ' + str(df['correspondance_2']) + ', ' + str(df['correspondance_3']) + ', ' + str(df['correspondance_4']) + ', ' + str(df['correspondance_5']) + '<br>Traffic année ' + '2018: ' + str(df['trafic_2018'])
    # elif année_choisie == 2019:
    #     df['text'] = 'Station' + df['Nom_Station'] + '<br>Ligne(s): ' + str(df['correspondance_1']) + ', ' + str(df['correspondance_2']) + ', ' + str(df['correspondance_3']) + ', ' + str(df['correspondance_4']) + ', ' + str(df['correspondance_5']) + '<br>Traffic année ' + '2019: ' + str(df['trafic_2019'])
    # else:
    #     df['text'] = 'Station' + df['Nom_Station'] + '<br>Ligne(s): ' + str(df['correspondance_1']) + ', ' + str(df['correspondance_2']) + ', ' + str(df['correspondance_3']) + ', ' + str(df['correspondance_4']) + ', ' + str(df['correspondance_5']) + '<br>Traffic année ' + '2020: ' + str(df['trafic_2020'])
    
    limits = [(0,15000),(15001,400000),(750001,15000000),(15000001,30000000),(30000001,5000000)]
    colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
    scale = 8500

    fig = go.Figure()
    
    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        #print(df['Nom_Station'] + str(df['correspondance_1']) + str(df['correspondance_2']) + str(df['correspondance_3']) + str(df['correspondance_4']) + str(df['correspondance_5']) + str(df_sub['trafic_2018']))
        #print(df['Nom_Station'][i] + str(df['correspondance_1'][i]) + str(df['correspondance_2'][i]) + str(df['correspondance_3'][i]) + str(df['correspondance_4'][i]) + str(df['correspondance_5'][i]) + str(df_sub['trafic_2018'][i]))
        #fig = go.Figure(data = go.Scattergeo(
        # if année_choisie == 2018:
        #     df['text'] = 'Station' + df_sub['Nom_Station'] + '<br>Ligne(s): ' + str(df_sub['correspondance_1']) + ', ' + str(df_sub['correspondance_2']) + ', ' + str(df_sub['correspondance_3']) + ', ' + str(df_sub['correspondance_4']) + ', ' + str(df_sub['correspondance_5']) + '<br>Traffic année ' + '2018: ' + str(df_sub['trafic_2018'])
        # elif année_choisie == 2019:
        #     df['text'] = 'Station' + df_sub['Nom_Station'] + '<br>Ligne(s): ' + str(df_sub['correspondance_1']) + ', ' + str(df_sub['correspondance_2']) + ', ' + str(df_sub['correspondance_3']) + ', ' + str(df_sub['correspondance_4']) + ', ' + str(df_sub['correspondance_5']) + '<br>Traffic année ' + '2019: ' + str(df_sub['trafic_2019'])
        # else:
        #     df['text'] = 'Station' + df_sub['Nom_Station'] + '<br>Ligne(s): ' + str(df_sub['correspondance_1']) + ', ' + str(df_sub['correspondance_2']) + ', ' + str(df_sub['correspondance_3']) + ', ' + str(df_sub['correspondance_4']) + ', ' + str(df_sub['correspondance_5']) + '<br>Traffic année ' + '2020: ' + str(df_sub['trafic_2020'])

        fig.add_trace(go.Scattergeo(
            locationmode = 'ISO-3',
            lon = df_sub['Longitude'],
            lat = df_sub['Latitude'],
            #text ='Station' + df_sub['Nom_Station'] + '<br>Ligne(s): ' + str(df_sub['correspondance_1']) + ', ' + str(df_sub['correspondance_2']) + ', ' + str(df_sub['correspondance_3']) + ', ' + str(df_sub['correspondance_4']) + ', ' + str(df_sub['correspondance_5']) + '<br>Traffic année ' + str(année_choisie) + ': ' + str(df_sub['trafic_'+ str(année_choisie)]), # df_sub['text'],
            hoverlabel = 'Nom_Station',
            marker = dict(
                size = df_sub['trafic_' + str(année_choisie)]/scale,
                color = colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1]))).update_geos(projection_type="satellite")

    fig.update_layout(
        title_text = 'Traffic Réseau Transport ' + str(année_choisie),
        showlegend = True,
        geo = dict(
             showland = True,
            # Add coordinates limits on a map
            lataxis = dict(range=[48.5,49.2]),
            lonaxis = dict(range=[2,2.9]),
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        )
    )

    figH = go.Figure()

    figH.show()

    return container, fig, figH


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
