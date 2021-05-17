CREATE TABLE IF NOT EXISTS people
(id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(30) NOT NULL,
lastname VARCHAR(50) NOT NULL);

CREATE TABLE IF NOT EXISTS temperature
(id SERIAL NOT NULL PRIMARY KEY,
temperature SMALLINT NOT NULL,
datatime BIGINT NOT NULL);

CREATE TABLE IF NOT EXISTS photos
(id SERIAL NOT NULL PRIMARY KEY,
user_id INT NOT NULL,
photo TEXT NOT NULL);