#!/usr/bin/env python

###############################################################################
##     DsGenerator module will generate a set of tango device servers for
##     your system. Taking as an input a file to parse.
##
##     Copyright (C) 2013  Max IV Laboratory, Lund Sweden
##
##     This program is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.
##
##     This program is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with this program.  If not, see [http://www.gnu.org/licenses/].
###############################################################################

import sys
import traceback
import PyTango

from PyQt4 import QtCore, QtGui
from taurus.qt.qtgui.container import TaurusWidget
from ui_measurements import Ui_Form
from AllowedMeasurements import ALLOWED_MEASUREMENTS_LIST


def alert_problems(meth):
    def _alert_problems(self, *args, **kws):
        try:
            return meth(self, *args, **kws)
        except PyTango.DevFailed:
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            exctype, value = sys.exc_info()[:2]
            str_aux = 'PyTango.DevFailed in ' + meth.__name__ + ':\n'
            for error in value:
                str_aux += '-----------\n'
                str_aux += "reason\t" + error.reason + "\n"
                str_aux += "description\t" + error.desc + "\n"
                str_aux += "origin\t" + error.origin + "\n"
            #error_str = 'Error in the communication with a device server!'
            QtGui.QMessageBox.critical(self, 'scope measurements', str_aux)
        except Exception, e:
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            str_aux = 'Exception in ' + meth.__name__ + ':\n'
            str_aux += str(e)+'\n'
            #error_str = 'Unexpected error !'
            QtGui.QMessageBox.critical(self, 'scope measurements', str_aux)
    return _alert_problems


class TaurusScopeMeasurements(TaurusWidget):
    def __init__(self, param=None, parent=None, desigMode=False):
        TaurusWidget.__init__(self, parent, desigMode)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.fillComboBoxes()

    @alert_problems
    def setModel(self, model):
        """ Set the model for the widget.
            @param model: list of attributes models
        """
         #deviceModel = model[0].rsplit('/', 1)[0]
        modelList = [(self.ui.taurusAttrListComboBox_1, model[0]),
                     (self.ui.taurusAttrListComboBox_2, model[1]),
                     (self.ui.taurusAttrListComboBox_3, model[2]),
                     (self.ui.taurusAttrListComboBox_4, model[3]),
                     (self.ui.taurusAttrListComboBox_5, model[4]),
                     (self.ui.taurusAttrListComboBox_6, model[5]),
                     (self.ui.taurusAttrListComboBox_7, model[6]),
                     (self.ui.taurusAttrListComboBox_8, model[7]),
                     (self.ui.taurusLabelVal1, model[8]),
                     (self.ui.taurusLabelVal2, model[9]),
                     (self.ui.taurusLabelVal3, model[10]),
                     (self.ui.taurusLabelVal4, model[11]),
                     (self.ui.taurusLabelVal5, model[12]),
                     (self.ui.taurusLabelVal6, model[13]),
                     (self.ui.taurusLabelVal7, model[14]),
                     (self.ui.taurusLabelVal8, model[15]),
                     ]
        
        for widget, modelToSet in modelList:
            print "PJB", modelToSet, type(modelToSet)
            widget.setModel(modelToSet)
            
    @alert_problems
    def fillComboBoxes(self):
        self.ui.taurusAttrListComboBox_1.addItems(ALLOWED_MEASUREMENTS_LIST)
        self.ui.taurusAttrListComboBox_2.addItems(ALLOWED_MEASUREMENTS_LIST)
        self.ui.taurusAttrListComboBox_3.addItems(ALLOWED_MEASUREMENTS_LIST)
        self.ui.taurusAttrListComboBox_4.addItems(ALLOWED_MEASUREMENTS_LIST)
        self.ui.taurusAttrListComboBox_5.addItems(ALLOWED_MEASUREMENTS_LIST)
        self.ui.taurusAttrListComboBox_6.addItems(ALLOWED_MEASUREMENTS_LIST)
        self.ui.taurusAttrListComboBox_7.addItems(ALLOWED_MEASUREMENTS_LIST)
        self.ui.taurusAttrListComboBox_8.addItems(ALLOWED_MEASUREMENTS_LIST)


def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = TaurusScopeMeasurements()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
