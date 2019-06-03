import psycopg2
from config import config


class Database:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect_db(self):
        try:
            params = config()

            self.conn = psycopg2.connect(**params)
            self.cur = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
        finally:
            if self.conn is None:
                return False
        return True

    def close_db(self):
        try:
            self.conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def exec_query(self, query):
        try:
            self.cur.execute(query)
            record = self.cur.fetchone()[0]
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            return error

        self.conn.commit()
        return record
