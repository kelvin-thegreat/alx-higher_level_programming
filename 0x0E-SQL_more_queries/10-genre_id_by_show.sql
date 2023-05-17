-- Select the tv_shows.title and tv_show_genres.genre_id columns
-- Join the tv_shows and tv_show_genres tables based on the id and show_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
