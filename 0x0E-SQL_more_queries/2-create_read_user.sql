-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user with the SELECT privilege in the database if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user only for the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;
