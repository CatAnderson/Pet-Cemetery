DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255),
    age INT,
    owner_id INT REFERENCES owners(id)
    );
