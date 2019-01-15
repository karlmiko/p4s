
CREATE DATABASE dbParking;

USE dbParking;

CREATE TABLE tbOwner 
(	
	id_Owner INT AUTO_INCREMENT,
	firstName_Owner VARCHAR(30),
	lastName_Owner VARCHAR(30),
	school_Owner VARCHAR(50),
	email_Owner VARCHAR(50), 
	totalSpots_Owner INT,
	totalSpotsAvailable_Owner INT,
	status_Owner VARCHAR (20),
	address_Owner VARCHAR (100),
	comment_Owner VARCHAR (500), 
	
	CONSTRAINT pk_tbOwner PRIMARY KEY (id_Owner)
);

CREATE TABLE tbDriver 
(	
	id_Driver INT AUTO_INCREMENT,
	firstName_Driver VARCHAR(30),
	lastName_Driver VARCHAR(30),
	school_Driver VARCHAR(50),
	email_Driver VARCHAR(50),
	cellphone_Driver VARCHAR(20),
	area_Driver VARCHAR(50),
	fieldStudy_Driver VARCHAR(100),
	status_Driver VARCHAR (20),
	carModel_Driver VARCHAR (50),
	carColor_Driver VARCHAR (20),
	
	CONSTRAINT pk_tbDriver PRIMARY KEY (id_Driver)
);

CREATE TABLE tbRider
(	
	id_Rider INT AUTO_INCREMENT,
	firstName_Rider VARCHAR(30),
	lastName_Rider VARCHAR(30),
	school_Rider VARCHAR(50),
	email_Rider VARCHAR(50),
	
	CONSTRAINT pk_tbRider PRIMARY KEY (id_Rider)
);

CREATE TABLE tbRent 
(	
	id_Rent INT AUTO_INCREMENT,
	id_Owner INT,
	id_Driver INT,
	status_Rent VARCHAR(20),
	from_Rent VARCHAR(15),
	to_Rent VARCHAR(15),
	price_Rent FLOAT,
	paymentStatus_Rent VARCHAR(30),
	
	CONSTRAINT pk_tbRent PRIMARY KEY (id_Rent),
	CONSTRAINT fk_tbRenttbOwner FOREIGN KEY (id_Owner) REFERENCES tbOwner (id_Owner),
	CONSTRAINT fk_tbRenttbDriver FOREIGN KEY (id_Driver) REFERENCES tbDriver (id_Driver)
);