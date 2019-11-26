-- Lists all the cities alongside their respective states.
SELECT cities.id, cities.name, states.name FROM ((cities 
	INNER JOIN states on cities.state_id = states.id));
