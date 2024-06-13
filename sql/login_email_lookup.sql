SELECT 
	crm_pernexium.users.user_id,
	crm_pernexium.users.name,
	crm_pernexium.users.email,
	crm_pernexium.users.password,
	crm_pernexium.users.role_id
FROM crm_pernexium.users
WHERE
	crm_pernexium.users.email = '{email}'
;