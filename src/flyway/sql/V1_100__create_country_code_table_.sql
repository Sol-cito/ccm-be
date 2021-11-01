create table country_code (
	id int(100) NOT NULL AUTO_INCREMENT,
	country_name varchar(100) NOT NULL,
	alpha2_code varchar(100) NOT NULL,
	alpha3_code varchar(100) NOT NULL,
	numeric_code int(100) NOT NULL,
	PRIMARY KEY (id)
)