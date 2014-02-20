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

import re
import sys
import traceback
import PyTango

from PyQt4 import QtCore, QtGui
from taurus.qt.qtgui.container import TaurusWidget
from ui_measurements import Ui_Form
from AllowedMeasurements import ALLOWED_MEASUREMENTS, ALLOWED_SOURCES


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
        modelList = [(self.ui.configMeasurement1, model[0]),
                     (self.ui.configMeasurement2, model[1]),
                     (self.ui.configMeasurement3, model[2]),
                     (self.ui.configMeasurement4, model[3]),
                     (self.ui.configMeasurement5, model[4]),
                     (self.ui.configMeasurement6, model[5]),
                     (self.ui.configMeasurement7, model[6]),
                     (self.ui.configMeasurement8, model[7]),
                     (self.ui.taurusLabelVal1, model[8]),
                     (self.ui.taurusLabelVal2, model[9]),
                     (self.ui.taurusLabelVal3, model[10]),
                     (self.ui.taurusLabelVal4, model[11]),
                     (self.ui.taurusLabelVal5, model[12]),
                     (self.ui.taurusLabelVal6, model[13]),
                     (self.ui.taurusLabelVal7, model[14]),
                     (self.ui.taurusLabelVal8, model[15]),
                     (self.ui.sourceMeasurement1, model[16]),
                     (self.ui.sourceMeasurement2, model[17]),
                     (self.ui.sourceMeasurement3, model[18]),
                     (self.ui.sourceMeasurement4, model[19]),
                     (self.ui.sourceMeasurement5, model[20]),
                     (self.ui.sourceMeasurement6, model[21]),
                     (self.ui.sourceMeasurement7, model[22]),
                     (self.ui.sourceMeasurement8, model[23]),
                     ]

        for widget, modelToSet in modelList:
            widget.setModel(modelToSet)

    @alert_problems
    def fillComboBoxes(self):
        self.ui.configMeasurement1.addValueNames(ALLOWED_MEASUREMENTS)
        self.ui.configMeasurement2.addValueNames(ALLOWED_MEASUREMENTS)
        self.ui.configMeasurement3.addValueNames(ALLOWED_MEASUREMENTS)
        self.ui.configMeasurement4.addValueNames(ALLOWED_MEASUREMENTS)
        self.ui.configMeasurement5.addValueNames(ALLOWED_MEASUREMENTS)
        self.ui.configMeasurement6.addValueNames(ALLOWED_MEASUREMENTS)
        self.ui.configMeasurement7.addValueNames(ALLOWED_MEASUREMENTS)
        self.ui.configMeasurement8.addValueNames(ALLOWED_MEASUREMENTS)

        self.ui.sourceMeasurement1.addValueNames(ALLOWED_SOURCES)
        self.ui.sourceMeasurement2.addValueNames(ALLOWED_SOURCES)
        self.ui.sourceMeasurement3.addValueNames(ALLOWED_SOURCES)
        self.ui.sourceMeasurement4.addValueNames(ALLOWED_SOURCES)
        self.ui.sourceMeasurement5.addValueNames(ALLOWED_SOURCES)
        self.ui.sourceMeasurement6.addValueNames(ALLOWED_SOURCES)
        self.ui.sourceMeasurement7.addValueNames(ALLOWED_SOURCES)
        self.ui.sourceMeasurement8.addValueNames(ALLOWED_SOURCES)

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
