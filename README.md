# Equipe:
Michael TRAN
Thomas MEONI

# Nom du fichier CSV:
trafic-annuel-entrant-par-station-du-reseau-ferre 2018-2020

# Description :
Taux de fréquentation des station ratp île de France. Comprend les RER, metro, TGV et train # de ligne

# Installation :
$ git clone https://github.com/maykeul27/DashBoard_Python

% Liste des packages additionnels: plotly.graph_objects, plotly.express, pandas, pathlib and dash, voir requirements.txt

$ python -m pip install -r requirements.txt

# Démarrage
 lancer sur votre terminal python le main.py

# Instruction à exécuter dans le terminal pour lancer le projet.
Utilisation: ouvrez l'url affiché
Puis cliquez sur le bouton de defilement et choisir une année.

# Architecture
Mermaid (diagramme)
https://mermaid-js.github.io/mermaid-live-editor/edit
graph TD
    A[import] -->|plotly.graph_objects & express, pandas, pathlib| B(main.py)
    B --> C
    C[import data] --> |callback : interagit avec l'interface|D{app.callback}
    C --> |trafic-annuel-entrant-par-station-du-reseau-ferre-2018-2020.csv|C1(csv est à part, il correspond à notre database et il est interprété par panda)
    D --> |contient les données du csv nécessaire à la lecture| E[def maj_interface:]
    D --> D1(C'est le lien entre le csv et l'interface)
    D --> E1{children} --> E11(année selectionnée)
    D --> E2{figure} --> E21(carte traffic)
        E2{figure} --> E22(histogramme_traffic)
    D --> E4{value} --> E41(select_year)
    E --> F{fig}
    E--> E3(def maj_interface prend: selected_year)
    E --> E5{container} --> E51[container = l'année  sélectionnée est :] --> E511(année_choisie correspondant à selected_year de l'interface)
    E --> |malheureusement non implétementé|J{figH} --> J1(figH : permettrais de dessiner un histogramme par rapport à la densité de fréquentation par station)
    F --> F1(.add_trace)
    F1 --> F11("Trace les lignes entre les stations")
    F --> F2(.update_layout)
    F2 --> F21("Met à jour l'affichage à chaque changement d'années")
    F --> |Description de fig|F3(dessine une carte en interprétant certaines données csv en fonction de l'année choisi par l'utilisateur sur l'interface)
    F --> G{return container, fig, figH}
    G --> G1(retourne : l'année selectionnée, la carte traffic, l'histogramme trafique)
    F --> H(figH : c'est le display final. Il va afficher les figures tracées avec :)
    H --> H1(figH = go.Figure)
    C --> I{app.layout}
    I --> |html.Div| I1(il s'agit de l'interface html)
    I1 --> I11[Titre : Traffic ratp par année]
    I1 --> I12[Sélection de l'année : slct_year]
        I12 --> I121{2018}
        I12 --> I122{2019}
        I12 --> I123{2020}
        I12 --> I124(default : 2018)
    I1 --> I13[Affichage de l'année sélectionnée : année_sélectionnée]
    I1 --> |C'est un Graph|I14[Carte correspondant à l'année : carte_traffic]
    I1 --> |C'est une figure|I15[Histogramme : histogramme_traffic]