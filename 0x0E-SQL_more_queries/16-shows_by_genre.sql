-- List shows and genres linked to the show DB
-- order by ascending show title and genre name.
SELECT `title`, `name`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s
ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS g
ON s.`genre_id` = g.`id`
ORDER BY `title`, `name`;
 
