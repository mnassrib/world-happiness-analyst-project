-- Création de la table finale world_happiness
CREATE TABLE IF NOT EXISTS world_happiness (
    country VARCHAR(100),
    year INT,
    life_ladder FLOAT,
    log_gdp_per_capita FLOAT,
    social_support FLOAT,
    healthy_life_expectancy_at_birth FLOAT,
    freedom_to_make_life_choices FLOAT,
    generosity FLOAT,
    perceptions_of_corruption FLOAT,
    positive_affect FLOAT,
    negative_affect FLOAT
);

-- Création de la table temporaire pour l'importation
CREATE TEMP TABLE world_happiness_temp (
    "Country name" VARCHAR(100),
    "year" INT,
    "Life Ladder" FLOAT,
    "Log GDP per capita" FLOAT,
    "Social support" FLOAT,
    "Healthy life expectancy at birth" FLOAT,
    "Freedom to make life choices" FLOAT,
    "Generosity" FLOAT,
    "Perceptions of corruption" FLOAT,
    "Positive affect" FLOAT,
    "Negative affect" FLOAT
);

-- Importation des données depuis le fichier CSV dans la table temporaire
COPY world_happiness_temp(
    "Country name",
    "year",
    "Life Ladder",
    "Log GDP per capita",
    "Social support",
    "Healthy life expectancy at birth",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption",
    "Positive affect",
    "Negative affect"
)
FROM '/data/world-happiness-report-2024.csv' 
DELIMITER ',' 
CSV HEADER
ENCODING 'UTF-8';

-- Insertion des données de la table temporaire dans la table finale
INSERT INTO world_happiness(
    country,
    year,
    life_ladder,
    log_gdp_per_capita,
    social_support,
    healthy_life_expectancy_at_birth,
    freedom_to_make_life_choices,
    generosity,
    perceptions_of_corruption,
    positive_affect,
    negative_affect
)
SELECT
    "Country name",
    "year",
    "Life Ladder",
    "Log GDP per capita",
    "Social support",
    "Healthy life expectancy at birth",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption",
    "Positive affect",
    "Negative affect"
FROM world_happiness_temp;

-- Suppression de la table temporaire
DROP TABLE world_happiness_temp;
