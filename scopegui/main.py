"""Module to run the taurus GUI."""

# Imports
import sys
from PyQt4 import QtGui
from functools import partial
from taurus.qt.qtgui.taurusgui import TaurusGui
from taurus.qt.qtgui.application import TaurusApplication
from scopegui.dialog import parse_argv_and_get_device_list
from scopegui.widget import ScopeWidget


# Constants
CLASSES = "RTMScope", "RTOScope", "LecroyScope"
MODULE_NAME = "scopegui"
PERIOD_ARG = "--taurus-polling-period="
PERIOD = 500


# Callback for actions
def display_widgets(arg, gui, name):
    """Display or hide widgets with a given name."""
    for child in gui.findChildren(QtGui.QWidget, name=name):
        child.setVisible(arg)


# Setup display action
def setup_display_action(gui, name, widget_name):
    """Setup a display action."""
    callback = partial(display_widgets, gui=gui, name=widget_name)
    action = QtGui.QAction(name, gui, triggered=callback, checkable=True)
    gui.quickAccessToolBar.addAction(action)


# Enable display buttons
def enable_display_buttons(gui):
    """Enable the display buttons."""
    for child in gui.quickAccessToolBar.findChildren(QtGui.QToolButton):
        if child.text():
            child.click()


# Argument formating
def set_polling_period(period):
    """Set the polling period if not defined in sys.argv."""
    for arg in sys.argv:
        if arg.startswith(PERIOD_ARG):
            break
    else:
        sys.argv.append(PERIOD_ARG+str(period))


# Create panels
def create_panels(gui, devices):
    """Create panels and set application name."""
    for device in devices:
        name = 'Scope {0}'.format(device)
        gui.createPanel(ScopeWidget(), name, floating=False, permanent=True)
        gui.getPanel(name).widget().setModel(device)


# Set application name
def set_application_name(gui, app_name):
    """Set a given application name."""
    gui.setWindowTitle(app_name)
    TaurusApplication.instance().setApplicationName(app_name)
    TaurusApplication.instance().basicConfig()


# Main function
def main(period=PERIOD):
    """Run the scope taurus gui with a given refreshing period."""
    set_polling_period(period)
    # Get devices and application name
    devices, server = parse_argv_and_get_device_list(CLASSES)
    app_name = server.replace("/", "-")
    # Create GUI
    app = TaurusApplication()
    gui = TaurusGui(confname=MODULE_NAME)
    set_application_name(gui, app_name)
    create_panels(gui, devices)
    # Setup GUI
    gui.jorgsBar.hide()
    setup_display_action(gui, "Main panel", "MainPanel")
    gui.quickAccessToolBar.addSeparator()
    setup_display_action(gui, "Settings panel", "SettingsPanel")
    enable_display_buttons(gui)
    # Run
    gui.show()
    app.exec_()


# Main execution
if __name__ == "__main__":
    main()
