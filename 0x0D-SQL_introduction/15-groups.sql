-- Shows the count for every score in 'second_table'
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY score DESC
