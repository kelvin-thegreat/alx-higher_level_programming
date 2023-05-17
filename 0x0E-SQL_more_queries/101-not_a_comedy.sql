-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
SELECT DISTINCT t.title
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s ON s.show_id = t.id
LEFT JOIN tv_genres AS g ON g.id = s.genre_id
WHERE g.name != 'Comedy' OR g.name IS NULL
ORDER BY t.title;
-- Records are ordered by ascending show title.
