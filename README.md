# Equipe:
Michael TRAN <br>
Thomas MEONI

# Nom du fichier CSV:
trafic-annuel-entrant-par-station-du-reseau-ferre 2018-2020

# Description :
Nous avons choisi de traiter les taux de fréquentation des stations ratp, métro et sncf en île de France. 
Il comprend donc les lignes de RER, Metros, TGV et trains de lignes.

Les données ont été récupérées sur 3 fichiers csv provenant du site du gouvernement.
Voici les liens :
1) https://www.data.gouv.fr/fr/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2018/
2) https://www.data.gouv.fr/fr/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2019/
3) https://www.data.gouv.fr/fr/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2020/

Ensuite nous les avons triées, fusionnées dans un seul fichier csv afin de traiter toutes ces données sans avoir à ouvrir plusieurs csv en même temps (performance réduite).

# Problématique :
Quelles ont été les répercussions de la crise Covid-19 sur le réseau de la RATP?

# Conclusion :
Nous pouvons constater avec ces données que depuis le début de la période Covid-19 (commencé en fin 2018), le taux de fréquentation
des transports en communs a commencé à drastiquement chuter d'année en année.

Suite au confinement et aux mesures sanitaires obligatoires mis en place par le gouvernement, l'utilisation des transports en communs et des trains a baissé. 
à cela, deux raisons : Soit parce que les français utilisaient leurs voitures ou d'autres moyens de transports alternatif, soit parce que la mise en place du télétravail à une baisse
des déplacements.

Au plus fort de la crise de la Covid en 2020.
Les taux de fréquentation des stations d'île-de-France ont chutés de presque 50% par rapport à 2018.

# Installation :
- Il y plusieurs façon d'accèder à ce dashboard :
1) cloner le dépôt git avec la commande ci-dessous dans un terminal :
$ git clone https://github.com/maykeul27/DashBoard_Python

2) télécharger le dossier du dashboard via le lien ci-dessus.

Ensuite il faut installer les packages nécessaires pour le bon fonctionnement du dashboard :
% plotly.graph_objects, plotly.express, pandas, pathlib et dash.
(voir le fichier texte requirements.txt)

Et pour finir utilisez cette commande dans un terminal afin d'installer les bons packages avec les bonne versions.
$ python -m pip install -r requirements.txt

# Démarrage :
Executer sur votre terminal python le main.py.
# Instructions à exécuter dans le terminal pour lancer le projet :
Une fois que vous avez exécuter le main.py, une adresse ip 127.0.0.1 (adresse local de la machine) apparaîtra. 
Il faudra faire un click ou ctrl+click dessus afin d'ouvrir le dashboard sur votre navigateur web.

# Utilisation: 
En haut à droite vous pourrez sélectionner l'année désirée dont vous souhaitez afficher le trafic.
Cette sélection changera les données affichées sur la carte. En-dessous vous trouverez un diagramme
récapitulatif sur le taux de fréquentation total annuel de toutes les stations en île-de-France.