-- Creates a table 'unique_id' with the following properties:
-- id, INT, unique with 1 as its default value.
-- name, VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
