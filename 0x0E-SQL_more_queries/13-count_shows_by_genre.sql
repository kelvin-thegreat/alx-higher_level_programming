-- Select the genre column and count the number of shows for each genre
-- Specify the table name
-- Group the results by genre
-- Filter out genres that don't have any shows linked
-- Sort the results in descending order by the number of shows linked
SELECT gen.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS tvs
       ON gen.`id` = tvs.`genre_id`
 GROUP BY gen.`name`
 ORDER BY `number_of_shows` DESC;
