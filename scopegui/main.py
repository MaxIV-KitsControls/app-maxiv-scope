"""Module to run the taurus GUI."""

# Imports
import sys
from PyQt4 import QtGui
from functools import partial
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.taurusgui import TaurusGui

# Constants
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
    for child in gui.quickAccessToolBar.findChildren(QtGui.QToolButton):
        if child.text():
            child.click()


# Argument formating
def set_polling_period(period):
    for arg in sys.argv:
        if arg.startswith(PERIOD_ARG):
            break
    else:
        sys.argv.append(PERIOD_ARG+str(period))


# Main function
def main(period=PERIOD):
    """Run the scope taurus gui with a given refreshing period."""
    set_polling_period(period)
    # Create GUI
    app = TaurusApplication()
    gui = TaurusGui(confname=MODULE_NAME)
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
