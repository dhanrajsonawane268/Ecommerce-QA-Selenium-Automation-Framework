import pymysql
from utils.config_reader import ConfigReader

class DBUtils:
    def __init__(self):
        self.conn = None

    def connect(self):
        host = ConfigReader.get('DB', 'host', 'localhost')
        port = int(ConfigReader.get('DB', 'port', 3306))
        user = ConfigReader.get('DB', 'user', 'root')
        password = ConfigReader.get('DB', 'password', '')
        database = ConfigReader.get('DB', 'database', None)
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, cursorclass=pymysql.cursors.DictCursor)
        return self.conn

    def execute_query(self, query, params=None):
        if self.conn is None:
            self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query, params or ())
            # try to fetch results if SELECT
            if query.strip().lower().startswith("select"):
                return cur.fetchall()
            else:
                self.conn.commit()
                return cur.rowcount

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
