from sqlalchemy import create_engine, text
import pandas as pd

class SqlClient:

    with open ("./sql/get_user_assignments.sql", 'r') as query:
        query_get_user_assignments = query.read()
    with open("./sql/get_interaction_results.sql", 'r') as query:
        query_get_interaction_results= query.read()
    with open("./sql/get_credit_payments.sql", 'r') as query:
        query_get_credit_payments = query.read()
    with open("./sql/insert_interaction_result.sql", 'r') as query:
        query_insert_interaction_result = query.read()
    with open("./sql/search_credit.sql", 'r') as query:
        query_search_credit = query.read()
    with open("./sql/login_email_lookup.sql", 'r') as query:
        query_login_email_lookup = query.read()
    with open('./sql/get_campaings.sql', 'r') as query:
        query_get_campaings = query.read()
    with open('./sql/insert_user.sql', 'r') as query:
        query_insert_user = query.read()
    with open('./sql/get_contact_status.sql', 'r') as query:
        query_get_contact_status = query.read()
    with open('./sql/get_roles.sql', 'r') as query:
        query_get_roles = query.read()


    def __init__(self, user, password, host, database, port):
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

    def get_user_assignments(self, user_id):
        return self.pandas_query(self.query_get_user_assignments.format(user_id = user_id))
    
    def get_interaction_results(self, credit_id):
        return self.pandas_query(self.query_get_interaction_results.format(credit_id = credit_id))
    
    def get_credit_payments(self, credit_id):
        return self.pandas_query(self.query_get_credit_payments.format(credit_id = credit_id))
    
    def insert_interaction_result(self, assignment_id, contact_status_id, contact_substatus_id, comments, payment_promise_date, payment_promise_amount):
        with self.engine.connect() as connection:
            connection.execute(
                text(
                    self.query_insert_interaction_result.format(
                        assignment_id = assignment_id,
                        contact_status_id = contact_status_id,
                        contact_substatus_id = contact_substatus_id,
                        comments = comments,
                        payment_promise_date = payment_promise_date,
                        payment_promise_amount = payment_promise_amount
                    )
                )
            )
            connection.commit()
    
    def search_credit(self, value):
        #TODO: Afinar dependiendo de si se busca por credit_id, name o phone_number
        return self.pandas_query(self.query_search_credit.format(value = value))
    
    def get_campaings(self):
        return self.pandas_query(self.query_get_campaings)
    

    def insert_user(self, name, email, password, campaign_id, role_id):
        query = text(self.query_insert_user.format(name = name, email = email, password = password, campaign_id = campaign_id, role_id = role_id))
        with self.engine.connect() as connection:
            connection.execute(query)
            connection.commit()


    def login_email_lookup(self, email):
        query = text(self.query_login_email_lookup.format(email = email))
        with self.engine.connect() as connection:
            result = connection.execute(query)
            row = result.fetchone()
            if row:
                return dict(zip(result.keys(), row))
            return None
        
    def get_contact_status(self):
        return self.pandas_query(self.query_get_contact_status)

    def get_roles(self):
        return self.pandas_query(self.query_get_roles)

    def pandas_query(self, query):
        with self.engine.connect() as connection:
            return pd.read_sql(query, connection)