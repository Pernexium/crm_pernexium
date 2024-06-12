SELECT
	crm_pernexium.interaction_result.*
    
FROM crm_pernexium.assignments

INNER JOIN crm_pernexium.interaction_result
	ON crm_pernexium.assignments.assignment_id = crm_pernexium.interaction_result.assignment_id
WHERE
	crm_pernexium.assignments.credit_id = {credit_id}
;