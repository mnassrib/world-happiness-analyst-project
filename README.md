# World Happiness Analyst Project

## Introduction
Ce projet utilise des données du "[World Happiness Report 2024](https://worldhappiness.report/data/)" pour analyser et visualiser divers indicateurs de bonheur par pays et par année.

## Structure du Projet
- `data/`: contient le jeu de données.
- `api/`: contient l'API Flask.
- `visualization/`: contient l'application Streamlit.
- `database/`: contient le script SQL d'initialisation.
- `docker-compose.yml`: fichier de configuration pour Docker Compose.
- `.env` : stocke toutes les variables d'environnement pour la configuration de la base de données.
- `README.md` : contient les instructions sur la configuration et l'utilisation du projet.

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
