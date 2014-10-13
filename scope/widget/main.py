"""Main widget for the RTM scope."""

# Dev patch
if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')

# Taurus import
from taurus.qt import QtGui, QtCore
from taurus.qt.qtgui.container import TaurusWidget, TaurusScrollArea

# Widget imports
from scope.widget.base import FilteredTaurusCommandsForm
from scope.widget.base import NoButtonTaurusForm
from scope.widget.base import PatchedTaurusValueCheckBox
from scope.widget.base import PatchedTaurusPlot
try: from scope.widget.scopeplot import ScopePlotWidget
except ImportError as e: ScopePlotWidget = None

# Apply patch
from scope.widget.patch import check_and_patch
check_and_patch(True)

# Main class
class ScopeWidget(TaurusScrollArea):
    """Main widget for the RTM scope."""

    channels = range(1,5)
    expert = True
    
    def __init__(self, *args, **kwargs):
        """Create inner widgets and set the layout."""
        TaurusScrollArea.__init__(self, *args, **kwargs)
        self.setFrameShape(self.NoFrame)
        # Create layout
        self.setLayout(QtGui.QGridLayout())
        # Create widgets
        self.state_widget = self.build_state_widget()
        self.exec_dialog = self.build_exec_dialog() if self.expert else None
        self.command_widget = self.build_command_widget(self.exec_dialog)
        self.plot_widget = self.build_plot_widget()
        self.channel_widget = self.build_channel_widget()
        self.tab_widget = self.build_tab_widget()
        # Add widget
        self.layout().addWidget(self.plot_widget,     0, 0, 3, 1)
        self.layout().addWidget(self.state_widget,    0, 1, 1, 2)
        self.layout().addWidget(self.command_widget,  1, 1, 1, 1)
        self.layout().addWidget(self.channel_widget,  1, 2, 1, 1)
        self.layout().addWidget(self.tab_widget,      2, 1, 1, 2)
        # Adjust stretch
        self.layout().setColumnStretch(0,4)
        self.layout().setColumnStretch(1,2)
        self.layout().setColumnStretch(2,1)
        self.layout().setRowStretch(0,0)
        self.layout().setRowStretch(1,3)
        self.layout().setRowStretch(2,5)

    def build_tab_widget(self):
        widget = QtGui.QTabWidget(parent=self)
        widget.setTabPosition(widget.South)
        # First tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.position_widget = self.build_position_widget()
        self.scale_widget = self.build_scale_widget()
        tab.layout().addWidget(self.position_widget)
        tab.layout().addWidget(self.scale_widget)
        tab.layout().setContentsMargins(0,0,0,0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, "Channel")
        # Second tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.time_widget = self.build_time_widget()
        tab.layout().addWidget(self.time_widget)
        tab.layout().setContentsMargins(0,0,0,0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, u"Time")
        # Third tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.trigger_widget = self.build_trigger_widget()
        self.level_widget = self.build_level_widget()
        tab.layout().addWidget(self.trigger_widget)
        tab.layout().addWidget(self.level_widget)
        tab.layout().setStretch(0,2)
        tab.layout().setStretch(1,5)
        tab.layout().setContentsMargins(0,0,0,0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, u"Trigger")
        # Return
        return widget

    def build_state_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['state', 'status']
        return widget

    def build_command_widget(self, dialog):
        ignore = ["execcommand", "autoset"]
        widget = FilteredTaurusCommandsForm(parent=self, ignore=ignore)
        widget.useParentModel = True
        if dialog:
            widget.exec_button = self.build_exec_button(dialog)
            widget.layout().addWidget(widget.exec_button)
            widget.layout().setStretch(0,1)
            widget.layout().setStretch(1,0)
        return widget

    def build_exec_button(self, dialog):
        # Frame
        CustomArea = type("CustomArea", (TaurusScrollArea,), {})
        CustomArea.minimumSizeHint = lambda self: QtCore.QSize(0,0)
        widget = CustomArea()
        widget.setFrameShape(widget.Panel)
        widget.setFrameShadow(widget.Sunken)
        layout = QtGui.QHBoxLayout()
        # Label
        label = QtGui.QLabel('[Expert only]')
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)
        # Button
        button = QtGui.QPushButton('ExecCommand')
        button.clicked.connect(dialog.show)
        layout.addWidget(button)
        # Layout
        widget.setLayout(layout)
        widget.layout().setStretch(0,1)
        return widget

    def build_exec_widget(self):
        include = ["execcommand"]
        widget = FilteredTaurusCommandsForm(include=include,
                                            show_output=True)
        widget.useParentModel = True
        return widget

    def build_exec_dialog(self):
        dialog = QtGui.QDialog(self, flags=QtCore.Qt.Window)
        dialog.setWindowTitle("ExecCommand")
        layout = QtGui.QGridLayout()
        widget = self.build_exec_widget()
        layout.addWidget(widget)
        dialog.setLayout(layout)
        return dialog

    def build_plot_widget(self):
        if ScopePlotWidget:
            return self.build_scopeplot_widget()
        return self.build_taurusplot_widget()

    def build_scopeplot_widget(self):
        widget = ScopePlotWidget(parent=self)
        widget.setUseParentModel(True)
        return widget

    def build_taurusplot_widget(self):
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
        widget.setMinimumSize(205,0)
        for item in widget:
            item.setWriteWidgetClass(PatchedTaurusValueCheckBox)
            item.setReadWidgetClass(None) 
        return widget

    def build_time_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['HRange', 'HPosition']
        return widget

    def build_trigger_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['TriggerChannel', 'TriggerSlope']
        return widget

    def build_level_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['TriggerLevel{0:1d}'.format(channel)
                        for channel in range(1,6)]
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
