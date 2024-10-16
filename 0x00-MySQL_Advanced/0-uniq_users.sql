-- This SQL script creates a table users with the following attributes:
-- id(integer, never null, auto increment, primary key)
-- email(string(255 characters), never null and unique)
-- name(255 characters)

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);