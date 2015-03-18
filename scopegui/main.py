"""Module to run the taurus GUI."""

# Imports
import os
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

# Configuration
ORGANIZATION = 'MAXIV'
LOGO = 'images/maxivlogo.png'


# Create application
def create_application(app_name, organization, logo):
    """Return an (application, taurusgui) pair."""
    app = TaurusApplication(app_name=app_name)
    gui = TaurusGui()
    gui.show()
    basedir = os.path.dirname(__file__)
    path = os.path.join(basedir, logo)
    gui.setWindowIcon(QtGui.QIcon(path))
    app.setOrganizationName(organization)
    return app, gui


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


# Main function
def main(period=PERIOD):
    """Run the scope taurus gui with a given refreshing period."""
    set_polling_period(period)
    # Get devices and application name
    devices, server = parse_argv_and_get_device_list(CLASSES)
    app_name = server.replace("/", "-")
    # Create GUI
    app, gui = create_application(app_name, ORGANIZATION, LOGO)
    create_panels(gui, devices)
    # Hide toolbars
    gui.jorgsBar.hide()
    gui.statusBar().hide()
    gui.panelsToolBar.hide()
    gui.perspectivesToolBar.hide()
    gui.setLockView(True)
    # Setup display buttons
    setup_display_action(gui, "Main panel", "MainPanel")
    gui.quickAccessToolBar.addSeparator()
    setup_display_action(gui, "Settings panel", "SettingsPanel")
    enable_display_buttons(gui)
    # Run
    app.exec_()


# Main execution
if __name__ == "__main__":
    main()
