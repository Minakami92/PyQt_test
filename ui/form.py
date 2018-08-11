# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(677, 640)
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 20, 621, 231))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 260, 171, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listView_2 = QtGui.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(20, 340, 621, 241))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 290, 171, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), button2Clicked)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), button4Clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def button2Clicked(self,Form):
        pass
    def button4Clicked(self,Form):
        pass
 
   def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", "Add new account", None))
        self.pushButton_4.setText(_translate("Form", "Delete this account", None))

