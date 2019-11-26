-- Creates a table 'second_table' in the current database.
-- The table contains:
-- id, INT field. name, VARCHAR(256) field and score, INT field.
-- The script will add four initial rows to the table.
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Adds the four initial rows to 'second_table'
INSERT INTO second_table (id, name, score)
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
