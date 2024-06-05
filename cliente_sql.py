from sqlalchemy import create_engine

class SqlClient:
    def __init__(self, user, password, host, database, port):
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

    def query(self, query):
        return self.connection.execute(query)

    def close(self):
        self.connection.close()