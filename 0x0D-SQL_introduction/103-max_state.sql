-- Shows the max temperature of each state, ordered by the state name.
SELECT state, max(value) as max_value FROM temperatures
	GROUP BY state
	ORDER BY state ASC;
