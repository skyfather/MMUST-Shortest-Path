import MySQLdb
from MySQLdb import Error
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

class DbCon():
    def __init__(self):
        self.connection = False
        # self.message = ''
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon("C:\\Users\\Fallen\\PycharmProjects\\project_graph\\pics\\icons.png"))

    def getConnection(self):
        try:
            self.db = MySQLdb.connect("localhost", "root", "", "project_graph1")  # "smsdb01")
            self.connection = True

        except Error as e:
            print(e)
            # return self.message
        return self.connection
    def add_vertex(self,id,name,desc):
        self.cur = self.db.cursor()
        self.sql = '''INSERT INTO vertex2 VALUES('{}','{}','{}')'''.format(id,name,desc)
        self.cur.execute(self.sql)
        self.db.commit()
        # self.db.close()
    def update_vertex(self,id,name,desc):
        try:
            self.cur = self.db.cursor()
            self.sql = '''UPDATE vertex2 SET vertex_id='{}',vertex_name='{}',
                            vertex_description='{}' WHERE vertex_id='{}' '''.format(id,name,desc,id)
            self.cur.execute(self.sql)
            self.db.commit()
        except Error as e:
            print(e)
    def delete_vertex(self,id):
        try:
            self.cur = self.db.cursor()
            self.sql = '''DELETE FROM vertex2 WHERE vertex_id ='{}' '''.format(id)
            self.cur.execute(self.sql)
            self.db.commit()
        except Error as e:
            print(e)
    def delete_verticies(self):
        try:
            self.cur = self.db.cursor()
            self.sql = '''DELETE FROM vertex2 WHERE vertex_id>0'''
            self.cur.execute(self.sql)
            self.db.commit()
        except Error as e:
            print(e)
    def get_vertex(self,id):
        try:
            self.curr = self.db.cursor()
            self.query = '''SELECT * FROM vertex2 WHERE vertex_id='{}' '''.format(id)
            self.curr.execute(self.query)
            rows = self.curr.fetchone()
            # print(rows)
            return rows
        except Error as e:
            print(e)
    def get_vertices(self):
        try:
            self.curr = self.db.cursor()
            self.query = '''SELECT * FROM vertex2'''
            self.curr.execute(self.query)
            rows = self.curr.fetchall()
            # print(rows)
            return rows
        except Error as e:
            print(e)
        # finally:
        #     self.db.close()
    def add_edge(self,edge_name,weight,start_vertex,target_vertex):
        try:
            self.cur = self.db.cursor()
            # id = int(id)
            weight = int(weight)
            self.query = '''INSERT INTO edgefrom333(name,length,startv,targetv) VALUES('{}','{}','{}','{}')'''.format(edge_name, weight, start_vertex,target_vertex)
            # self.query2 = '''INSERT INTO edgefrom3(id,name,length,startv,targetv)(name,length,startv,targetv) VALUES('{}','{}','{}','{}')'''.format(edge_name, weight, start_vertex,target_vertex)
            self.cur.execute(self.query)
            # self.cur.execute(self.query2)
            self.db.commit()
            # self.query2 = '''INSERT INTO edgefrom3(name,length,startv,targetv)(name,length,startv,targetv) VALUES('{}','{}','{}','{}')'''.format(edge_name, weight, start_vertex, target_vertex)
            # self.cur.execute(self.query2)
            # self.db.commit()
        except Error as e:
            print(e)
        # self.db.close()
    def add_edge2(self,edge_name,weight,start_vertex,target_vertex):
        try:
            self.cur = self.db.cursor()
            weight = int(weight)
            self.query = '''INSERT INTO edgefrom333(name,length,startv,targetv) VALUES('{}','{}','{}','{}','{}')'''.format(edge_name, weight, start_vertex,target_vertex)
            # self.query2 = '''INSERT INTO edgefrom3(id,name,length,startv,targetv)(name,length,startv,targetv) VALUES('{}','{}','{}','{}')'''.format(edge_name, weight, start_vertex,target_vertex)
            self.cur.execute(self.query)
            # self.cur.execute(self.query2)
            self.db.commit()
            # self.query2 = '''INSERT INTO edgefrom3(name,length,startv,targetv)(name,length,startv,targetv) VALUES('{}','{}','{}','{}')'''.format(edge_name, weight, start_vertex, target_vertex)
            # self.cur.execute(self.query2)
            # self.db.commit()
        except Error as e:
            print(e)

    def update_edge(self,id,name,length,startv,targetv):
        try:
            self.cur = self.db.cursor()
            self.query = '''UPDATE edgefrom333 SET name='{}',
                            length='{}',startv='{}',targetv='{}' WHERE id ='{}' '''.format(name,length,startv,targetv,id)
            self.cur.execute(self.query)
            self.db.commit()

            # self.msg.setIcon(QMessageBox.Information)
            # self.msg.setText("Path {} has been updated".format(name))
            # self.msg.setWindowTitle("Path Update")
            # self.msg.setStandardButtons(QMessageBox.Ok)
            # self. msg.exec_()
        except Error as e:
            # print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText(str(e).strip("()"))
            # msg.setInformativeText("Are you sure you want to block path? ")
            msg.setWindowTitle("Path Update")
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    def block_path(self,name,startv,targetv):
        try:
            self.cur = self.db.cursor()
            self.query = '''UPDATE edgefrom333 SET blocked = '1' where startv = '{}' and targetv= '{}' '''.format(startv,targetv)
            # self.query2 = '''UPDATE edgefrom3 SET blocked = '1' where targetv = '{}' and startv= '{}' '''.format(startv,targetv)
            self.cur.execute(self.query)
            # self.cur.execute(self.query2)
            self.db.commit()

            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Path {} has been blocked".format(name))
            self.msg.setWindowTitle("Path Update")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self. msg.exec_()
        except Error as e:
            # print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText(str(e).strip("()"))
            # msg.setInformativeText("Are you sure you want to block path? ")
            msg.setWindowTitle("Path Update")
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def block_path2(self,name):
        try:
            self.cur = self.db.cursor()
            self.query = '''UPDATE edgefrom333 SET blocked = '1' where name = '{}' '''.format(name)
            self.cur.execute(self.query)
            self.db.commit()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Path {} has been blocked".format(name))
            self.msg.setWindowTitle("Path Update")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self. msg.exec_()
        except Error as e:
            # print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e).strip("()"))
            msg.setWindowTitle("Path Update")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def unblock_path(self,name,startv,targetv):
        try:
            self.cur = self.db.cursor()
            self.query = '''UPDATE edgefrom333 SET blocked = '0' where startv = '{}' and targetv= '{}' '''.format(startv,targetv)
            # self.query2 = '''UPDATE edgefrom3 SET blocked = '0' where targetv = '{}' and startv= '{}' '''.format(startv,targetv)
            self.cur.execute(self.query)
            # self.cur.execute(self.query2)
            self.db.commit()

            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Path {} has been blocked".format(name))
            self.msg.setWindowTitle("Path Update")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self. msg.exec_()
        except Error as e:
            # print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText(str(e).strip("()"))
            # msg.setInformativeText("Are you sure you want to block path? ")
            msg.setWindowTitle("Path Update")
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def unblock_path2(self,name):
        try:
            self.cur = self.db.cursor()
            self.query = '''UPDATE edgefrom333 SET blocked = '0' where name = '{}' '''.format(name)
            self.cur.execute(self.query)
            self.db.commit()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Path {} has been unblocked".format(name))
            self.msg.setWindowTitle("Path Update")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self. msg.exec_()
        except Error as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e).strip("()"))
            msg.setWindowTitle("Path Update")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def blockedPaths(self):
        try:
            self.cur = self.db.cursor()
            self.query = '''SELECT * FROM edgefrom333 WHERE blocked='1' '''
            self.cur.execute(self.query)
            rows = self.cur.fetchall()
            # print(rows)
            return rows
        except Error as e:
            print(e)
    def delete_edge(self,id):
        try:
            self.cur = self.db.cursor()
            self.query = '''DELETE  FROM edgefrom333 WHERE id='{}' '''.format(id)
            self.cur.execute(self.query)
            self.db.commit()
        except Error as e:
            print(e)
    def delete_edges(self):
        try:
            self.cur = self.db.cursor()
            self.query = '''DELETE FROM edgefrom333 WHERE id>0'''
            self.cur.execute(self.query)
            self.db.commit()
        except Error as e:
            print(e)
    def get_edge(self,id):
        try:
            self.curr = self.db.cursor()
            self.query = '''SELECT * FROM edgesfrom333 WHERE id='{}' '''.format(id)
            self.curr.execute(self.query)
            rows = self.curr.fetchone()
            # print(rows)
            return rows
        except Error as e:
            print(e)
    def get_edges(self):
        try:
            self.curr = self.db.cursor()
            self.query = '''SELECT * FROM edgefrom333'''
            self.curr.execute(self.query)
            rows = self.curr.fetchall()
            # print(rows)
            return rows
        except Error as e:
            print(e)

    def adduser(self,id,username,password):
        try:
            self.curr = self.db.cursor()
            self.query = '''INSERT INTO users VALUES('{}','{}','{}')'''.format(id,username,password)
            self.curr.execute(self.query)
            self.db.commit()
        except Error as e:
            print(e)
    def authenticate_user(self,username,password):
        try:
            self.curr = self.db.cursor()
            self.query = '''SELECT * FROM users where username='{}' AND
                            password='{}' '''.format(username,password)
            self.curr.execute(self.query)
            rows = self.curr.fetchone()
            # print(rows)
            return rows
        except Error as e:
            print(e)

    def get_user(self,username):
        try:
            self.curr = self.db.cursor()
            self.query = '''SELECT * FROM users where username='{}' '''.format(username)
            self.curr.execute(self.query)
            rows = self.curr.fetchone()
            # print(rows)
            return rows
        except Error as e:
            print(e)
    def update_User(self,username,password,id):
        try:
            self.curr = self.db.cursor()
            self.query = '''UPDATE users SET username = '{}' AND password='{}' where id = '{}' '''.format(username,password,id)
            self.curr.execute(self.query)
            self.db.commit()
        except Error as e:
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Unable to update User")
            self.msg.setWindowTitle("Login")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()
