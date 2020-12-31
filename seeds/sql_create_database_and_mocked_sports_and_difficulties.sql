--Tables for database and its columns.
CREATE TABLE esport (
	id int NOT NULL AUTO_INCREMENT,
	nom_esport VARCHAR(100),
	PRIMARY KEY (id)
);
CREATE TABLE dificultat (
	id int NOT NULL AUTO_INCREMENT,
	dificultat VARCHAR(30),
	PRIMARY KEY (id)
);

CREATE TABLE esport_log (
	id int NOT NULL AUTO_INCREMENT,
	dia_esport TIMESTAMP,
	durada VARCHAR(50),
	esport int,
	dificultat int,
	PRIMARY KEY (id),
	FOREIGN KEY (esport) REFERENCES esport(id),
	FOREIGN KEY (dificultat) REFERENCES dificultat(id)
);

CREATE TABLE recordatori (
	id int NOT NULL AUTO_INCREMENT,
	dia TIMESTAMP,
	esport int,
	PRIMARY KEY (id),
	FOREIGN KEY (esport) REFERENCES esport(id)
);

--Inserts for database. Names are in Catalan but you can put other values.

INSERT INTO esport (nom_esport) VALUES ('Natacio');
INSERT INTO esport (nom_esport) VALUES ('Caminar');
INSERT INTO dificultat (dificultat) VALUES ('Molt facil');
INSERT INTO dificultat (dificultat) VALUES ('Facil');
INSERT INTO dificultat (dificultat) VALUES ('Mitja');
INSERT INTO dificultat (dificultat) VALUES ('Mitja alt');
INSERT INTO dificultat (dificultat) VALUES ('Dificil');
INSERT INTO dificultat (dificultat) VALUES ('Extremadament dificil');
