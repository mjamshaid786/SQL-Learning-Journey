-- remove column phone from persons

ALTER TABLE persons
DROP COLUMN phone

select * from persons