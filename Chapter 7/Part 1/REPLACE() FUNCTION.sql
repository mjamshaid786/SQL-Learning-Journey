-- remove dashes from the number 

SELECT 
	'123-434-54545444' AS phone,

REPLACE('123-434-54545444', '-', '') AS new_phone