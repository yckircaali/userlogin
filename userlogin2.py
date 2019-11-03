# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idpassword.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

class Ui_Dialog(object):
    def __init__(self):
        super().__init__()
        self.databaseDB()

    def databaseDB(self):
        db = sqlite3.connect("database.db")
        self.cursor = db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS USERS (username TEXT, password TEXT)')
        db.commit()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 70, 21, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 61, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(125, 250, 241, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 181, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 110, 181, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 190, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signup)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def login(self):
        adi = self.label.text()
        par = self.label_2.text()
        self.cursor.execute('SELECT * FROM USERS WHERE username=? and password=?',(adi,par))
        data = self.cursor.fetchall()
        if (len(data) == 0):
            self.label_3.setText("Böyle bir kullanıcı bulunamadı!")
        else:
            self.label_3.setText("Giriş Başarılı.")

    def signup(self):
        ui2.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Login"))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Kayıt Ol"))

class Ui2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.database()
        self.SetupUi2()

    def database(self):
        self.db = sqlite3.connect("users.db")
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS USERS (username TEXT, password TEXT)')
        self.cursor.execute('INSERT INTO USERS VALUES ("admin","123456")')
        self.db.commit()

    def SetupUi2(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kayitol = QtWidgets.QPushButton("Sign Up")
        self.yazialani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.kayitol)

        self.setLayout(v_box)
        self.setWindowTitle("Sign Up")
        self.kayitol.clicked.connect(self.signup2)
        self.setFixedSize(200, 175)

    def signup2(self):
        adi = self.username.text()
        par = self.password.text()
        self.cursor.execute('INSERT INTO USERS VALUES (?,?)',(adi,par))
        self.db.commit()
        self.yazialani.setText("Kayıt Başarılı.")
        self.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui2 = Ui2()
    sys.exit(app.exec_())

