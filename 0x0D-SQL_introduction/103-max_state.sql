-- script that displays the max temperature of each state
SELECT state, MAX(temperature) AS max_temperature
FROM temperature_table
ORDER BY state;
