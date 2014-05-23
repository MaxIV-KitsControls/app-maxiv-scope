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
        attributes = [model+"/OffsetCh1",
                      model+"/OffsetCh2",
                      model+"/OffsetCh3",
                      model+"/OffsetCh4",
                      model+"/VScaleCh1",
                      model+"/VScaleCh2",
                      model+"/VScaleCh3",
                      model+"/VScaleCh4",
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
