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

from PyQt4 import QtCore, QtGui, Qt
from taurus.qt.qtgui.container import TaurusWidget
from ui_testplot import Ui_TestPlot
import PyQt4.Qwt5 as Qwt
from PyQt4.Qt import *
from PyQt4.Qwt5 import *
import taurus

class TestPlot(TaurusWidget):

    trigger = QtCore.pyqtSignal()

    def __init__(self, param=None, parent=None, desigMode=False):
        TaurusWidget.__init__(self, parent, desigMode)
        self.ui = Ui_TestPlot()
        self.ui.setupUi(self)
    
        self.hscale=1.0
        self.yscale=1.0
        
        self.devname=""
        self.tango_scope=None

        #peak marker
        self.peakMarker = QwtPlotMarker()
        self.peakMarker.setLineStyle(QwtPlotMarker.HLine)
        #self.peakMarker.setLabelAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.peakMarker.setLinePen(QPen(Qt.red, 2, Qt.DashDotLine))
        self.peakMarker.attach(self.ui.taurusPlot)
        #
        #time marker 1
        self.timeMarker = QwtPlotMarker()
        self.timeMarker.setLineStyle(QwtPlotMarker.VLine)
        #self.timeMarker.setLabelAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.timeMarker.setLinePen(QPen(Qt.green, 2, Qt.DashDotLine))
        #self.timeMarker.setXValue(-hscale/10.0)
        self.timeMarker.attach(self.ui.taurusPlot)
        #time marker 2
        self.timeMarker2 = QwtPlotMarker()
        self.timeMarker2.setLineStyle(QwtPlotMarker.VLine)
        self.timeMarker2.setLinePen(QPen(Qt.green, 2, Qt.DashDotLine))
        #self.timeMarker2.setXValue(hscale/10.0)
        self.timeMarker2.attach(self.ui.taurusPlot)
        #
        self.plotPicker = Qwt.QwtPlotPicker(Qwt.QwtPlot.xBottom, Qwt.QwtPlot.yLeft, Qwt.QwtPicker.PointSelection, Qwt.QwtPlotPicker.NoRubberBand, Qwt.QwtPicker.AlwaysOff, self.ui.taurusPlot.canvas())
        self.connect(self.plotPicker,  QtCore.SIGNAL('moved(const QPoint &)'), self.moveCursor)
        self.trigger.connect(self.changeScale)



    def setModel(self, device_name):
        """ Set the model for the widget.
        @param model: list of attributes models
        """

        #device_name is a string containing the device name
        model=[
            str(device_name)+'/TimeScale|'+str(device_name)+'/WaveformDataCh1',
            str(device_name)+'/TimeScale|'+str(device_name)+'/WaveformDataCh2',
            str(device_name)+'/TimeScale|'+str(device_name)+'/WaveformDataCh3',
            str(device_name)+'/TimeScale|'+str(device_name)+'/WaveformDataCh4',
            ]

        #set model for the plot
        self.ui.taurusPlot.setModel(model)

        self.devname = str(device_name)
        self.tango_scope = taurus.Device(self.devname)
        #print "in testplot devname ", self.devname,    
        #self.hscale = (taurus.Attribute(self.devname+'/HScale').getValueObj())

        try:
            self.hscale =  self.tango_scope.HScale
            #yscales =[self.tango_scope.VScaleCh1,
            #          self.tango_scope.VScaleCh2,
            #          self.tango_scope.VScaleCh3,
            #          self.tango_scope.VScaleCh4]
            #self.yscale = max(yscales)
        except:    
            print "cannot connect plot to scope"

        self.timeMarker.setXValue(-self.hscale/100.0)
        self.timeMarker2.setXValue(self.hscale/100.0)
     
        #print "y scale ", self.yscale*5.0
        self.ui.taurusPlot.setAxisScale(self.ui.taurusPlot.yLeft, -self.yscale*5.0,  self.yscale*5.0)
        self.ui.taurusPlot.setAxisScale(self.ui.taurusPlot.yRight, -self.yscale*5.0,  self.yscale*5.0)

        taurus.Attribute(str(device_name)+'/TimeScale').addListener(self.stateListener)
        #taurus.Attribute(str(device_name)+'/VScaleCh1').addListener(self.stateListener)
        #taurus.Attribute(str(device_name)+'/VScaleCh2').addListener(self.stateListener)
        #taurus.Attribute(str(device_name)+'/VScaleCh3').addListener(self.stateListener)
        #taurus.Attribute(str(device_name)+'/VScaleCh4').addListener(self.stateListener)


    #PJB not used for vscale in v2.3.3 since set scale always to pm5 and receive unscaled waveform data
    def stateListener(self, src, evt_type, attr_val):
        if isinstance(src,taurus.core.tango.tangoattribute.TangoAttribute) and evt_type==PyTango.EventType.CHANGE_EVENT:
        #if evt_type==PyTango.EventType.QUALITY_EVENT:
        #if isinstance(src,taurus.core.tango.tangoattribute.TangoAttribute):
            #yscales =[self.tango_scope.VScaleCh1,
            #          self.tango_scope.VScaleCh2,
            #          self.tango_scope.VScaleCh3,
            #          self.tango_scope.VScaleCh4]
            #self.yscale = max(yscales)
            #self.hscale =self.tango_scope.TimeScale1,
            #print "new scale ", self.yscale
            self.trigger.emit()

    def changeScale(self):
        self.ui.taurusPlot.setAxisScale(Qwt.QwtPlot.yLeft, -self.yscale*5.0,  self.yscale*5.0)
        
    def moveCursor(self, point):

        #print self.timeMarker.xValue()
        #print self.timeMarker2.xValue()

        pickX = (self.ui.taurusPlot.invTransform(Qwt.QwtPlot.xBottom, point.x()))
        pickY = (self.ui.taurusPlot.invTransform(Qwt.QwtPlot.yLeft, point.y()))
        
        #get the distance to the marker
        Ydistance = pickY - self.peakMarker.yValue()
        Xdistance = pickX - self.timeMarker.xValue()
        Xdistance2 = pickX - self.timeMarker2.xValue()
        
        #10 percent y scale NEED TO GET VSCALE FROM THE SETTING IN THE DEVICE
        granularityY= self.yscale/ 3.0
        granularityX= self.hscale / 2.0

        #print " x -- y     distance ", pickX, pickY, Xdistance, granularityX

        #markerSelected = self.closestMarker(pickX,pickY)
        if abs(Ydistance) < granularityY:
            self.peakMarker.setValue(0.0, self.ui.taurusPlot.invTransform(Qwt.QwtPlot.yLeft, point.y()))
            self.ui.taurusPlot.replot()
        if abs(Xdistance) < granularityX and abs(Xdistance) < abs(Xdistance2):
            self.timeMarker.setValue(self.ui.taurusPlot.invTransform(Qwt.QwtPlot.xBottom, point.x()), 0.0)
            self.ui.taurusPlot.replot()
        if abs(Xdistance2) < granularityX and abs(Xdistance2) < abs(Xdistance):
            self.timeMarker2.setValue(self.ui.taurusPlot.invTransform(Qwt.QwtPlot.xBottom, point.x()), 0.0)
            self.ui.taurusPlot.replot()

        #set the line edits
        coords=""
        self.ui.taurusValueLineEditVert.setValue(self.peakMarker.yValue())
        if(self.timeMarker.xValue() < self.timeMarker2.xValue()):
            self.ui.taurusValueLineEditTimeMin.setValue(self.timeMarker.xValue())
            self.ui.taurusValueLineEditTimeMax.setValue(self.timeMarker2.xValue())
            coords = str(self.timeMarker.xValue())+":"+str(self.timeMarker2.xValue())
        else:
            self.ui.taurusValueLineEditTimeMin.setValue(self.timeMarker2.xValue())
            self.ui.taurusValueLineEditTimeMax.setValue(self.timeMarker.xValue())
            coords =  str(self.timeMarker2.xValue())+":"+str(self.timeMarker.xValue())

        self.emit(SIGNAL("sendPoint(QString)"), coords)

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = TestPlot()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
