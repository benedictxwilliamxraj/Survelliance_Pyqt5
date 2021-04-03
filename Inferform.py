# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inferform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Infer_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-image: url(:/wallpaper/wallpaper-1.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Startlab = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Startlab.setFont(font)
        self.Startlab.setObjectName("Startlab")
        self.gridLayout.addWidget(self.Startlab, 0, 0, 1, 1)
        self.startime = QtWidgets.QTimeEdit(Dialog)
        self.startime.setObjectName("startime")
        self.gridLayout.addWidget(self.startime, 0, 1, 1, 1)
        self.Endlabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Endlabel.setFont(font)
        self.Endlabel.setObjectName("Endlabel")
        self.gridLayout.addWidget(self.Endlabel, 1, 0, 1, 1)
        self.endtime = QtWidgets.QTimeEdit(Dialog)
        self.endtime.setObjectName("endtime")
        self.gridLayout.addWidget(self.endtime, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inference Time"))
        self.Startlab.setText(_translate("Dialog", "START TIME"))
        self.Endlabel.setText(_translate("Dialog", "END TIME"))

    def SubmitInfer(self):
        self.sttime = self.startime.text()
        self.etime = self.endtime.text()
        f = open("data/infertime.txt",'w')
        f.write(self.sttime)
        f.write('-')
        f.write(self.etime)
        f.close()

import image_rc

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Infer_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

