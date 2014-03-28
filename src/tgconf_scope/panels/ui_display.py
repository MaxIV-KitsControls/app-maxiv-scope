# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created: Thu Mar 27 16:06:32 2014
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_Display(object):
    def setupUi(self, Display):
        Display.setObjectName(_fromUtf8("Display"))
        Display.resize(199, 182)
        self.gridLayout = QtGui.QGridLayout(Display)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusForm = TaurusForm(Display)
        self.taurusForm.setWithButtons(False)
        self.taurusForm.setObjectName(_fromUtf8("taurusForm"))
        self.gridLayout.addWidget(self.taurusForm, 0, 0, 1, 2)

        self.retranslateUi(Display)
        QtCore.QMetaObject.connectSlotsByName(Display)

    def retranslateUi(self, Display):
        Display.setWindowTitle(_translate("Display", "Form", None))

from taurus.qt.qtgui.panel import TaurusForm

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Display = QtGui.QWidget()
    ui = Ui_Display()
    ui.setupUi(Display)
    Display.show()
    sys.exit(app.exec_())

