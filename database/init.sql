CREATE TABLE world_happiness (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100),
    year INT,
    happiness_score FLOAT,
    economy_gdp_per_capita FLOAT,
    social_support FLOAT,
    healthy_life_expectancy FLOAT,
    freedom_to_make_life_choices FLOAT,
    generosity FLOAT,
    perceptions_of_corruption FLOAT
);

COPY world_happiness(country, year, happiness_score, economy_gdp_per_capita, social_support, healthy_life_expectancy, freedom_to_make_life_choices, generosity, perceptions_of_corruption)
FROM '/docker-entrypoint-initdb.d/world-happiness-report.csv' DELIMITER ',' CSV HEADER;
