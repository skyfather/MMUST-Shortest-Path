import MySQLdb
from MySQLdb import Error

class Dbtest2():
    def __init__(self):
        self.connection = False
        try:
            db = MySQLdb.connect("localhost", "root", "", "proj1")  # "smsdb01")
            cur = db.cursor()
            # sql = "SELECT * FROM vertex"  # users_test"
            # cur.execute(sql)
            # for users in cur.fetchall():
            #     print(users)
            self.connection = True
        except:
            return self.connection
    def getConnection(self):
        try:
            db = MySQLdb.connect("localhost", "root", "", "proj1")  # "smsdb01")
            cur = db.cursor()
            # sql = "SELECT * FROM vertex"  # users_test"
            # cur.execute(sql)
            # for users in cur.fetchall():
            #     print(users)
            self.connection = True
        except Error as e:
            print(e)
        return self.connection