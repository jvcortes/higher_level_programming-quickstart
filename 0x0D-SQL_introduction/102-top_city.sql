-- Shows the top three cities with the highest average temperature between July and August.
SELECT city, AVG(value) as avg_temp
	FROM temperatures
	WHERE month >= 7 and month <= 8
	GROUP BY city
	ORDER BY AVG(value) DESC
	LIMIT 3;
