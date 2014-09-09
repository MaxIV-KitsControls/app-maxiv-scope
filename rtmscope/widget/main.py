"""Main widget for the RTM scope."""

# Dev patch
if __name__ == "__main__":
    import sys
    sys.path.append('../..')


# Qt import
from PyQt4 import QtGui, QtCore


# Taurus import
from taurus.qt.qtgui.container import TaurusWidget


# Widget imports
from rtmscope.widget.base import FilteredTaurusCommandsForm
from rtmscope.widget.base import NoButtonTaurusForm
from rtmscope.widget.base import PatchedTaurusValueCheckBox
from rtmscope.widget.base import PatchedTaurusPlot


# Main class
class ScopeWidget(TaurusWidget):
    """Main widget for the RTM scope."""

    channels = range(1,5)
    
    def __init__(self, *args, **kwargs):
        """Create inner widgets and set the layout."""
        TaurusWidget.__init__(self, *args, **kwargs)
        # Create layout
        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)
        # Create widgets
        self.state_widget = self.build_state_widget()
        self.command_widget = self.build_command_widget()
        self.plot_widget = self.build_plot_widget()
        self.channel_widget = self.build_channel_widget()
        self.range_widget = self.build_range_widget()
        self.position_widget = self.build_position_widget()
        self.scale_widget = self.build_scale_widget()
        # Add widget
        self.layout.addWidget(self.plot_widget,     0, 0, 5, 1)
        self.layout.addWidget(self.state_widget,    0, 1, 1, 2)
        self.layout.addWidget(self.command_widget,  1, 1, 1, 1)
        self.layout.addWidget(self.channel_widget,  1, 2, 1, 1)
        self.layout.addWidget(self.range_widget,    2, 1, 1, 2)
        self.layout.addWidget(self.position_widget, 3, 1, 1, 2)
        self.layout.addWidget(self.scale_widget,    4, 1, 1, 2)
        # Adjust stretch
        self.layout.setColumnStretch(0,2)
        self.layout.setColumnStretch(1,1)
        self.layout.setColumnStretch(2,0)
        self.layout.setRowStretch(1,0)
        self.layout.setRowStretch(1,2)
        self.layout.setRowStretch(2,0)
        self.layout.setRowStretch(3,2)
        self.layout.setRowStretch(4,2)

    def build_state_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['state', 'status']
        return widget

    def build_command_widget(self):
        ignore = ["execcommand"]
        widget = FilteredTaurusCommandsForm(ignore=ignore)
        widget.useParentModel = True
        return widget

    def build_plot_widget(self):
        widget = PatchedTaurusPlot(parent=self, scale='/TimeScale')
        widget.useParentModel = True
        widget.setAxisAutoScale(False)
        widget.setAxisScale(widget.yLeft, -4, 4)
        model_func = '/WaveformDataCh{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        return widget

    def build_channel_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        model_func = 'StateCh{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        widget.setMinimumSize(200,0)
        for item in widget:
            item.setWriteWidgetClass(PatchedTaurusValueCheckBox)
            item.setReadWidgetClass(None) 
        return widget

    def build_range_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['HRange']
        return widget

    def build_position_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        model_func = 'PositionCh{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        return widget

    def build_scale_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        model_func = 'VScaleCh{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        return widget
        

# Main execution
if __name__ == "__main__":
    import taurus, sys
    taurus.Manager().changeDefaultPollingPeriod(100)
    app = QtGui.QApplication(sys.argv)
    myapp = ScopeWidget()
    myapp.show()
    myapp.setModel("maxiv/dev/scope")
    sys.exit(app.exec_())
