-- script that displays the top 3 of cities temperature
SELECT city, temperature
FROM temperature_table
WHERE month IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;

