# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addemail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Addemail_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 300)
        Dialog.setStyleSheet("background-image: url(:/wallpaper/wallpaper-1.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.EmailL = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EmailL.setFont(font)
        self.EmailL.setObjectName("EmailL")
        self.gridLayout.addWidget(self.EmailL, 2, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 2)
        self.NameL = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NameL.setFont(font)
        self.NameL.setObjectName("NameL")
        self.gridLayout.addWidget(self.NameL, 0, 2, 1, 1)
        self.Email = QtWidgets.QLineEdit(Dialog)
        self.Email.setObjectName("Email")
        self.gridLayout.addWidget(self.Email, 2, 3, 1, 1)
        self.Name = QtWidgets.QLineEdit(Dialog)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 0, 3, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Receipt"))
        self.EmailL.setText(_translate("Dialog", "E-Mail ID"))
        self.NameL.setText(_translate("Dialog", "Name"))


    def submitformemail(self):
        f = open( 'data/Receipt.json','r')
        self.list_dump = json.load( f )
        f.close()


        self.email = self.Email.text()
        self.name = self.Name.text()

        # self.dict = {self.name: self.email}
        # self.list_dump[0].update( self.dict )
        # print(self.list_dump)

        self.list_dump.append(self.email)
        f1 = open( 'data/Receipt.json', 'w' )
        self.list_dump = json.dumps( self.list_dump )

        f1.write( self.list_dump )
        f1.close()



import image_rc

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Addemail_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

