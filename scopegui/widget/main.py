"""Main widget for the RTM scope."""

# Dev patch
if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')

# Taurus import
from taurus.qt import QtGui, QtCore
from taurus.qt.qtgui.container import TaurusWidget, TaurusScrollArea
from taurus.qt.qtgui.button import TaurusCommandButton

# Widget imports
from scopegui.widget.base import FilteredTaurusCommandsForm
from scopegui.widget.base import NoButtonTaurusForm
from scopegui.widget.base import PatchedTaurusValueCheckBox
from scopegui.widget.base import PatchedTaurusPlot
try:
    from scopegui.widget.scopeplot import ScopePlotWidget
except ImportError as e:
    ScopePlotWidget = None

# Apply patch
from scopegui.widget.patch import check_and_patch
check_and_patch(True)


# Main class
class ScopeWidget(TaurusScrollArea):
    """Main widget for the RTM scope."""

    channels = range(1, 5)
    dialog = False

    def __init__(self, *args, **kwargs):
        """Create inner widgets and set the layout."""
        TaurusScrollArea.__init__(self, *args, **kwargs)
        self.setFrameShape(self.NoFrame)
        # Create layout
        self.setLayout(QtGui.QGridLayout())
        # Create widgets
        self.state_widget = self.build_state_widget()
        self.exec_dialog = self.build_exec_dialog() if self.dialog else None
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
        self.layout().setColumnStretch(0, 4)
        self.layout().setColumnStretch(1, 0)
        self.layout().setColumnStretch(2, 0)
        self.layout().setRowStretch(0, 0)
        self.layout().setRowStretch(1, 0)
        self.layout().setRowStretch(2, 1)

    def build_tab_widget(self):
        widget = QtGui.QTabWidget(parent=self)
        widget.setMinimumWidth(500)
        widget.setObjectName('SettingsPanel')
        widget.setTabPosition(widget.South)
        # First tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.position_widget = self.build_position_widget()
        self.scale_widget = self.build_scale_widget()
        tab.layout().addWidget(self.position_widget)
        tab.layout().addWidget(self.scale_widget)
        tab.layout().setContentsMargins(0, 0, 0, 0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, "Channel")
        # Second tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.time_widget = self.build_time_widget()
        tab.layout().addWidget(self.time_widget)
        tab.layout().setContentsMargins(0, 0, 0, 0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, u"Time")
        # Third tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.trigger_widget = self.build_trigger_widget()
        self.level_widget = self.build_level_widget()
        tab.layout().addWidget(self.trigger_widget)
        tab.layout().addWidget(self.level_widget)
        tab.layout().setStretch(0, 2)
        tab.layout().setStretch(1, 5)
        tab.layout().setContentsMargins(0, 0, 0, 0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, u"Trigger")
        # Fourth tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.trigger_coupling_widget = self.build_trigger_coupling_widget()
        self.channel_coupling_widget = self.build_channel_coupling_widget()
        tab.layout().addWidget(self.trigger_coupling_widget)
        tab.layout().addWidget(self.channel_coupling_widget)
        tab.layout().setStretch(0, 1)
        tab.layout().setStretch(1, 4)
        tab.layout().setContentsMargins(0, 0, 0, 0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, u"Coupling")
        # Fifth tab
        tab = QtGui.QWidget(parent=self)
        tab.setLayout(QtGui.QVBoxLayout())
        self.exec_widget = self.build_exec_widget()
        tab.layout().addWidget(self.exec_widget)
        tab.layout().setContentsMargins(0, 0, 0, 0)
        tab.layout().setSpacing(0)
        widget.addTab(tab, u"Expert")
        # Return
        return widget

    def build_state_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.setMinimumWidth(500)
        widget.setObjectName('MainPanel')
        widget.useParentModel = True
        widget.model = ['state', 'status']
        return widget

    def build_command_widget(self, dialog):
        # Equivalent to a taurus form
        widget = TaurusWidget()
        widget.setObjectName('MainPanel')
        widget.setLayout(QtGui.QVBoxLayout())
        frame = TaurusWidget()
        frame.setLayout(QtGui.QGridLayout())
        scroll_area = TaurusScrollArea(widget)
        scroll_area.setWidget(frame)
        scroll_area.setWidgetResizable(True)
        widget.layout().addWidget(scroll_area)
        widget.useParentModel = True
        frame.useParentModel = True
        scroll_area.useParentModel = True
        # Command buttons
        command = TaurusCommandButton(self, command="Init")
        command.setUseParentModel(True)
        frame.layout().addWidget(command, 0, 0, 1, 2)
        command = TaurusCommandButton(self, command="On")
        command.setUseParentModel(True)
        frame.layout().addWidget(command, 1, 0, 1, 1)
        command = TaurusCommandButton(self, command="Standby")
        command.setUseParentModel(True)
        frame.layout().addWidget(command, 1, 1, 1, 1)
        command = TaurusCommandButton(self, command="Run")
        command.setUseParentModel(True)
        frame.layout().addWidget(command, 2, 0, 1, 1)
        command = TaurusCommandButton(self, command="Stop")
        command.setUseParentModel(True)
        frame.layout().addWidget(command, 2, 1, 1, 1)

        return widget

    def build_exec_widget(self):
        include = ["execute"]
        widget = FilteredTaurusCommandsForm(include=include,
                                            show_output=True)
        widget.useParentModel = True
        return widget

    def build_exec_dialog(self):
        dialog = QtGui.QDialog(self, flags=QtCore.Qt.Window)
        dialog.setWindowTitle("Execute commands")
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
        widget = PatchedTaurusPlot(parent=self, scale='/TimeBase')
        widget.setMinimumWidth(500)
        widget.setObjectName('PlotPanel')
        widget.useParentModel = True
        widget.setAxisAutoScale(False)
        widget.setAxisScale(widget.yLeft, -4, 4)
        model_func = '/RawWaveform{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        return widget

    def build_channel_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.setObjectName('MainPanel')
        widget.useParentModel = True
        model_func = 'ChannelEnabled{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        widget.sizeHint = lambda: QtCore.QSize(0, 180)
        for item in widget:
            item.setWriteWidgetClass(PatchedTaurusValueCheckBox)
            item.setReadWidgetClass(None)
        return widget

    def build_time_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['TimeRange', 'TimePosition', 'RecordLength']
        return widget

    def build_trigger_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['TriggerSource', 'TriggerSlope']
        return widget

    def build_level_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['TriggerLevel{0:1d}'.format(channel)
                        for channel in range(1, 6)]
        return widget

    def build_position_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        model_func = 'ChannelPosition{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        return widget

    def build_scale_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        model_func = 'ChannelScale{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        return widget

    def build_channel_coupling_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        model_func = 'ChannelCoupling{0}'.format
        widget.model = [model_func(i) for i in self.channels]
        return widget

    def build_trigger_coupling_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['TriggerCoupling']
        return widget


# Main execution
if __name__ == "__main__":
    import sys
    import taurus
    taurus.Manager().changeDefaultPollingPeriod(100)
    app = QtGui.QApplication(sys.argv)
    myapp = ScopeWidget()
    myapp.show()
    myapp.setModel("maxiv/test/rtm")
    sys.exit(app.exec_())
