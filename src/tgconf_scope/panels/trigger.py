#!/usr/bin/env python

__docformat__ = 'restructuredtext'

import sys
from PyQt4 import QtCore, QtGui
from ui_trigger import Ui_Trigger
from taurus.qt.qtgui.panel import TaurusWidget
import taurus
import PyTango

class Trigger(TaurusWidget):

    state = None
    tango_scope = None

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_Trigger()
        self._ui.setupUi(self)

    def setModel(self, model):

        print "IN SET MODEL TRIGGER PANEL"
        #Get the model from the scope chooser then set attributes here
        attributes = [model+"/Trig1Source",
                      model+"/Trig1Mode",
                      model+"/TrigLevel",
                      ]

        self._ui.taurusForm.setModel(attributes)


def main():
    app = QtGui.QApplication(sys.argv)
    w = Trigger()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
