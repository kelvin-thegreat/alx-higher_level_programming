-- script that displays the average temperature
SELECT city, AVG(temperature * 9/5 + 32) AS avg_temperature_fahrenheit 
FROM temperature_table 
GROUP BY city 
ORDER BY avg_temperature_fahrenheit DESC;
