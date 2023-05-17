-- Select the cities.id, cities.name, and states.name columns
-- Join the cities and states tables based on the state_id and id columns
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
