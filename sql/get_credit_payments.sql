SELECT 
	crm_pernexium.payments.payment_id,
    crm_pernexium.payments.payment_amount,
    crm_pernexium.payments.payment_date
FROM crm_pernexium.payments

WHERE
	crm_pernexium.payments.credit_id = {credit_id}
;