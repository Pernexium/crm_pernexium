from sqlalchemy import create_engine, text
import pandas as pd

class SqlClient:

    with open ("./sql/get_agent_assignments.sql", 'r') as query:
        query_get_agent_assignments = query.read()
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


    def __init__(self, user, password, host, database, port):
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

    def get_agent_assignments(self, user_id):
        return self.pandas_query(self.query_get_agent_assignments.format(user_id = user_id))
    
    def get_interaction_results(self, credit_id):
        return self.pandas_query(self.query_get_interaction_results.format(credit_id = credit_id))
    
    def get_credit_payments(self, credit_id):
        return self.pandas_query(self.query_get_credit_payments.format(credit_id = credit_id))
    
    def insert_interaction_result(self, assignment_id, contact_date, contact_status, contact_substatus, comments, payment_promise_date, payment_promise_amount):
        with self.engine.connect() as connection:
            connection.execute(
                text(
                    self.query_insert_interaction_result.format(
                        assignment_id = assignment_id,
                        contact_date = contact_date,
                        contact_status = contact_status,
                        contact_substatus = contact_substatus,
                        comments = comments,
                        payment_promise_date = payment_promise_date,
                        payment_promise_amount = payment_promise_amount
                    )
                )
            )
            connection.commit()
    
    def search_credit(self, credit_id, name, phone_number):
        #TODO: Afinar dependiendo de si se busca por credit_id, name o phone_number
        return self.pandas_query(self.query_search_credit.format(credit_id = credit_id, name = name, phone_number = phone_number))
    
    def get_campaings_name(self):
        query = text("SELECT campaign_id, name FROM campaigns")
        with self.engine.connect() as connection:
            result = connection.execute(query)
            dict_names = {x[1]: x[0] for x in result}
        return dict_names
    

    def insert_user(self, nombre, correo, password, campaign_id, rol):
        insert_query = text("INSERT INTO users (campaign_id, name, email, pass) VALUES (:campaign_id, :nombre, :correo, :password, :rol)")
        with self.engine.connect() as connection:
            connection.execute(insert_query, {"campaign_id": campaign_id, "nombre": nombre, "correo": correo, "password": password, "rol": rol})
            connection.commit()


    def login_email_lookup(self, email):
        query = text(self.query_login_email_lookup.format(email = email))
        with self.engine.connect() as connection:
            result = connection.execute(query)
            row = result.fetchone()
            if row:
                return dict(zip(result.keys(), row))
            return None

    def pandas_query(self, query):
        with self.engine.connect() as connection:
            return pd.read_sql(query, connection)