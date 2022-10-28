# Lidar_localisation_indoor

Les codes proposés sont séparés en deux parties principales:
 - des codes à exécuter sur la raspberry pi 
 - des codes à exécuter un ordinateur


## Projet IoT
    └── Lidar_localisation_indoor/
        ├── README.md
        │
        ├─ rpi/
        │    ├── LivePlot.py
        │    ├── MQTTexploitV3.py
        │    └── rplidar.py
        │
        ├── pc/
        │    ├── blanc8000.png
        │    ├── DetectionPers.py
        │    ├── mur.png
        │    ├── noir.png
        │    ├── pers.png
        │    └── VF.py
        │
        └── exemples/
            ├── changement de repère.png
            ├── demo2.png
            └── intégration.png

## rpi
    ├─ rpi/
    │    ├── LivePlot.py
    │    ├── MQTTexploitV3.py
    │    └── rplidar.py
Le fichier rplidar.py contient l'ensemble des classes nécessaires au bon fonctionnement du lidar. Il doit être placé dans le même répertoire que le fichier en cours d'éxécution (sinon changer les paths).

Le fichier LivePlot.py permet une fois lancé d'avoir une visualisation en temps réel du résultat des acquisitions. Cette exécution est autonome et ne nécessite pas de connection au serveur / de pc distant.

Le fichier MQTTexploitV3.py permet de communiquer au serveur une acquisition préraitée. Pour visualiser ces données, il est nécessaire d'avoir un autre pc pour récupérer ces acquisition depuis le serveur et de les visualiser.

## pc
    ├── pc/
    │    ├── blanc8000.png
    │    ├── DetectionPers.py
    │    ├── mur.png
    │    ├── noir.png
    │    ├── pers.png
    │    └── VF.py

L'ensemble des fichiers présents dans ce répertoires sont destinés à être exécuter sur un pc. Il est nécessites pour leur bon fonctionnement que la rapsberry soit opérationnelle (avec le fichier MQTTexploitV3.py en cours d'éxecution) et le serveur MQTT accessible. 

Le fichier DetectionPers.py permet de réaliser une démonstration succincte du fonctionnement du système. 

Le fichier VF.py permet de réaliser une démonstration plus complète et visuelle du fonctionnement du système

Les différentes images présentes servent à l'affichage de la carte interactive du fichier VF.py.

## exemples
    └── exemples/
         ├── changement de repère.png
         ├── demo2.png
         └── intégration.png

![logo](https://github.com/AlexandreProthin/Lidar_localisation_indoor/blob/main/codes/exemples/demo2.png)
Illustre le mode d'affichage avec trace.

![changement de repere](https://github.com/AlexandreProthin/Lidar_localisation_indoor/blob/main/codes/exemples/changement%20de%20rep%C3%A8re.png)
Résultat du clustering dans différents espace de représentation.

![plan](https://github.com/AlexandreProthin/Lidar_localisation_indoor/blob/main/codes/exemples/int%C3%A9gration.png)
Repère principal et exemple d'ajout de nouvelles technologies de détection / localisation.