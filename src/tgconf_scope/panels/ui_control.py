# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created: Thu Feb 13 17:59:34 2014
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

class Ui_Control(object):
    def setupUi(self, Control):
        Control.setObjectName(_fromUtf8("Control"))
        Control.resize(199, 182)
        self.gridLayout = QtGui.QGridLayout(Control)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusForm = TaurusForm(Control)
        self.taurusForm.setWithButtons(False)
        self.taurusForm.setObjectName(_fromUtf8("taurusForm"))
        self.gridLayout.addWidget(self.taurusForm, 0, 0, 1, 2)
        self.golocalButton = TaurusCommandButton(Control)
        self.golocalButton.setModel(_fromUtf8(""))
        self.golocalButton.setObjectName(_fromUtf8("golocalButton"))
        self.gridLayout.addWidget(self.golocalButton, 1, 0, 1, 1)
        self.startButton = TaurusCommandButton(Control)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.gridLayout.addWidget(self.startButton, 1, 1, 1, 1)

        self.retranslateUi(Control)
        QtCore.QMetaObject.connectSlotsByName(Control)

    def retranslateUi(self, Control):
        Control.setWindowTitle(_translate("Control", "Form", None))

from taurus.qt.qtgui.panel import TaurusForm
from taurus.qt.qtgui.button import TaurusCommandButton

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Control = QtGui.QWidget()
    ui = Ui_Control()
    ui.setupUi(Control)
    Control.show()
    sys.exit(app.exec_())

