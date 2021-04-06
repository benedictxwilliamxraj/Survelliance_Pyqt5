# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inferform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class Infer_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 300)
        Dialog.setStyleSheet("background-image: url(:/wallpaper/wallpaper-1.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Endlabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Endlabel.setFont(font)
        self.Endlabel.setObjectName("Endlabel")
        self.gridLayout.addWidget(self.Endlabel, 2, 2, 1, 1)
        self.Startlab = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Startlab.setFont(font)
        self.Startlab.setObjectName("Startlab")
        self.gridLayout.addWidget(self.Startlab, 0, 2, 1, 1)
        self.enddttime = QtWidgets.QDateTimeEdit(Dialog)
        self.enddttime.setObjectName("enddttime")
        self.gridLayout.addWidget(self.enddttime, 2, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 2)
        self.stdatetime = QtWidgets.QDateTimeEdit(Dialog)
        self.stdatetime.setObjectName("stdatetime")
        self.gridLayout.addWidget(self.stdatetime, 0, 3, 1, 1)
        self.Alltime = QtWidgets.QRadioButton(Dialog)
        self.Alltime.setObjectName("Alltime")
        self.gridLayout.addWidget(self.Alltime, 3, 3, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Infer Time"))
        self.Endlabel.setText(_translate("Dialog", "End Time"))
        self.Startlab.setText(_translate("Dialog", "Start Time"))
        self.Alltime.setText(_translate("Dialog", "ALL time"))



    def SubmitInfer(self):
        if self.Alltime.isChecked():
            # self.stdatetime.setDisabled(True)
            # self.enddttime.setDisabled(True)
            f = open('data/infertime.txt','w')
            f.write('0000')
            f.close()
        else:
            self.st = datetime.datetime.strptime(self.stdatetime.text(), "%d/%m/%Y  %H:%M")
            self.st = datetime.datetime.timestamp( self.st )
            print(self.st)
            self.ed = datetime.datetime.strptime( self.stdatetime.text(), "%d/%m/%Y  %H:%M" )
            self.ed = datetime.datetime.timestamp( self.ed )

            f = open('data/infertime.txt','w')
            f.write(self.st)
            f.write('-')
            f.write(self.ed)
            f.close()

import image_rc

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

