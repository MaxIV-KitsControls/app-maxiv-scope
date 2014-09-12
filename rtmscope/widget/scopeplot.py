"""Contain a plot widget specifically for displaying oscilloscope waveforms."""

# Imports
from taurus.qt.qtgui.panel import TaurusWidget
from taurus.qt import QtGui, QtCore
import pyqtgraph as pg
import PyTango

# Scope plot widget
class ScopePlotWidget(TaurusWidget):
    """A plot widget specifically for displaying oscilloscope waveforms."""

    # Attributes
    
    trigger = QtCore.pyqtSignal(str)
    channel_colors = ("FF0", "0F0", "F80", "44F")

    # Initialize
    
    def __init__(self, title=None, parent=None, y=False):
        """Initialize with a given title and parent widget."""
        TaurusWidget.__init__(self, parent)

        # Widget
        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.plot = pg.PlotWidget()
        layout.addWidget(self.plot)
        self.setLayout(layout)

        # Plot
        self.plotitem = self.plot.plotItem
        self.plot.showGrid(x=True, y=True)

        self.vb = self.plotitem.getViewBox()
        self.vb.setRange(yRange=(-5, 5), xRange=(-0.01, 0.01),
                         padding=0, disableAutoRange=True)
        self.vb.setMouseEnabled(x=False, y=False)
        
        # Axes
        xaxis = self.plot.getAxis("bottom")
        xaxis.setLabel("Time", units="s")
        xaxis.setGrid(100)
        xaxis.enableAutoSIPrefix()

        yaxis = self.plot.getAxis("left")
        yaxis.setTicks([[(0, "0")], [(i, str(i)) for i in xrange(-5, 6, 1)]])
        yaxis.setGrid(100)

        # Cursors
        self.lx1 = pg.InfiniteLine(angle=90, movable=True)
        self.lx2 = pg.InfiniteLine(angle=90, movable=True)
        self.plot.addItem(self.lx1)
        self.plot.addItem(self.lx2)

        self.y_cursors = {}
        for channel in xrange(3, 0, -1):
            pen = {"color": self.channel_colors[channel]}
            l = self.y_cursors[channel+1] = pg.InfiniteLine(
                angle=0, movable=True, pen=pen)
            self.plot.addItem(l)

        # Legend
        self.legend = pg.LegendItem(offset=(-5, 5))
        self.legend.setParentItem(self.plotitem)

        # Attributes
        self.waveform_plots = {}
        self._waveform_attrs = {}
        self._waveform_data = {}
        self._timescale_attr = None
        self._timescale_data = []

        # Signals
        self.trigger.connect(self._show_graph)

    # Overiding methods
    
    def parentModelChanged(self, model):
        """Set the new model if using the parent model."""
        if self.useParentModel:
            self.setModel(model)    

    def setModel(self, scope):
        """Set the model from a given scope model name."""
        # Model
        TaurusWidget.setModelName(self, scope)
        self._scope = self.getModelObj()
        if not self._scope:
            return
        # Wavefroms
        for i in xrange(4):
            wf = "WaveformDataCh%d" % (i + 1)
            attr = self._waveform_attrs[wf] = self._scope.getAttribute(wf)
            attr.addListener(self._handle_waveform)
            p = self.waveform_plots[wf] = pg.PlotDataItem(
                pen={"color": self.channel_colors[i], "width": 1})
            self.plotitem.addItem(p)
            self.legend.addItem(p, i + 1)

            chstate = "StateCh%d" % (i + 1)
            s = self._scope.getAttribute(chstate)
            s.addListener(self._handle_state)
        # Timescale
        attr = self._scope.getAttribute("TimeScale")
        attr.addListener(self._handle_timescale)

    # Semi private methods

    def _handle_state(self, evt_src, evt_type, evt_value):
        """Handle events from the channel states."""
        if (evt_type in (PyTango.EventType.PERIODIC_EVENT,
                         PyTango.EventType.CHANGE_EVENT) and evt_value):
            s = evt_value.value
            wf = "WaveformDataCh%s" % evt_value.name[-1]  
            if s:
                self.plotitem.addItem(self.waveform_plots[wf])
            else:
                self.plotitem.removeItem(self.waveform_plots[wf])

    def _handle_timescale(self, evt_src, evt_type, evt_value):
        """Handle events from the time scale attribute."""
        if (evt_type in (PyTango.EventType.PERIODIC_EVENT,
                         PyTango.EventType.CHANGE_EVENT) and evt_value):
            timedata = evt_value.value
            self.set_timescale(timedata)

    def _handle_waveform(self, evt_src, evt_type, evt_value):
        """Handle events from the channel waveforms."""
        if (evt_type in (PyTango.EventType.PERIODIC_EVENT,
                         PyTango.EventType.CHANGE_EVENT) and evt_value):
            wfname = evt_value.name
            wfdata = evt_value.value
            self.set_waveform(wfname, wfdata)

    def set_timescale(self, scale):
        """Set the timescale from a given list."""
        scale = [] if scale is None else scale
        self._timescale_data = scale
        if len(scale):
            self.vb.setRange(xRange=(scale[0], scale[-1]), padding=0)

    def set_waveform(self, wfname, wfdata):
        """Apply given data to a given waveform."""
        self._waveform_data[wfname] = wfdata
        self.trigger.emit(wfname)

    def _show_graph(self, wf):
        """Update a given waveform on the graph."""
        wf = str(wf)
        if wf in self.waveform_plots and wf in self._waveform_data:
            data = self._waveform_data[wf]
            if data is not None and len(data):
                self.waveform_plots[wf].setData(y=data, x=self._timescale_data)
