# TP_webapp_python

Ce projet est un TP d'intégration continue en s'appuyant sur le déploiement d'une webapp python


## Prérequis

Pour exécuter ce projet, vous aurez besoin de :

- Un ordinateur exécutant une distribution de Linux ou de macOS
- Un interpréteur Python 3.x installé sur votre ordinateur
- Un gestionnaire de paquets Python (pip) installé sur votre ordinateur


## Installation

1. Clonez ce dépôt Git sur votre ordinateur en utilisant la commande suivante :
```git clone https://github.com/Lavinash/TP_webapp_python.git```

2. Accédez au répertoire du projet :
``cd TP_webapp_python``

3. Installez les dépendances du projet en utilisant la commande suivante :
```pip install -r requirements.txt```


## Exécution

Pour lancer l'application, utilisez la commande suivante à partir du répertoire du projet :
```python main.py```

L'application devrait maintenant être disponible à l'adresse http://localhost:5000/

## Fonctionnalités

Notre application se sert d'une API, plus précisement la Bored API.

Elle permet de trouver soit : 
  - une activité aléatoire à réaliser seul;
  - une activité de groupe en fonction du nombre de participants.
Sur la page web on peut voir deux boutons permettant de faire le choix entre ces deux options.

## Fonctionnement

Pour build notre application il faut suivre les étapes de la partie : ## Installation.
Les phases de test de l'application sont directement incluses dans le code et sont faites avant de donner un résultat.
Si l'on souhaite lancer l'application localement il faut suivre les étapes precedentes jusqu'à l'execution, l'application arrive donc à l'adresse http://localhost:5000/

## Intégration continue

Notre tp traite les aspects CICD de notre application en se basant sur le process suivant : 
  - build image docker intégrant notre application
  - push cette image automatiquement dès mises jours

Vous pouvez retrouver un Dokerfile ready to use ainsi qu'un workflow GithubActions pour la partie CICD





