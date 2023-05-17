-- Select the tv_shows.title and tv_show_genres.genre_id columns
-- Join the tv_shows and tv_show_genres tables based on the id and show_id columns
-- Use a LEFT JOIN to include all shows from tv_shows table, even if they don't have a corresponding genre in tv_show_genres table
-- Order the results in ascending order by the tv_shows.title and tv_show_genres.genre_id columns
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

