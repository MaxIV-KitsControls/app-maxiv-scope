#!/usr/bin/env python

__docformat__ = 'restructuredtext'

import sys
from PyQt4 import QtCore, QtGui
from ui_channels import Ui_Channels
from taurus.qt.qtgui.panel import TaurusWidget
import taurus
import PyTango

class Channels(TaurusWidget):

    state = None
    tango_scope = None

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_Channels()
        self._ui.setupUi(self)

    def setModel(self, model):

        #Get the model from the scope chooser then set attributes here
        attributes = [model+"/CouplingCh1",
                      model+"/CouplingCh2",
                      model+"/CouplingCh3",
                      model+"/CouplingCh4",
                      ]

        self._ui.taurusForm.setModel(attributes)


def main():
    app = QtGui.QApplication(sys.argv)
    w = Channels()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
