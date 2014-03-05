# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measurements.ui'
#
# Created: Thu Feb 27 10:58:18 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(855, 324)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusLabelVal1 = TaurusLabel(Form)
        self.taurusLabelVal1.setObjectName(_fromUtf8("taurusLabelVal1"))
        self.gridLayout.addWidget(self.taurusLabelVal1, 1, 2, 1, 1)
        self.sourceMeasurement2 = TaurusValueComboBox(Form)
        self.sourceMeasurement2.setAutoApply(True)
        self.sourceMeasurement2.setObjectName(_fromUtf8("sourceMeasurement2"))
        self.gridLayout.addWidget(self.sourceMeasurement2, 2, 0, 1, 1)
        self.configMeasurement4 = TaurusValueComboBox(Form)
        self.configMeasurement4.setAutoApply(True)
        self.configMeasurement4.setObjectName(_fromUtf8("configMeasurement4"))
        self.gridLayout.addWidget(self.configMeasurement4, 4, 1, 1, 1)
        self.configMeasurement2 = TaurusValueComboBox(Form)
        self.configMeasurement2.setAutoApply(True)
        self.configMeasurement2.setObjectName(_fromUtf8("configMeasurement2"))
        self.gridLayout.addWidget(self.configMeasurement2, 2, 1, 1, 1)
        self.taurusLabelVal2 = TaurusLabel(Form)
        self.taurusLabelVal2.setObjectName(_fromUtf8("taurusLabelVal2"))
        self.gridLayout.addWidget(self.taurusLabelVal2, 2, 2, 1, 1)
        self.sourceMeasurement3 = TaurusValueComboBox(Form)
        self.sourceMeasurement3.setAutoApply(True)
        self.sourceMeasurement3.setObjectName(_fromUtf8("sourceMeasurement3"))
        self.gridLayout.addWidget(self.sourceMeasurement3, 3, 0, 1, 1)
        self.configMeasurement3 = TaurusValueComboBox(Form)
        self.configMeasurement3.setAutoApply(True)
        self.configMeasurement3.setObjectName(_fromUtf8("configMeasurement3"))
        self.gridLayout.addWidget(self.configMeasurement3, 3, 1, 1, 1)
        self.taurusLabelVal3 = TaurusLabel(Form)
        self.taurusLabelVal3.setObjectName(_fromUtf8("taurusLabelVal3"))
        self.gridLayout.addWidget(self.taurusLabelVal3, 3, 2, 1, 1)
        self.sourceMeasurement4 = TaurusValueComboBox(Form)
        self.sourceMeasurement4.setAutoApply(True)
        self.sourceMeasurement4.setObjectName(_fromUtf8("sourceMeasurement4"))
        self.gridLayout.addWidget(self.sourceMeasurement4, 4, 0, 1, 1)
        self.taurusLabelVal4 = TaurusLabel(Form)
        self.taurusLabelVal4.setObjectName(_fromUtf8("taurusLabelVal4"))
        self.gridLayout.addWidget(self.taurusLabelVal4, 4, 2, 1, 1)
        self.sourceMeasurement5 = TaurusValueComboBox(Form)
        self.sourceMeasurement5.setAutoApply(True)
        self.sourceMeasurement5.setObjectName(_fromUtf8("sourceMeasurement5"))
        self.gridLayout.addWidget(self.sourceMeasurement5, 5, 0, 1, 1)
        self.configMeasurement5 = TaurusValueComboBox(Form)
        self.configMeasurement5.setAutoApply(True)
        self.configMeasurement5.setObjectName(_fromUtf8("configMeasurement5"))
        self.gridLayout.addWidget(self.configMeasurement5, 5, 1, 1, 1)
        self.taurusLabelVal5 = TaurusLabel(Form)
        self.taurusLabelVal5.setObjectName(_fromUtf8("taurusLabelVal5"))
        self.gridLayout.addWidget(self.taurusLabelVal5, 5, 2, 1, 1)
        self.sourceMeasurement6 = TaurusValueComboBox(Form)
        self.sourceMeasurement6.setAutoApply(True)
        self.sourceMeasurement6.setObjectName(_fromUtf8("sourceMeasurement6"))
        self.gridLayout.addWidget(self.sourceMeasurement6, 6, 0, 1, 1)
        self.configMeasurement6 = TaurusValueComboBox(Form)
        self.configMeasurement6.setAutoApply(True)
        self.configMeasurement6.setObjectName(_fromUtf8("configMeasurement6"))
        self.gridLayout.addWidget(self.configMeasurement6, 6, 1, 1, 1)
        self.taurusLabelVal6 = TaurusLabel(Form)
        self.taurusLabelVal6.setObjectName(_fromUtf8("taurusLabelVal6"))
        self.gridLayout.addWidget(self.taurusLabelVal6, 6, 2, 1, 1)
        self.sourceMeasurement7 = TaurusValueComboBox(Form)
        self.sourceMeasurement7.setAutoApply(True)
        self.sourceMeasurement7.setObjectName(_fromUtf8("sourceMeasurement7"))
        self.gridLayout.addWidget(self.sourceMeasurement7, 7, 0, 1, 1)
        self.configMeasurement7 = TaurusValueComboBox(Form)
        self.configMeasurement7.setAutoApply(True)
        self.configMeasurement7.setObjectName(_fromUtf8("configMeasurement7"))
        self.gridLayout.addWidget(self.configMeasurement7, 7, 1, 1, 1)
        self.taurusLabelVal7 = TaurusLabel(Form)
        self.taurusLabelVal7.setObjectName(_fromUtf8("taurusLabelVal7"))
        self.gridLayout.addWidget(self.taurusLabelVal7, 7, 2, 1, 1)
        self.sourceMeasurement8 = TaurusValueComboBox(Form)
        self.sourceMeasurement8.setAutoApply(True)
        self.sourceMeasurement8.setObjectName(_fromUtf8("sourceMeasurement8"))
        self.gridLayout.addWidget(self.sourceMeasurement8, 8, 0, 1, 1)
        self.configMeasurement8 = TaurusValueComboBox(Form)
        self.configMeasurement8.setAutoApply(True)
        self.configMeasurement8.setObjectName(_fromUtf8("configMeasurement8"))
        self.gridLayout.addWidget(self.configMeasurement8, 8, 1, 1, 1)
        self.taurusLabelVal8 = TaurusLabel(Form)
        self.taurusLabelVal8.setObjectName(_fromUtf8("taurusLabelVal8"))
        self.gridLayout.addWidget(self.taurusLabelVal8, 8, 2, 1, 1)
        self.sourceMeasurement1 = TaurusValueComboBox(Form)
        self.sourceMeasurement1.setAutoApply(True)
        self.sourceMeasurement1.setObjectName(_fromUtf8("sourceMeasurement1"))
        self.gridLayout.addWidget(self.sourceMeasurement1, 1, 0, 1, 1)
        self.configMeasurement1 = TaurusValueComboBox(Form)
        self.configMeasurement1.setAutoApply(True)
        self.configMeasurement1.setObjectName(_fromUtf8("configMeasurement1"))
        self.gridLayout.addWidget(self.configMeasurement1, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.taurusValueCheckBox = TaurusValueCheckBox(self.groupBox)
        self.taurusValueCheckBox.setAutoApply(True)
        self.taurusValueCheckBox.setObjectName(_fromUtf8("taurusValueCheckBox"))
        self.horizontalLayout.addWidget(self.taurusValueCheckBox)
        self.cursorMinValEdit = TaurusValueLineEdit(self.groupBox)
        self.cursorMinValEdit.setAutoApply(True)
        self.cursorMinValEdit.setObjectName(_fromUtf8("cursorMinValEdit"))
        self.horizontalLayout.addWidget(self.cursorMinValEdit)
        self.cursorMaxValEdit = TaurusValueLineEdit(self.groupBox)
        self.cursorMaxValEdit.setAutoApply(True)
        self.cursorMaxValEdit.setObjectName(_fromUtf8("cursorMaxValEdit"))
        self.horizontalLayout.addWidget(self.cursorMaxValEdit)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Cursor gating", None))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.input import TaurusValueComboBox, TaurusValueLineEdit, TaurusValueCheckBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

