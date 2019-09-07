# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fallen\Documents\project\gui2\AddVertex.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from dbconnections.DbCon import DbCon


class Ui_AddVertex(object):
    def __init__(self):
        self.dbcon = DbCon()
        self.status = self.dbcon.getConnection()

    def setupAddVertex(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 306)
        self.lbl_id = QtWidgets.QLabel(Dialog)
        self.lbl_id.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.lbl_id.setObjectName("lbl_id")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 161, 31))
        self.label_2.setObjectName("label_2")
        self.lbl_name = QtWidgets.QLabel(Dialog)
        self.lbl_name.setGeometry(QtCore.QRect(20, 130, 71, 20))
        self.lbl_name.setObjectName("lbl_name")
        self.txtid = QtWidgets.QLineEdit(Dialog)
        self.txtid.setGeometry(QtCore.QRect(120, 70, 181, 20))
        self.txtid.setObjectName("txtid")
        self.txtname = QtWidgets.QLineEdit(Dialog)
        self.txtname.setGeometry(QtCore.QRect(120, 130, 181, 20))
        self.txtname.setObjectName("txtname")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(350, 0, 31, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/new_icons/icons8-home-page-24.png"))
        self.label_4.setObjectName("label_4")
        self.txtdescription = QtWidgets.QLineEdit(Dialog)
        self.txtdescription.setGeometry(QtCore.QRect(120, 190, 181, 20))
        self.txtdescription.setObjectName("txtdescription")
        self.lbl_description = QtWidgets.QLabel(Dialog)
        self.lbl_description.setGeometry(QtCore.QRect(20, 190, 91, 20))
        self.lbl_description.setObjectName("lbl_description")
        self.btnok = QtWidgets.QPushButton(Dialog)
        self.btnok.setGeometry(QtCore.QRect(220, 260, 71, 23))
        self.btnok.setObjectName("btnok")

        self.btnok.clicked.connect(self.addVertex)

        self.btncancel = QtWidgets.QPushButton(Dialog)
        self.btncancel.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.btncancel.setObjectName("btncancel")

        self.btncancel.clicked.connect(self.cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_id.setText(_translate("Dialog", "Vertex id"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">ADD VERTEX</span></p></body></html>"))
        self.lbl_name.setText(_translate("Dialog", "Vertex name"))
        self.lbl_description.setText(_translate("Dialog", "Vertex description"))
        self.btnok.setText(_translate("Dialog", "Ok"))
        self.btncancel.setText(_translate("Dialog", "Cancel"))

    def addVertex(self):
        if self.status:#
            self.vertexid = self.txtid.text()
            self.vertexname = self.txtname.text()
            self.vertedescription = self.txtdescription.text()
            # self.cur = self.db.cursor()
            # print(self.cur)
            self.dbcon.add_vertex(self.vertexid,self.vertexname,self.vertedescription)
            print(self.vertexid, self.vertexname, self.vertedescription, 'has been saved')
            self.txtid.setText('')
            self.txtname.setText('')
            self.txtdescription.setText('')
        else:
            print("Data not saved")
            # print(self.message)

    def close_application(self):
        # choice = QMessageBox.question(self, 'Exit', "Are you sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        choice = QMessageBox()
        choice.setText('Exit', "Are you sure?")
        choice.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
            quit()
        else:
            pass

    def cancel(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgbtn)

        retval = msg.exec_()
        print("value of pressed message box button:", retval)
        if retval == 1024:
            sys.exit()

    def msgbtn(self,i):
        print("Button pressed is:", i.text())
import new_icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AddVertex()
    ui.setupAddVertex(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

