#!/usr/bin/env python

__docformat__ = 'restructuredtext'

import sys
from PyQt4 import QtCore, QtGui
from ui_display import Ui_Display
from taurus.qt.qtgui.panel import TaurusWidget
import taurus
import PyTango

class Scales(TaurusWidget):

    state = None
    tango_scope = None

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)

        self._ui = Ui_Display()
        self._ui.setupUi(self)

    def setModel(self, model):

        #Get the model from the scope chooser then set attributes here
        attributes = [model+"/PositionCh1",
                      model+"/PositionCh2",
                      model+"/PositionCh3",
                      model+"/PositionCh4",
                      model+"/VRangeCh1",
                      model+"/VRangeCh2",
                      model+"/VRangeCh3",
                      model+"/VRangeCh4",
                      model+"/HRange",
                      ]

        self._ui.taurusForm.setModel(attributes)



def main():
    app = QtGui.QApplication(sys.argv)
    w = Scales()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
