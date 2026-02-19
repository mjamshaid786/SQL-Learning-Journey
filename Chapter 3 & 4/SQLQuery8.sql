-- insert date from customers to persons table
INSERT INTO persons (id, person_name, dob, phone)
SELECT 
	id,
	first_name AS person_name,
	NULL AS dob,
	'Unkwon' AS phone
FROM customers

select * from persons