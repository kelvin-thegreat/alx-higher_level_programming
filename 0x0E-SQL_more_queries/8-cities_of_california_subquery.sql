-- Select the id and name columns from the cities table
-- Join the cities and states tables based on the state_id and id columns
-- Filter the results to include only cities where the state name is 'California'
-- Order the results in ascending order by the cities.id column
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;

