-- Select the genre column and count the number of shows for each genre
-- Specify the table name
-- Group the results by genre
-- Filter out genres that don't have any shows linked
-- Sort the results in descending order by the number of shows linked

SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;
