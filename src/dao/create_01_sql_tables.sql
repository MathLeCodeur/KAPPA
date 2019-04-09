CREATE TABLE IMAGE(
	id_image INT PRIMARY KEY NOT NULL,
	comment VARCHAR(255),
	creation_date date,
	length int,
	width int,
	size int,
	path VARCHAR(255)
);


CREATE TABLE VECTOR(
	id_vector INT PRIMARY KEY NOT NULL,
	value_vector VARCHAR NOT NULL
);

CREATE TABLE OBJECT_VECTOR(
	id_vector INT NOT NULL,
	id_parent INT,
	FOREIGN KEY (id_vector) REFERENCES OBJECT_VECTOR(id_vector)
	FOREIGN KEY (id_vector) REFERENCES VECTOR(id_vector)
);

CREATE TABLE FACE_VECTOR(
	id_vector INT NOT NULL,
	IsKnown int NOT NULL,
	FOREIGN KEY (id_vector) REFERENCES VECTOR(id_vector)
);

CREATE TABLE INCLUDE(
	id_vector INT NOT NULL,
	id_image INT NOT NULL,
	FOREIGN KEY (id_vector) REFERENCES VECTOR(id_vector),
	FOREIGN KEY (id_image) REFERENCES IMAGE(id_image)
);


