#!/usr/bin/env python

__docformat__ = 'restructuredtext'

import sys
from PyQt4 import QtCore, QtGui
from ui_control import Ui_Control
from taurus.qt.qtgui.panel import TaurusWidget
import taurus
import PyTango

class Control(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_Control()
        self._ui.setupUi(self)

        self._ui.startButton.setUseParentModel(False)
        self._ui.startButton.setCommand('Start') #this is the Tango device command
        self._ui.startButton.setCustomText('Start')

        self._ui.golocalButton.setUseParentModel(False)
        self._ui.golocalButton.setCommand('Standby') #this is the Tango device command
        self._ui.golocalButton.setCustomText('Standby')

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'modulatorctrl'
        ret['group'] = 'Taurus Containers'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret
    
    def setModel(self, model):

        #Model is a list of dev names and attribues passed from the config file

        #set attributes in the form
        self._ui.taurusForm.setModel(model)

        #set the buttons - just need device name
        devname = (model[0].rsplit('/', 1))[0]

        self._ui.startButton.setModel('scope/rohdeschwarz/rto-1024')
        self._ui.golocalButton.setModel(devname)
        #print 'PJB *************************', self._ui.golocalButton.getModelObj(), self._ui.golocalButton.UseParentModel

        tango_scope = taurus.Device(devname)
        print 'PJB ------- ',  tango_scope.State()
        #set button labels and commands according to status!
        
        self.setControlButtons(tango_scope.State())

        # Add event listeners to monitor relevant Taurus attribute changes
        #taurus.Attribute(tango_scope+'/State').addListener(self.stateListener)

   # def stateListener(src, evt_type, attr_val):
        #if isinstance(src,taurus.core.tango.tangoattribute.TangoAttribute) and evt_type==PyTango.EventType.CHANGE_EVENT:
        #pass

    def setControlButtons(self, state):
        if(state in [PyTango.DevState.RUNNING]):
               print 'PJB -------  running ---- ',  state
               self._ui.startButton.setCustomText('Stop')
               self._ui.startButton.setCommand('Stop')
        if(state in [PyTango.DevState.ON]):
               print 'PJB -------  on ---- ',  state
               self._ui.startButton.setCustomText('Start')
               self._ui.startButton.setCommand('Start')


def main():
    app = QtGui.QApplication(sys.argv)
    w = Control()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
