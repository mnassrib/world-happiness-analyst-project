# Data Analyst Project

## Introduction
Ce projet utilise des données du "[World Happiness Report 2024](https://worldhappiness.report/data/)" pour analyser et visualiser divers indicateurs de bonheur par pays et par année.

## Structure du Projet
- `data/`: Contient le jeu de données.
- `api/`: Contient l'API Flask.
- `visualization/`: Contient l'application Streamlit.
- `database/`: Contient le script SQL d'initialisation.
- `docker-compose.yml`: Fichier de configuration pour Docker Compose.

## Instructions

1. Clonez le dépôt.
2. Placez le "[`fichier`](https://happiness-report.s3.amazonaws.com/2024/DataForTable2.1.xls)" après avoir le convertir en csv `world-happiness-report-2024.csv` dans le dossier `data/`.
3. Exécutez `docker-compose up --build` pour lancer tous les services.
4. Accédez à PgAdmin à l'adresse http://localhost:5050, à l'API Flask à http://localhost:5000/happiness, et à l'application Streamlit à http://localhost:8501.
