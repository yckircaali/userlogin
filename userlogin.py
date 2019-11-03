import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.database()
        self.SetupUi()

    def database(self):
        db = sqlite3.connect("users.db")
        self.cursor = db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS USERS (username TEXT, password TEXT)')
        self.cursor.execute('INSERT INTO USERS VALUES ("admin","123456")')
        db.commit()

    def SetupUi(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Login")
        self.kayitol = QtWidgets.QPushButton("Sign Up")
        self.yazialani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayitol)

        self.setLayout(v_box)
        self.setWindowTitle("User Login")
        self.giris.clicked.connect(self.login)
        self.kayitol.clicked.connect(self.signup)
        self.setFixedSize(200,175)
        self.show()

    def login(self):
        adi = self.username.text()
        par = self.password.text()
        self.cursor.execute('SELECT * FROM USERS WHERE username=? and password=?',(adi,par))
        data = self.cursor.fetchall()
        if(len(data) == 0):
            self.yazialani.setText("Böyle bir kullanıcı bulunamadı!")
        else:
            self.yazialani.setText("Giriş Başarılı.")

    def signup(self):
        ui2.show()

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

app = QtWidgets.QApplication(sys.argv)
ui = Ui()
ui2 = Ui2()
sys.exit(app.exec_())