-- Shows the max temperature of each state, ordered by the state name.
SELECT state, max(value) as max_temp FROM temperatures
	GROUP BY state
	ORDER BY state ASC;
