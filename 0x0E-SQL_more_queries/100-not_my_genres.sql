-- Lists all genres of hbtn_0d_tvshows
-- show Dexter.
-- sort by ascending genre name.

SELECT DISTINCT genres.name
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS s ON genres.id = s.genre_id
INNER JOIN tv_shows AS tvs ON s.show_id = tvs.id
WHERE genres.name NOT IN (
    SELECT genres.name
    FROM tv_genres AS genres
    INNER JOIN tv_show_genres AS s ON genres.id = s.genre_id
    INNER JOIN tv_shows AS tvs ON s.show_id = tvs.id
    WHERE tvs.title = 'Dexter'
)
ORDER BY genres.name;

