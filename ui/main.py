#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
import form

def onClickedButton2():
    pass
def onClickedButton4():
    pass
class MyForm(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = form.Ui_Form()
        self.ui.setupUi(self)
        

def run_app():
    app = QtGui.QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    run_app()
