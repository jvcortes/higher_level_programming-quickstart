-- Selects all the cities that are in the state of California
SELECT id, name FROM cities
	WHERE state_id
	IN (SELECT id FROM states
		WHERE name = "California")
	ORDER BY cities.id ASC;
