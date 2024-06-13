INSERT INTO crm_pernexium.interaction_result
	(assignment_id, contact_status_id, contact_substatus_id, comments, payment_promise_date, payment_promise_amount)
VALUES 
	({assignment_id}, {contact_status_id}, {contact_substatus_id}, "{comments}", "{payment_promise_date}", {payment_promise_amount})
;