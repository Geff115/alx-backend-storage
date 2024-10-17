-- This SQL script creates an index idx_name_first on the
-- table names and the first letter of name

ALTER TABLE names 
ADD COLUMN first_letter CHAR(1) GENERATED ALWAYS AS (SUBSTRING(name, 1, 1)) VIRTUAL;

CREATE INDEX idx_name_first ON names (first_letter);
