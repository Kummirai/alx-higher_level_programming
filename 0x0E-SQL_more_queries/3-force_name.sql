-- This script creates the table force_name
-- force_name values: id INT, name VARCHAR(256)
-- If force_name already exists, no error will occur
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);