# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measurements.ui'
#
# Created: Wed Feb 12 16:49:35 2014
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
        Form.resize(855, 479)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelMeas1 = QtGui.QLabel(Form)
        self.labelMeas1.setObjectName(_fromUtf8("labelMeas1"))
        self.gridLayout.addWidget(self.labelMeas1, 0, 0, 1, 1)
        self.taurusAttrListComboBox_1 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_1.setObjectName(_fromUtf8("taurusAttrListComboBox_1"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_1, 0, 1, 1, 1)
        self.labelRes1 = QtGui.QLabel(Form)
        self.labelRes1.setObjectName(_fromUtf8("labelRes1"))
        self.gridLayout.addWidget(self.labelRes1, 0, 2, 1, 1)
        self.taurusLabelVal1 = TaurusLabel(Form)
        self.taurusLabelVal1.setObjectName(_fromUtf8("taurusLabelVal1"))
        self.gridLayout.addWidget(self.taurusLabelVal1, 0, 3, 1, 1)
        self.labelMeas2 = QtGui.QLabel(Form)
        self.labelMeas2.setObjectName(_fromUtf8("labelMeas2"))
        self.gridLayout.addWidget(self.labelMeas2, 1, 0, 1, 1)
        self.taurusAttrListComboBox_2 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_2.setObjectName(_fromUtf8("taurusAttrListComboBox_2"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_2, 1, 1, 1, 1)
        self.labelRes2 = QtGui.QLabel(Form)
        self.labelRes2.setObjectName(_fromUtf8("labelRes2"))
        self.gridLayout.addWidget(self.labelRes2, 1, 2, 1, 1)
        self.taurusLabelVal2 = TaurusLabel(Form)
        self.taurusLabelVal2.setObjectName(_fromUtf8("taurusLabelVal2"))
        self.gridLayout.addWidget(self.taurusLabelVal2, 1, 3, 1, 1)
        self.labelMeas3 = QtGui.QLabel(Form)
        self.labelMeas3.setObjectName(_fromUtf8("labelMeas3"))
        self.gridLayout.addWidget(self.labelMeas3, 2, 0, 1, 1)
        self.taurusAttrListComboBox_3 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_3.setObjectName(_fromUtf8("taurusAttrListComboBox_3"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_3, 2, 1, 1, 1)
        self.labelRes3 = QtGui.QLabel(Form)
        self.labelRes3.setObjectName(_fromUtf8("labelRes3"))
        self.gridLayout.addWidget(self.labelRes3, 2, 2, 1, 1)
        self.taurusLabelVal3 = TaurusLabel(Form)
        self.taurusLabelVal3.setObjectName(_fromUtf8("taurusLabelVal3"))
        self.gridLayout.addWidget(self.taurusLabelVal3, 2, 3, 1, 1)
        self.labelMeas4 = QtGui.QLabel(Form)
        self.labelMeas4.setObjectName(_fromUtf8("labelMeas4"))
        self.gridLayout.addWidget(self.labelMeas4, 3, 0, 1, 1)
        self.taurusAttrListComboBox_4 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_4.setObjectName(_fromUtf8("taurusAttrListComboBox_4"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_4, 3, 1, 1, 1)
        self.labelRes4 = QtGui.QLabel(Form)
        self.labelRes4.setObjectName(_fromUtf8("labelRes4"))
        self.gridLayout.addWidget(self.labelRes4, 3, 2, 1, 1)
        self.taurusLabelVal4 = TaurusLabel(Form)
        self.taurusLabelVal4.setObjectName(_fromUtf8("taurusLabelVal4"))
        self.gridLayout.addWidget(self.taurusLabelVal4, 3, 3, 1, 1)
        self.labelMeas5 = QtGui.QLabel(Form)
        self.labelMeas5.setObjectName(_fromUtf8("labelMeas5"))
        self.gridLayout.addWidget(self.labelMeas5, 4, 0, 1, 1)
        self.taurusAttrListComboBox_5 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_5.setObjectName(_fromUtf8("taurusAttrListComboBox_5"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_5, 4, 1, 1, 1)
        self.labelRes5 = QtGui.QLabel(Form)
        self.labelRes5.setObjectName(_fromUtf8("labelRes5"))
        self.gridLayout.addWidget(self.labelRes5, 4, 2, 1, 1)
        self.taurusLabelVal5 = TaurusLabel(Form)
        self.taurusLabelVal5.setObjectName(_fromUtf8("taurusLabelVal5"))
        self.gridLayout.addWidget(self.taurusLabelVal5, 4, 3, 1, 1)
        self.labelMeas6 = QtGui.QLabel(Form)
        self.labelMeas6.setObjectName(_fromUtf8("labelMeas6"))
        self.gridLayout.addWidget(self.labelMeas6, 5, 0, 1, 1)
        self.taurusAttrListComboBox_6 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_6.setObjectName(_fromUtf8("taurusAttrListComboBox_6"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_6, 5, 1, 1, 1)
        self.labelRes6 = QtGui.QLabel(Form)
        self.labelRes6.setObjectName(_fromUtf8("labelRes6"))
        self.gridLayout.addWidget(self.labelRes6, 5, 2, 1, 1)
        self.taurusLabelVal6 = TaurusLabel(Form)
        self.taurusLabelVal6.setObjectName(_fromUtf8("taurusLabelVal6"))
        self.gridLayout.addWidget(self.taurusLabelVal6, 5, 3, 1, 1)
        self.labelMeas7 = QtGui.QLabel(Form)
        self.labelMeas7.setObjectName(_fromUtf8("labelMeas7"))
        self.gridLayout.addWidget(self.labelMeas7, 6, 0, 1, 1)
        self.taurusAttrListComboBox_7 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_7.setObjectName(_fromUtf8("taurusAttrListComboBox_7"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_7, 6, 1, 1, 1)
        self.labelRes7 = QtGui.QLabel(Form)
        self.labelRes7.setObjectName(_fromUtf8("labelRes7"))
        self.gridLayout.addWidget(self.labelRes7, 6, 2, 1, 1)
        self.taurusLabelVal7 = TaurusLabel(Form)
        self.taurusLabelVal7.setObjectName(_fromUtf8("taurusLabelVal7"))
        self.gridLayout.addWidget(self.taurusLabelVal7, 6, 3, 1, 1)
        self.labelMeas8 = QtGui.QLabel(Form)
        self.labelMeas8.setObjectName(_fromUtf8("labelMeas8"))
        self.gridLayout.addWidget(self.labelMeas8, 7, 0, 1, 1)
        self.taurusAttrListComboBox_8 = TaurusAttrListComboBox(Form)
        self.taurusAttrListComboBox_8.setObjectName(_fromUtf8("taurusAttrListComboBox_8"))
        self.gridLayout.addWidget(self.taurusAttrListComboBox_8, 7, 1, 1, 1)
        self.labelRes8 = QtGui.QLabel(Form)
        self.labelRes8.setObjectName(_fromUtf8("labelRes8"))
        self.gridLayout.addWidget(self.labelRes8, 7, 2, 1, 1)
        self.taurusLabelVal8 = TaurusLabel(Form)
        self.taurusLabelVal8.setObjectName(_fromUtf8("taurusLabelVal8"))
        self.gridLayout.addWidget(self.taurusLabelVal8, 7, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.labelMeas1.setText(_translate("Form", "Measurement 1", None))
        self.labelRes1.setText(_translate("Form", "Result", None))
        self.labelMeas2.setText(_translate("Form", "Measurement 2", None))
        self.labelRes2.setText(_translate("Form", "Result", None))
        self.labelMeas3.setText(_translate("Form", "Measurement 3", None))
        self.labelRes3.setText(_translate("Form", "Result", None))
        self.labelMeas4.setText(_translate("Form", "Measurement 4", None))
        self.labelRes4.setText(_translate("Form", "Result", None))
        self.labelMeas5.setText(_translate("Form", "Measurement 5", None))
        self.labelRes5.setText(_translate("Form", "Result", None))
        self.labelMeas6.setText(_translate("Form", "Measurement 6", None))
        self.labelRes6.setText(_translate("Form", "Result", None))
        self.labelMeas7.setText(_translate("Form", "Measurement 7", None))
        self.labelRes7.setText(_translate("Form", "Result", None))
        self.labelMeas8.setText(_translate("Form", "Measurement 8", None))
        self.labelRes8.setText(_translate("Form", "Result", None))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.input import TaurusAttrListComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

