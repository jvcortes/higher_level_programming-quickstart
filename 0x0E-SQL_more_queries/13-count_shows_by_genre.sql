-- Lists all the shows that don't have a genre
SELECT tv_genres.name, COUNT(*) as number_of_shows FROM ((tv_genres
	INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id))
	GROUP BY tv_show_genres.genre_id
	ORDER BY number_of_shows DESC;
