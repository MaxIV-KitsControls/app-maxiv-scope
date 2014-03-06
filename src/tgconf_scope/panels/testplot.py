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
from taurus_scope_measurements import TaurusScopeMeasurements
import taurus

class TestPlot(TaurusWidget):
    def __init__(self, param=None, parent=None, desigMode=False):
        TaurusWidget.__init__(self, parent, desigMode)
        self.ui = Ui_TestPlot()
        self.ui.setupUi(self)
    
        self.hscale=1.0
        self.devname=""
        self.tango_scope=None
        self.measurements_panel = None

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



    def setModel(self, model):
        """ Set the model for the widget.
        @param model: list of attributes models
        """

        self.ui.taurusPlot.setModel(model)
        
        print "got measurement panel ", model[0]
        #self.measurements_panel =  model[4]

        self.devname = ((model[0].rsplit('|', 1))[0]).rsplit('/', 1)[0]
        self.tango_scope = taurus.Device(self.devname)
        #print "in testplot devname ", self.devname,    
        #self.hscale = (taurus.Attribute(self.devname+'/HScale').getValueObj())
        self.hscale =  self.tango_scope.HScale
        self.timeMarker.setXValue(-self.hscale/100.0)
        self.timeMarker2.setXValue(self.hscale/100.0)
     

        yscales =[self.tango_scope.VScaleCh1,
                  self.tango_scope.VScaleCh2,
                  self.tango_scope.VScaleCh3,
                  self.tango_scope.VScaleCh4]

        self.yscale = max(yscales)
        print "in testplot devname ", self.devname,   self.hscale, self.yscale
        

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
        granularityX= self.hscale / 8.0

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
