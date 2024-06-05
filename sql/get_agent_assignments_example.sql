SELECT
	crm_pernexium.crm_client.*,
    agent_assignments.*
FROM 
(
	SELECT     
		crm_pernexium.assignments.assignment_id,
		crm_pernexium.assignments.agent_id,
        crm_pernexium.assignments.credit_id
	FROM crm_pernexium.assignments
    WHERE
		crm_pernexium.assignments.agent_id = "1"
		/* 
			AND 
			FECHA Y OTRAS COSAS 
        */
) AS agent_assignments

INNER JOIN crm_pernexium.crm_client
	ON agent_assignments.credit_id = crm_pernexium.crm_client.credit_id
;