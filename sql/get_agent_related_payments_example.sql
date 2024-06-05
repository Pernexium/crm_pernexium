SELECT
/*Obtener columnas necesarias*/
*
FROM 
(
	SELECT
		crm_pernexium.assignments.agent_id,
		crm_pernexium.credits.*
    FROM 
		crm_pernexium.credits 
    INNER JOIN crm_pernexium.assignments
		ON crm_pernexium.credits.credit_id = crm_pernexium.assignments.credit_id
	WHERE
		crm_pernexium.assignments.agent_id = "1"
) as agent_credits
INNER JOIN crm_pernexium.payments
	ON agent_credits.credit_id = crm_pernexium.payments.credit_id
;