# World Happiness Analyst Project

Ce projet décrit l'orchestration de plusieurs services conteneurisés pour une application. Il utilise des données du "[World Happiness Report 2024](https://worldhappiness.report/data/)" pour analyser et visualiser divers indicateurs de bonheur par pays et par année.

## Objectif
L'objectif est de définir et de gérer une stack de services Docker nécessaires pour une application qui doit inclure une base de données PostgreSQL, une interface d'administration pour PostgreSQL, une API Flask, et une application de visualisation Streamlit. Ces services sont configurés pour fonctionner ensemble de manière coordonnée.

## Structure du projet

```
world-happiness-analyst-project/
├── api/
│   ├── app.py
│   ├── Dockerfile
│   ├── config.py
│   └── requirements.txt
├── data/
│   └── world-happiness-report-2024.csv
├── database/
│   └── init.sql
├── visualization/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── .env
└── README.md
```

- `data/`: contient le jeu de données.
- `api/`: contient l'API Flask.
- `visualization/`: contient l'application Streamlit.
- `database/`: contient le script SQL d'initialisation.
- `docker-compose.yml`: fichier de configuration pour Docker Compose.
- `.env` : stocke toutes les variables d'environnement pour la configuration de la base de données.
- `README.md` : contient les instructions sur la configuration et l'utilisation du projet.

## Structure des services

1. **Service `db` (PostgreSQL)**
   - **Image**: Utilise l'image `postgres:13`.
   - **Nom du conteneur**: `postgres_db`.
   - **Variables d'environnement**: Définit les utilisateurs, mots de passe et nom de la base de données via des variables d'environnement.
   - **Volumes**: Monte deux fichiers locaux dans le conteneur :
     - `world-happiness-report-2024.csv` pour les données.
     - `init.sql` pour initialiser la base de données.
   - **Ports**: Expose le port `5432` pour accéder à PostgreSQL depuis l'extérieur.

2. **Service `pgadmin` (PgAdmin4)**
   - **Image**: Utilise l'image `dpage/pgadmin4`.
   - **Nom du conteneur**: `pgadmin`.
   - **Variables d'environnement**: Définit l'email et le mot de passe par défaut pour PgAdmin via des variables d'environnement.
   - **Ports**: Expose le port `5050` pour accéder à PgAdmin via le navigateur.
   - **Dépendance**: Dépend du service `db`, donc il ne démarre qu'après `db`.

3. **Service `api` (Flask API)**
   - **Construction**: Utilise le répertoire `./api` pour construire l'image Docker de l'API Flask.
   - **Nom du conteneur**: `flask_api`.
   - **Variables d'environnement**: Passe les détails de connexion à la base de données via des variables d'environnement.
   - **Ports**: Expose le port `5000` pour l'API Flask.
   - **Dépendance**: Dépend du service `db`, donc il ne démarre qu'après `db`.

4. **Service `visualization` (Streamlit)**
   - **Construction**: Utilise le répertoire `./visualization` pour construire l'image Docker de l'application Streamlit.
   - **Nom du conteneur**: `streamlit_app`.
   - **Ports**: Expose le port `8501` pour l'application Streamlit.
   - **Dépendance**: Dépend du service `api`, donc il ne démarre qu'après `api`.

En résumé le fichier `docker-compose.yml` configure une application composée de quatre services :

- Un serveur PostgreSQL pour la base de données.
- PgAdmin pour la gestion de PostgreSQL.
- Une API Flask pour la logique backend.
- Une application Streamlit pour la visualisation des données.

Ces services sont orchestrés de manière à démarrer dans l'ordre nécessaire pour garantir que chaque service dépendant des autres est disponible avant de démarrer.

## Instructions

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/mnassrib/world-happiness-analyst-project.git
    cd world-happiness-analyst-project
    ```

2. Exécutez `docker-compose up --build` pour lancer tous les services.
3. Accédez à :
    - PgAdmin à l'adresse http://localhost:5050 
    - API Flask à http://localhost:5000/happiness
    - Application Streamlit à http://localhost:8501

## Note

---

Le jeu de données `world-happiness-report-2024.csv` placé dans le dossier `data/` n'est autre que celui de [`DataForTable2.1.xls`](https://happiness-report.s3.amazonaws.com/2024/DataForTable2.1.xls) converti en csv. 

---

- **Connexion à pgAdmin :**
    - **Email** : Utilisez l'adresse email que vous avez spécifiée pour pgAdmin dans le fichier `.env`.
    - **Mot de passe** : Utilisez le mot de passe que vous avez spécifié pour pgAdmin dans le fichier `.env`.

- **Enregistrez un nouveau serveur :**
    - Faites un clic droit sur "Servers" > "Register" > "Server..."

- **Configurez le serveur :**
    - **Onglet "General" :**
        - **Name** : Entrez un nom pour le serveur, par exemple : `PostgreSQL`.
    - **Onglet "Connection" :**
        - **Host name/address** : Utilisez le nom du service Docker PostgreSQL défini dans le fichier `docker-compose.yml`. Par exemple, `db` si votre service PostgreSQL est nommé `db`.
        - **Port** : 5432
        - **Maintenance database** : Utilisez le nom de la base de données que vous avez spécifié dans le fichier `.env`.
        - **Username** : Utilisez le nom d'utilisateur que vous avez spécifié dans le fichier `.env`.
        - **Password** : Utilisez le mot de passe que vous avez spécifié dans le fichier `.env`.
        - **Save password?** : Cochez cette case pour enregistrer le mot de passe.

- **Enregistrez les paramètres :**
    - Cliquez sur "Save".

---

### Exemple de fichier `.env`

Pour référence, voici un exemple de fichier `.env` contenant les variables nécessaires :

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=happiness

PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin

DB_HOST=db  
DB_PORT=5432
DB_NAME=happiness
DB_USER=postgres
DB_PASS=postgres
```
---
