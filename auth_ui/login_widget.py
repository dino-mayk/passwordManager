# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(622, 312)
        self.labelPassword = QtWidgets.QLabel(parent=Login)
        self.labelPassword.setGeometry(QtCore.QRect(150, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.linePassword = QtWidgets.QLineEdit(parent=Login)
        self.linePassword.setGeometry(QtCore.QRect(250, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linePassword.setFont(font)
        self.linePassword.setObjectName("linePassword")
        self.lineLogin = QtWidgets.QLineEdit(parent=Login)
        self.lineLogin.setGeometry(QtCore.QRect(250, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineLogin.setFont(font)
        self.lineLogin.setObjectName("lineLogin")
        self.labelLogin = QtWidgets.QLabel(parent=Login)
        self.labelLogin.setGeometry(QtCore.QRect(150, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelLogin.setFont(font)
        self.labelLogin.setObjectName("labelLogin")
        self.btnLogin = QtWidgets.QPushButton(parent=Login)
        self.btnLogin.setGeometry(QtCore.QRect(270, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnBack = QtWidgets.QPushButton(parent=Login)
        self.btnBack.setGeometry(QtCore.QRect(0, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.labelPassword.setText(_translate("Login", "Пароль:"))
        self.labelLogin.setText(_translate("Login", "Логин:"))
        self.btnLogin.setText(_translate("Login", "Войти"))
        self.btnBack.setText(_translate("Login", "<-"))