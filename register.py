# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel
import sys
import sqlite3
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtGui import QFont
import qdarkstyle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 0, 20, 0)
        self.formLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font.setPointSize(15)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setFont(font)
        self.name.setObjectName("plainTextEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setFont(font)
        self.email.setObjectName("plainTextEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.email)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setFont(font)
        self.password.setObjectName("plainTextEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        #self.gridLayout.setContentsMargins(5, 0, 5, 50)
        self.gridLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.addUser)
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("padding: 12px")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat Application"))
        self.label.setText(_translate("MainWindow", "Register User"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainsWindow", "Register"))
        
    def addUser(self):
        
        # Inserting Data from Line Edits into Database
        def InsertData(name, email, password):
            c.execute("INSERT INTO Users(Name, Email, Password) VALUES(?,?,?)", (name, email, password))
            con.commit()
            print('committed')
            
        Name = self.name.text()
        Email = self.email.text()
        Password = self.password.text()
        print(Name,Email,Password)
        checker = [Name, Email, Password]
        
        if "" in checker:
            print('abc')
            dlg = QDialog()
            dlg.setStyleSheet(dark_stylesheet)
            dlg.setWindowTitle("Error")
            dlg.resize(360, 100)
            contact = QLabel('\nEmpty Fields aren\'t accepted!', dlg)
            contact.setAlignment(QtCore.Qt.AlignCenter)
            contact.setFont(QFont("Arial Rounded MT Bold", 14))
            # contact.setStyleSheet("color: white")
            contact.move(10, 10)
            dlg.exec_()

        else:
            con = sqlite3.connect("chatapp.db")
            c = con.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS Users(Name TEXT, Email TEXT PRIMARY KEY, Password TEXT)")
            c.execute('SELECT * FROM Users WHERE Email="{}"'.format(Email))
            row = c.fetchone()
            
            if not row:
                    InsertData(Name, Email, Password)
                    dlg = QDialog()
                    dlg.setStyleSheet(dark_stylesheet)
                    dlg.setWindowTitle("Success")
                    dlg.resize(360, 100)
                    contact = QLabel('\nUser registered successfully!', dlg)
                    contact.setFont(QFont("Arial Rounded MT Bold", 14))
                    # contact.setStyleSheet("color: white")
                    contact.move(10, 10)
                    dlg.exec_()
                    self.name.setText("")
                    self.email.setText("")
                    self.password.setText("")
            else:
                    dlg = QDialog()
                    dlg.setStyleSheet(dark_stylesheet)
                    dlg.setWindowTitle("Error")
                    dlg.resize(250, 90)
                    contact = QLabel('  🛑 ERROR!!!\nEmail already exist!', dlg)
                    contact.setFont(QFont("Arial Rounded MT Bold", 14))
                    # contact.setStyleSheet("color: white")
                    contact.move(10, 10)
                    dlg.exec_()

            con.close()
    
app = QApplication(sys.argv)
dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
app.setStyleSheet(dark_stylesheet)
app.setWindowIcon(QtGui.QIcon('chat-icon.png'))
MainWindow = QMainWindow()
Ui = Ui_MainWindow()
Ui.setupUi(MainWindow)
MainWindow.show()
app.exec()
