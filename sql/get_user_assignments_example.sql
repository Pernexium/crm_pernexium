SELECT
	crm_pernexium.crm_client.*,
    user_assignments.assignment_id,
    user_assignments.user_id
FROM
(
	SELECT     
		crm_pernexium.assignments.assignment_id,
		crm_pernexium.assignments.user_id,
        crm_pernexium.assignments.credit_id
	FROM crm_pernexium.assignments
    WHERE
		crm_pernexium.assignments.user_id = 12
		/* 
			AND 
			FECHA Y OTRAS COSAS 
        */
) AS user_assignments

INNER JOIN crm_pernexium.crm_client
	ON user_assignments.credit_id = crm_pernexium.crm_client.credit_id
;