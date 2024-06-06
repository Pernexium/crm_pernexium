SELECT
	crm_pernexium.crm_client.*,
    agent_assignments.assignment_id,
    agent_assignments.user_id
FROM
(
	SELECT     
		crm_pernexium.assignments.assignment_id,
		crm_pernexium.assignments.user_id,
        crm_pernexium.assignments.credit_id
	FROM crm_pernexium.assignments
    WHERE
		crm_pernexium.assignments.user_id = "{user_id}"
		/* 
			AND 
			FECHA Y OTRAS COSAS 
        */
) AS agent_assignments

INNER JOIN crm_pernexium.crm_client
	ON agent_assignments.credit_id = crm_pernexium.crm_client.credit_id
;