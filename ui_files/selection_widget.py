# Form implementation generated from reading ui file 'selection_menu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SelectionMenu(object):
    def setupUi(self, SelectionMenu):
        SelectionMenu.setObjectName("SelectionMenu")
        SelectionMenu.resize(527, 523)
        self.btnGotoGenerate = QtWidgets.QPushButton(parent=SelectionMenu)
        self.btnGotoGenerate.setGeometry(QtCore.QRect(130, 60, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnGotoGenerate.setFont(font)
        self.btnGotoGenerate.setObjectName("btnGotoGenerate")
        self.btnGotoGrade = QtWidgets.QPushButton(parent=SelectionMenu)
        self.btnGotoGrade.setGeometry(QtCore.QRect(130, 200, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGotoGrade.setFont(font)
        self.btnGotoGrade.setObjectName("btnGotoGrade")
        self.btnMyPass = QtWidgets.QPushButton(parent=SelectionMenu)
        self.btnMyPass.setGeometry(QtCore.QRect(130, 350, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnMyPass.setFont(font)
        self.btnMyPass.setObjectName("btnMyPass")
        self.btnBack = QtWidgets.QPushButton(parent=SelectionMenu)
        self.btnBack.setGeometry(QtCore.QRect(0, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")

        self.retranslateUi(SelectionMenu)
        QtCore.QMetaObject.connectSlotsByName(SelectionMenu)

    def retranslateUi(self, SelectionMenu):
        _translate = QtCore.QCoreApplication.translate
        SelectionMenu.setWindowTitle(_translate("SelectionMenu", "Меню выбора"))
        self.btnGotoGenerate.setText(_translate("SelectionMenu", "Генерация пароля"))
        self.btnGotoGrade.setText(_translate("SelectionMenu", "Оценка пароля"))
        self.btnMyPass.setText(_translate("SelectionMenu", "Мои пароли"))
        self.btnBack.setText(_translate("SelectionMenu", "<-"))