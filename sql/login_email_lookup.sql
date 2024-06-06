SELECT 
	crm_pernexium.users.user_id,
	crm_pernexium.users.name,
	crm_pernexium.users.email,
	crm_pernexium.users.pass,
	crm_pernexium.users.role
FROM crm_pernexium.users
WHERE
	crm_pernexium.users.email = '{email}'
;