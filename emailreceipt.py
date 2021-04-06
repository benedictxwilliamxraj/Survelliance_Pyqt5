# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmailReceipt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import addemail
import json

class Emaillist_Dialog(object):
    def __init__(self):
        self.model = QtGui.QStandardItemModel()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(446, 437)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setObjectName("listView")

        self.listView.setModel( self.model )
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 2)
        self.newBttn = QtWidgets.QPushButton(Dialog)
        self.newBttn.setObjectName("newBttn")
        self.gridLayout.addWidget(self.newBttn, 1, 0, 1, 1)
        self.Deletebttn = QtWidgets.QPushButton(Dialog)
        self.Deletebttn.setObjectName("Deletebttn")
        self.gridLayout.addWidget(self.Deletebttn, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        ####Listview##
        self.f = open('data/Receipt.json','r')
        self.dict_dump = json.load( self.f )
        self.f.close()
        for i in range(len(self.dict_dump)):
            item = QtGui.QStandardItem(self.dict_dump[i])
            self.model.appendRow( item)




        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ##all connection
        self.newBttn.clicked.connect(lambda: self.addemail())
        self.Deletebttn.clicked.connect( lambda: self.deleteemail() )

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Recipient"))
        self.newBttn.setText(_translate("Dialog", "New"))
        self.Deletebttn.setText(_translate("Dialog", "Delete"))

    def addemail(self):
        Dialog = QtWidgets.QDialog()
        ui = addemail.Addemail_Dialog()
        ui.setupUi( Dialog )
        Dialog.show()
        res = Dialog.exec_()
        if res == QtWidgets.QDialog.Accepted:
            ui.submitformemail()

    # def deleteemail(self):
    #     item  = self.listView.currentIndex()
    #     print(item)
        # f = open('data/Receipt.json')
        # self.list_dump =

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Emaillist_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     # sys.exit(app.exec_())

