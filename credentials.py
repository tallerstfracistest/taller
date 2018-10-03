import mysql.connector

class Database:
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host="sql3.freemysqlhosting.net",
            user="sql3259391",
            password="meWRlNdurJ",
            database="sql3259391"
        )

    def execute(self, query, params=None):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        if "SELECT" in query:
            return cursor.fetchall()
        if "INSERT" in query:
            return self.db.commit()