-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Results must be sorted in descending order by their rating
SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_shows` AS tv
INNER JOIN `tv_show_ratings` AS ra
ON tv.`id` = ra.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
