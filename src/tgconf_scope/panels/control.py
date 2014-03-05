#!/usr/bin/env python

__docformat__ = 'restructuredtext'

import sys
from PyQt4 import QtCore, QtGui
from ui_control import Ui_Control
from taurus.qt.qtgui.panel import TaurusWidget
import taurus
import PyTango

class Control(TaurusWidget):

    state = None
    tango_scope = None

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_Control()
        self._ui.setupUi(self)

        self._ui.startButton.setUseParentModel(False)
        self._ui.golocalButton.setUseParentModel(False)

        #self.connect(self._ui.startButton, QtCore.SIGNAL('clicked()'), self.setControlButtons)
        #self.connect(self._ui.golocalButton, QtCore.SIGNAL('clicked()'), self.setControlButtons)


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

        self._ui.startButton.setModel(devname)
        self._ui.golocalButton.setModel(devname)
        #print 'PJB *************************', self._ui.golocalButton.getModelObj(), self._ui.golocalButton.UseParentModel

        self.tango_scope = taurus.Device(devname)
        self.state = self.tango_scope.State()
        #print 'PJB ------- ',  self.state

        #set button labels and commands according to status!
        self.setControlButtons()

        # Add event listeners to monitor relevant Taurus attribute changes
        # PJB can do it like this to check change of state in the device, with a listener below.
        # However, this requires the attribute to be polled. Can also just do it in Qt with a signal
        taurus.Attribute(devname+'/State').addListener(self.stateListener)

    def setControlButtons(self):
        #print "-----------------clicked "

        if(self.state in [PyTango.DevState.RUNNING]):
               #print 'PJB -------  running ---- ',  self.state
               self._ui.startButton.setCustomText('Stop')
               self._ui.startButton.setCommand('Stop')
               self._ui.golocalButton.setCustomText('Go Local')
               self._ui.golocalButton.setCommand('Standby')
        if(self.state in [PyTango.DevState.ON]):
               #print 'PJB -------  on ---- ',  self.state
               self._ui.startButton.setCustomText('Start')
               self._ui.startButton.setCommand('Start')
               self._ui.golocalButton.setCustomText('Go Local')
               self._ui.golocalButton.setCommand('Standby')
        if(self.state in [PyTango.DevState.STANDBY]):
               #print 'PJB -------  standby ---- ',  self.state
               self._ui.startButton.setCustomText('Start/Stop')
               self._ui.startButton.setCommand('Init')
               self._ui.golocalButton.setCustomText('Go Remote')
               self._ui.golocalButton.setCommand('Init')


    def stateListener(self, src, evt_type, attr_val):
        if isinstance(src,taurus.core.tango.tangoattribute.TangoAttribute) and evt_type==PyTango.EventType.CHANGE_EVENT:
            #print "*************** PJB see change ************** "
            print src,taurus.core.tango.tangoattribute.TangoAttribute,PyTango.EventType
            self.state = self.tango_scope.State()
            #print 'PJB state now ------- ',  self.state
            self.setControlButtons()

    # Rather than above, tango way, can do it with connection to above method, 
    # i.e. Qt way (and hope gui and device stay in sync)



def main():
    app = QtGui.QApplication(sys.argv)
    w = Control()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
