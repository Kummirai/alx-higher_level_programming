-- This script creates the table unique_id with values id INT (default 1, unique) & name VARCHAR(256)
-- If the table exists, no error will occur
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);