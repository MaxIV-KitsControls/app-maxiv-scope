# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testplot.ui'
#
# Created: Thu Feb 27 11:46:44 2014
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

class Ui_TestPlot(object):
    def setupUi(self, TestPlot):
        TestPlot.setObjectName(_fromUtf8("TestPlot"))
        TestPlot.resize(547, 510)
        self.gridLayout = QtGui.QGridLayout(TestPlot)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusPlot = TaurusPlot(TestPlot)
        self.taurusPlot.setAllowZoomers(False)
        self.taurusPlot.setProperty("enableMagnifier", False)
        self.taurusPlot.setObjectName(_fromUtf8("taurusPlot"))
        self.gridLayout.addWidget(self.taurusPlot, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(TestPlot)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.taurusValueLineEditVert = TaurusValueLineEdit(self.groupBox)
        self.taurusValueLineEditVert.setObjectName(_fromUtf8("taurusValueLineEditVert"))
        self.gridLayout_2.addWidget(self.taurusValueLineEditVert, 1, 1, 1, 1)
        self.taurusValueLineEditTimeMin = TaurusValueLineEdit(self.groupBox)
        self.taurusValueLineEditTimeMin.setObjectName(_fromUtf8("taurusValueLineEditTimeMin"))
        self.gridLayout_2.addWidget(self.taurusValueLineEditTimeMin, 1, 2, 1, 1)
        self.taurusValueLineEditTimeMax = TaurusValueLineEdit(self.groupBox)
        self.taurusValueLineEditTimeMax.setObjectName(_fromUtf8("taurusValueLineEditTimeMax"))
        self.gridLayout_2.addWidget(self.taurusValueLineEditTimeMax, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(TestPlot)
        QtCore.QMetaObject.connectSlotsByName(TestPlot)

    def retranslateUi(self, TestPlot):
        TestPlot.setWindowTitle(_translate("TestPlot", "Form", None))
        self.groupBox.setTitle(_translate("TestPlot", "Cursors", None))
        self.label.setText(_translate("TestPlot", "Vertical", None))
        self.label_2.setText(_translate("TestPlot", "Time min", None))
        self.label_3.setText(_translate("TestPlot", "Time max", None))

from taurus.qt.qtgui.plot import TaurusPlot
from taurus.qt.qtgui.input import TaurusValueLineEdit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TestPlot = QtGui.QWidget()
    ui = Ui_TestPlot()
    ui.setupUi(TestPlot)
    TestPlot.show()
    sys.exit(app.exec_())

