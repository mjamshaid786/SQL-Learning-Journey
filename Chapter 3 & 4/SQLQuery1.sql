/* Create table persons with column name
id, person_name, dob, phone*/

CREATE TABLE persons (
	id INT NOT NULL,
	person_name VARCHAR(50) NOT NULL,
	dob DATE,
	phone VARCHAR(15) NOT NULL,
	CONSTRAINT pk_perons PRIMARY KEY (id)
)