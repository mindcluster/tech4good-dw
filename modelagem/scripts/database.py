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

    def insert(self, sql):
        print(sql)
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)

        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()

    def execute(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        return mycursor.fetchall()

    def close(self):
        self.mydb.close()
