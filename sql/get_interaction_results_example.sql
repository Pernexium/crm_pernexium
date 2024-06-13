SELECT 
	creditAssignments.interaction_id,
	parent_contact_status.name as contact_status_name,
    sub_contact_status.name as contact_substatus_name,
	creditAssignments.contact_date,
	creditAssignments.comments,
	creditAssignments.payment_promise_date,
	creditAssignments.payment_promise_amount,
	creditAssignments.call_later_date,
    creditAssignments.reference

FROM 
	(
		SELECT
			crm_pernexium.interaction_result.*,
			crm_pernexium.assignments.reference
			
		FROM crm_pernexium.assignments

		INNER JOIN crm_pernexium.interaction_result
			ON crm_pernexium.assignments.assignment_id = crm_pernexium.interaction_result.assignment_id
		WHERE
			crm_pernexium.assignments.credit_id = 2
) as creditAssignments
	
INNER JOIN crm_pernexium.contact_status AS parent_contact_status
	ON parent_contact_status.contact_status_id = creditAssignments.contact_status_id
	
INNER JOIN crm_pernexium.contact_status AS sub_contact_status
	ON sub_contact_status.contact_status_id = creditAssignments.contact_substatus_id

;