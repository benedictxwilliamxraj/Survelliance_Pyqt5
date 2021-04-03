# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Loginframe = QtWidgets.QFrame(self.centralwidget)
        self.Loginframe.setStyleSheet("background-image: url(:/wallpaper/wallpaper-1.jpg);")
        self.Loginframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Loginframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Loginframe.setObjectName("Loginframe")
        self.LoginLabel = QtWidgets.QLabel(self.Loginframe)
        self.LoginLabel.setGeometry(QtCore.QRect(280, 160, 151, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setObjectName("LoginLabel")
        self.UsernameLabel = QtWidgets.QLabel(self.Loginframe)
        self.UsernameLabel.setGeometry(QtCore.QRect(280, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.UsernameLabel.setFont(font)
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.PasswordLabel = QtWidgets.QLabel(self.Loginframe)
        self.PasswordLabel.setGeometry(QtCore.QRect(280, 310, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.UsernameInput = QtWidgets.QLineEdit(self.Loginframe)
        self.UsernameInput.setGeometry(QtCore.QRect(400, 250, 113, 22))
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(self.Loginframe)
        self.PasswordInput.setGeometry(QtCore.QRect(400, 310, 113, 22))
        self.PasswordInput.setObjectName("PasswordInput")
        self.LoginButton = QtWidgets.QPushButton(self.Loginframe)
        self.LoginButton.setGeometry(QtCore.QRect(400, 360, 93, 28))
        self.LoginButton.setObjectName("LoginButton")
        self.label = QtWidgets.QLabel(self.Loginframe)
        self.label.setGeometry(QtCore.QRect(430, 160, 61, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/fcritlogo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Loginframe)
        self.label_2.setGeometry(QtCore.QRect(660, 430, 151, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/logo/tifr-logo.png"))
        self.label_2.setObjectName("label_2")
        self.LoginLabel_2 = QtWidgets.QLabel(self.Loginframe)
        self.LoginLabel_2.setGeometry(QtCore.QRect(210, 70, 391, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        self.LoginLabel_2.setFont(font)
        self.LoginLabel_2.setObjectName("LoginLabel_2")
        self.gridLayout.addWidget(self.Loginframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoginLabel.setText(_translate("MainWindow", "LOGIN"))
        self.UsernameLabel.setText(_translate("MainWindow", "Username"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password"))
        self.LoginButton.setText(_translate("MainWindow", "Submit"))
        self.LoginLabel_2.setText(_translate("MainWindow", "AI Surveillance System"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

