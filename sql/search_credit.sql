SELECT
	* 
FROM crm_pernexium.crm_client 

WHERE 
	crm_pernexium.crm_client.name COLLATE utf8mb4_general_ci LIKE '%<NAME>%'
    AND
    crm_pernexium.crm_client.phone_number = "<TEL>"
    AND 
    crm_pernexium.crm_client.credit_id = "<ID>"
;