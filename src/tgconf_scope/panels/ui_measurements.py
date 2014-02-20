# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measurements.ui'
#
# Created: Wed Feb 19 13:00:20 2014
#      by: PyQt4 UI code generator 4.10.3
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
        Form.resize(855, 479)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.configMeasurement2 = TaurusValueComboBox(Form)
        self.configMeasurement2.setAutoApply(True)
        self.configMeasurement2.setObjectName(_fromUtf8("configMeasurement2"))
        self.gridLayout.addWidget(self.configMeasurement2, 1, 1, 1, 1)
        self.taurusLabelVal2 = TaurusLabel(Form)
        self.taurusLabelVal2.setObjectName(_fromUtf8("taurusLabelVal2"))
        self.gridLayout.addWidget(self.taurusLabelVal2, 1, 2, 1, 1)
        self.taurusLabelVal1 = TaurusLabel(Form)
        self.taurusLabelVal1.setObjectName(_fromUtf8("taurusLabelVal1"))
        self.gridLayout.addWidget(self.taurusLabelVal1, 0, 2, 1, 1)
        self.sourceMeasurement2 = TaurusValueComboBox(Form)
        self.sourceMeasurement2.setAutoApply(True)
        self.sourceMeasurement2.setObjectName(_fromUtf8("sourceMeasurement2"))
        self.gridLayout.addWidget(self.sourceMeasurement2, 1, 0, 1, 1)
        self.taurusLabelVal3 = TaurusLabel(Form)
        self.taurusLabelVal3.setObjectName(_fromUtf8("taurusLabelVal3"))
        self.gridLayout.addWidget(self.taurusLabelVal3, 2, 2, 1, 1)
        self.taurusLabelVal4 = TaurusLabel(Form)
        self.taurusLabelVal4.setObjectName(_fromUtf8("taurusLabelVal4"))
        self.gridLayout.addWidget(self.taurusLabelVal4, 3, 2, 1, 1)
        self.taurusLabelVal5 = TaurusLabel(Form)
        self.taurusLabelVal5.setObjectName(_fromUtf8("taurusLabelVal5"))
        self.gridLayout.addWidget(self.taurusLabelVal5, 4, 2, 1, 1)
        self.taurusLabelVal6 = TaurusLabel(Form)
        self.taurusLabelVal6.setObjectName(_fromUtf8("taurusLabelVal6"))
        self.gridLayout.addWidget(self.taurusLabelVal6, 5, 2, 1, 1)
        self.taurusLabelVal7 = TaurusLabel(Form)
        self.taurusLabelVal7.setObjectName(_fromUtf8("taurusLabelVal7"))
        self.gridLayout.addWidget(self.taurusLabelVal7, 6, 2, 1, 1)
        self.taurusLabelVal8 = TaurusLabel(Form)
        self.taurusLabelVal8.setObjectName(_fromUtf8("taurusLabelVal8"))
        self.gridLayout.addWidget(self.taurusLabelVal8, 7, 2, 1, 1)
        self.configMeasurement4 = TaurusValueComboBox(Form)
        self.configMeasurement4.setAutoApply(True)
        self.configMeasurement4.setObjectName(_fromUtf8("configMeasurement4"))
        self.gridLayout.addWidget(self.configMeasurement4, 3, 1, 1, 1)
        self.configMeasurement7 = TaurusValueComboBox(Form)
        self.configMeasurement7.setAutoApply(True)
        self.configMeasurement7.setObjectName(_fromUtf8("configMeasurement7"))
        self.gridLayout.addWidget(self.configMeasurement7, 6, 1, 1, 1)
        self.configMeasurement3 = TaurusValueComboBox(Form)
        self.configMeasurement3.setAutoApply(True)
        self.configMeasurement3.setObjectName(_fromUtf8("configMeasurement3"))
        self.gridLayout.addWidget(self.configMeasurement3, 2, 1, 1, 1)
        self.configMeasurement5 = TaurusValueComboBox(Form)
        self.configMeasurement5.setAutoApply(True)
        self.configMeasurement5.setObjectName(_fromUtf8("configMeasurement5"))
        self.gridLayout.addWidget(self.configMeasurement5, 4, 1, 1, 1)
        self.sourceMeasurement5 = TaurusValueComboBox(Form)
        self.sourceMeasurement5.setAutoApply(True)
        self.sourceMeasurement5.setObjectName(_fromUtf8("sourceMeasurement5"))
        self.gridLayout.addWidget(self.sourceMeasurement5, 4, 0, 1, 1)
        self.sourceMeasurement6 = TaurusValueComboBox(Form)
        self.sourceMeasurement6.setAutoApply(True)
        self.sourceMeasurement6.setObjectName(_fromUtf8("sourceMeasurement6"))
        self.gridLayout.addWidget(self.sourceMeasurement6, 5, 0, 1, 1)
        self.configMeasurement8 = TaurusValueComboBox(Form)
        self.configMeasurement8.setAutoApply(True)
        self.configMeasurement8.setObjectName(_fromUtf8("configMeasurement8"))
        self.gridLayout.addWidget(self.configMeasurement8, 7, 1, 1, 1)
        self.sourceMeasurement7 = TaurusValueComboBox(Form)
        self.sourceMeasurement7.setAutoApply(True)
        self.sourceMeasurement7.setObjectName(_fromUtf8("sourceMeasurement7"))
        self.gridLayout.addWidget(self.sourceMeasurement7, 6, 0, 1, 1)
        self.sourceMeasurement8 = TaurusValueComboBox(Form)
        self.sourceMeasurement8.setAutoApply(True)
        self.sourceMeasurement8.setObjectName(_fromUtf8("sourceMeasurement8"))
        self.gridLayout.addWidget(self.sourceMeasurement8, 7, 0, 1, 1)
        self.sourceMeasurement3 = TaurusValueComboBox(Form)
        self.sourceMeasurement3.setAutoApply(True)
        self.sourceMeasurement3.setObjectName(_fromUtf8("sourceMeasurement3"))
        self.gridLayout.addWidget(self.sourceMeasurement3, 2, 0, 1, 1)
        self.sourceMeasurement1 = TaurusValueComboBox(Form)
        self.sourceMeasurement1.setAutoApply(True)
        self.sourceMeasurement1.setObjectName(_fromUtf8("sourceMeasurement1"))
        self.gridLayout.addWidget(self.sourceMeasurement1, 0, 0, 1, 1)
        self.sourceMeasurement4 = TaurusValueComboBox(Form)
        self.sourceMeasurement4.setAutoApply(True)
        self.sourceMeasurement4.setObjectName(_fromUtf8("sourceMeasurement4"))
        self.gridLayout.addWidget(self.sourceMeasurement4, 3, 0, 1, 1)
        self.configMeasurement1 = TaurusValueComboBox(Form)
        self.configMeasurement1.setAutoApply(True)
        self.configMeasurement1.setObjectName(_fromUtf8("configMeasurement1"))
        self.gridLayout.addWidget(self.configMeasurement1, 0, 1, 1, 1)
        self.configMeasurement6 = TaurusValueComboBox(Form)
        self.configMeasurement6.setAutoApply(True)
        self.configMeasurement6.setObjectName(_fromUtf8("configMeasurement6"))
        self.gridLayout.addWidget(self.configMeasurement6, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.input import TaurusValueComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

