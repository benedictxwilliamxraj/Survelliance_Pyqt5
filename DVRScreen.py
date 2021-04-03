# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DVRScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.DVRframe = QtWidgets.QFrame(self.centralwidget)
        self.DVRframe.setStyleSheet("background-image: url(:/wallpaper/cam.jpg);")
        self.DVRframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DVRframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DVRframe.setObjectName("DVRframe")
        self.CentralLibBttn = QtWidgets.QPushButton(self.DVRframe)
        self.CentralLibBttn.setGeometry(QtCore.QRect(20, 320, 131, 91))
        self.CentralLibBttn.setStyleSheet("color: rgb(255, 255, 255);")
        self.CentralLibBttn.setObjectName("CentralLibBttn")
        self.DVRlabel = QtWidgets.QLabel(self.DVRframe)
        self.DVRlabel.setGeometry(QtCore.QRect(50, 30, 96, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.DVRlabel.setFont(font)
        self.DVRlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.DVRlabel.setWordWrap(False)
        self.DVRlabel.setObjectName("DVRlabel")
        self.Logout = QtWidgets.QPushButton(self.DVRframe)
        self.Logout.setGeometry(QtCore.QRect(910, 20, 93, 39))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Logout.setFont(font)
        self.Logout.setStyleSheet("color: rgb(255, 255, 255);")
        self.Logout.setObjectName("Logout")
        self.ADDVR = QtWidgets.QPushButton(self.DVRframe)
        self.ADDVR.setGeometry(QtCore.QRect(910, 70, 93, 39))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ADDVR.setFont(font)
        self.ADDVR.setStyleSheet("color: rgb(255, 255, 255);")
        self.ADDVR.setObjectName("ADDVR")
        self.gridLayout.addWidget(self.DVRframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CentralLibBttn.setText(_translate("MainWindow", "CENTRAL LIBRARY"))
        self.DVRlabel.setText(_translate("MainWindow", "DVR"))
        self.Logout.setText(_translate("MainWindow", "Logout"))
        self.ADDVR.setText(_translate("MainWindow", "ADD DVR"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

