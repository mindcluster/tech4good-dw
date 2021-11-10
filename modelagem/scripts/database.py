import mysql.connector


class Database:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="tech4good"
        )

    def select(self, table):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM " + table)
        return mycursor.fetchall()

    def insert(self, sql, data):
        mycursor = self.mydb.cursor()
        mycursor.executemany(sql, data)

        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()

    def execute(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        return mycursor.fetchall()

    def close(self):
        self.mydb.close()
