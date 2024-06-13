SELECT 
	search.client_id,
    crm_pernexium.assignments.assignment_id,
    search.credit_id,
    search.name AS client_name,
    search.product_name,
    search.current_balance, 
    search.balance_to_settle,
    crm_pernexium.assignments.reference as assignment_reference
    
FROM (
	SELECT
		* 
	FROM crm_pernexium.crm_client 

	WHERE 
		/*AFINAR EN PYTHON*/
		crm_pernexium.crm_client.name COLLATE utf8mb4_general_ci LIKE '%%{value}%%'
		OR
		/*
			crm_pernexium.crm_client.phone_number = "{value}"
		OR 
		*/
		crm_pernexium.crm_client.credit_id = {value}
) as search

INNER JOIN crm_pernexium.assignments
	ON crm_pernexium.assignments.credit_id = search.credit_id
    
LIMIT 10
;