SELECT
	* 
FROM crm_pernexium.crm_client 
WHERE 
	crm_pernexium.crm_client.name COLLATE utf8mb4_general_ci LIKE '%joSE%'
    AND
    crm_pernexium.crm_client.phone_number = "5539086157"
    AND 
    crm_pernexium.crm_client.credit_id = "079005238085"
;