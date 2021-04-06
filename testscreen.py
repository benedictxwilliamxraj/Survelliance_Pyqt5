# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Screenframe = QtWidgets.QFrame(self.centralwidget)
        self.Screenframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Screenframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Screenframe.setObjectName("Screenframe")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Screenframe)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Screenlabel = QtWidgets.QLabel(self.Screenframe)
        self.Screenlabel.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Screenlabel.setObjectName("Screenlabel")
        self.gridLayout_2.addWidget(self.Screenlabel, 1, 0, 2, 2)
        self.CurrDVRName = QtWidgets.QLabel(self.Screenframe)
        self.CurrDVRName.setMaximumSize(QtCore.QSize(250, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CurrDVRName.setFont(font)
        self.CurrDVRName.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.CurrDVRName.setObjectName("CurrDVRName")
        self.gridLayout_2.addWidget(self.CurrDVRName, 0, 0, 1, 1)
        self.Timelabel = QtWidgets.QLabel(self.Screenframe)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Timelabel.setFont(font)
        self.Timelabel.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.Timelabel.setObjectName("Timelabel")
        self.gridLayout_2.addWidget(self.Timelabel, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.Screenframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuDVR = QtWidgets.QMenu(self.menubar)
        self.menuDVR.setObjectName("menuDVR")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_DVR = QtWidgets.QAction(MainWindow)
        self.actionAdd_DVR.setObjectName("actionAdd_DVR")
        self.actionCentral_Library = QtWidgets.QAction(MainWindow)
        self.actionCentral_Library.setObjectName("actionCentral_Library")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuMenu.addAction(self.actionAdd_DVR)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionLogout)
        self.menuDVR.addAction(self.actionCentral_Library)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuDVR.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Screenlabel.setText(_translate("MainWindow", "TextLabel"))
        self.CurrDVRName.setText(_translate("MainWindow", "Central Library"))
        self.Timelabel.setText(_translate("MainWindow", "TextLabel"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuDVR.setTitle(_translate("MainWindow", "DVR"))
        self.actionAdd_DVR.setText(_translate("MainWindow", "Add DVR"))
        self.actionCentral_Library.setText(_translate("MainWindow", "Central Library"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

