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


# Main class
class ScopeWidget(TaurusWidget):
    """Main widget for the RTM scope."""

    channels = range(1,5)
    
    def __init__(self, *args, **kwargs):
        """Create inner widgets and set the layout."""
        TaurusWidget.__init__(self, *args, **kwargs)
        # Create layout
        self.setLayout(QtGui.QGridLayout())
        # Create widgets
        self.exec_dialog = self.build_exec_dialog()
        self.state_widget = self.build_state_widget()
        self.command_widget = self.build_command_widget(self.exec_dialog)
        self.plot_widget = self.build_plot_widget()
        self.channel_widget = self.build_channel_widget()
        self.range_widget = self.build_range_widget()
        self.position_widget = self.build_position_widget()
        self.scale_widget = self.build_scale_widget()
        # Add widget
        self.layout().addWidget(self.plot_widget,     0, 0, 5, 1)
        self.layout().addWidget(self.state_widget,    0, 1, 1, 2)
        self.layout().addWidget(self.command_widget,  1, 1, 1, 1)
        self.layout().addWidget(self.channel_widget,  1, 2, 1, 1)
        self.layout().addWidget(self.range_widget,    2, 1, 1, 2)
        self.layout().addWidget(self.position_widget, 3, 1, 1, 2)
        self.layout().addWidget(self.scale_widget,    4, 1, 1, 2)
        # Adjust stretch
        self.layout().setColumnStretch(0,2)
        self.layout().setColumnStretch(1,1)
        self.layout().setColumnStretch(2,0)
        self.layout().setRowStretch(1,0)
        self.layout().setRowStretch(1,3)
        self.layout().setRowStretch(2,0)
        self.layout().setRowStretch(3,2)
        self.layout().setRowStretch(4,2)

    def build_state_widget(self):
        widget = NoButtonTaurusForm(parent=self)
        widget.useParentModel = True
        widget.model = ['state', 'status']
        return widget

    def build_command_widget(self, dialog):
        ignore = ["execcommand"]
        widget = FilteredTaurusCommandsForm(parent=self, ignore=ignore)
        widget.useParentModel = True
        widget.exec_button = self.build_exec_button(dialog)
        widget.layout().addWidget(widget.exec_button)
        widget.layout().setStretch(0,1)
        return widget

    def build_exec_button(self, dialog):
        # Frame
        widget = QtGui.QFrame()
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