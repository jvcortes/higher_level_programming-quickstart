-- Lists the shows whose genre is not 'Comedy'
SELECT tv_shows.title FROM ((tv_genres
	RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id)
	RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id)
	WHERE tv_shows.title NOT IN 
		(SELECT tv_shows.title FROM ((tv_genres
                        INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id)
                  	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id)
                        WHERE tv_genres.name = 'Comedy')
	GROUP BY tv_shows.title
	ORDER BY tv_shows.title ASC;
