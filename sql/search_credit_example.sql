SELECT 
	search.*,
    crm_pernexium.assignments.assignment_id
FROM (
SELECT
	* 
	FROM crm_pernexium.crm_client 
	WHERE 
		crm_pernexium.crm_client.name COLLATE utf8mb4_general_ci LIKE '%%'
		OR
		crm_pernexium.crm_client.phone_number = "5539086157"
		OR 
		crm_pernexium.crm_client.credit_id = "079005238085"
) as search

INNER JOIN crm_pernexium.assignments
	ON crm_pernexium.assignments.credit_id = search.credit_id
    
LIMIT 10
;