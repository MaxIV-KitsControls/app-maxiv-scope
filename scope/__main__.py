"""Module to run the taurus GUI."""

# Imports
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.taurusgui import TaurusGui
from scope import config
import sys

# Constants
PERIOD_ARG = "--taurus-polling-period="
PERIOD = 100

# Argument formating
for arg in sys.argv:
    if arg.startswith(PERIOD_ARG):
        break
else:
    sys.argv.append(PERIOD_ARG+str(PERIOD))
    
# Run
app = TaurusApplication() 
gui = TaurusGui(confname=config.__file__)
gui.show()
app.exec_() 
