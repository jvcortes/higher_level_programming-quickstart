-- Creates a database 'hbtn_0d_usa'
-- Creates a table 'states' inside 'hbtn_0d_usa' with the following properties:
-- id, INT, auto generated, not null, primary key
-- name, VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

