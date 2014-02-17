#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
###########################################################################

"""
configuration file for an example of how to construct a GUI based on TaurusGUI  

This configuration file determines the default, permanent, pre-defined
contents of the GUI. While the user may add/remove more elements at run
time and those customizations will also be stored, this file defines what a
user will find when launching the GUI for the first time.
"""

#==============================================================================
# Import section. You probably want to keep this line. Don't edit this block 
# unless you know what you are doing
from taurus.qt.qtgui.taurusgui.utils import PanelDescription, Qt_Qt, ExternalApp, ToolBarDescription, AppletDescription
# (end of import section)
#==============================================================================


#===============================================================================
# General info.
#===============================================================================
GUI_NAME = 'scope'
ORGANIZATION = 'MAXIV'

#===============================================================================
# Specific logo. It can be an absolute path,or relative to the app dir or a 
# resource path. If commented out, ":/taurus.png" will be used
#===============================================================================
CUSTOM_LOGO = 'images/maxivlogo.png'

#===============================================================================
# You can provide an URI for a manual in html format
# (comment out or make MANUAL_URI=None to skip creating a Manual panel) 
#===============================================================================

#===============================================================================
# If you want to have a main synoptic panel, set the SYNOPTIC variable
# to the file name of a jdraw file. If a relative path is given, the directory
# containing this configuration file will be used as root
# (comment out or make SYNOPTIC=None to skip creating a synoptic panel)
#===============================================================================

#===============================================================================
# Set INSTRUMENTS_FROM_POOL to True for enabling auto-creation of
# instrument panels based on the Pool Instrument info
#===============================================================================
INSTRUMENTS_FROM_POOL = False

#===============================================================================
# Define panels to be shown.  
# To define a panel, instantiate a PanelDescription object (see documentation
# for the gblgui_utils module)
#===============================================================================


configWidget2 = PanelDescription('myconfig2',
                                 classname = 'TaurusForm',
                                 model = ['scope/rohdeschwarz/rto-1024/OffsetCh1',
                                          'scope/rohdeschwarz/rto-1024/OffsetCh2',
                                          'scope/rohdeschwarz/rto-1024/OffsetCh3',
                                          'scope/rohdeschwarz/rto-1024/OffsetCh4',
                                          'scope/rohdeschwarz/rto-1024/VScaleCh1',
                                          'scope/rohdeschwarz/rto-1024/VScaleCh2',
                                          'scope/rohdeschwarz/rto-1024/VScaleCh3',
                                          'scope/rohdeschwarz/rto-1024/VScaleCh4',
                                          'scope/rohdeschwarz/rto-1024/HScale'],                               
                                 )

configWidget = PanelDescription('myconfig1',
                                 classname = 'TaurusForm',
                                 model = ['scope/rohdeschwarz/rto-1024/TrigLevel',
                                          'scope/rohdeschwarz/rto-1024/CouplingCh1',
                                          'scope/rohdeschwarz/rto-1024/CouplingCh2',
                                          'scope/rohdeschwarz/rto-1024/CouplingCh3',
                                          'scope/rohdeschwarz/rto-1024/CouplingCh4'],
                                )

waveWidget2 = PanelDescription('mywave2',
                                 classname = 'TaurusPlot',
                                 model = ['scope/rohdeschwarz/rto-1024/WaveformDataCh1'],
                                )

#custom panel
measurements1 = PanelDescription('measurements',
                                 classname='TaurusScopeMeasurements',
                                 modulename='tgconf_scope.panels',
                                 area=Qt_Qt.TopDockWidgetArea,
                                 model=['scope/rohdeschwarz/rto-1024/Measurement1',
                                        'scope/rohdeschwarz/rto-1024/Measurement2',
                                        'scope/rohdeschwarz/rto-1024/Measurement3',
                                        'scope/rohdeschwarz/rto-1024/Measurement4',
                                        'scope/rohdeschwarz/rto-1024/Measurement5',
                                        'scope/rohdeschwarz/rto-1024/Measurement6',
                                        'scope/rohdeschwarz/rto-1024/Measurement7',
                                        'scope/rohdeschwarz/rto-1024/Measurement8',
                                        'scope/rohdeschwarz/rto-1024/Measurement1Res',
                                        'scope/rohdeschwarz/rto-1024/Measurement2Res',
                                        'scope/rohdeschwarz/rto-1024/Measurement3Res',
                                        'scope/rohdeschwarz/rto-1024/Measurement4Res',
                                        'scope/rohdeschwarz/rto-1024/Measurement5Res',
                                        'scope/rohdeschwarz/rto-1024/Measurement6Res',
                                        'scope/rohdeschwarz/rto-1024/Measurement7Res',
                                        'scope/rohdeschwarz/rto-1024/Measurement8Res']
                                 )

#custom panel
mod = []
mod.append('scope/rohdeschwarz/rto-1024/Status')
mod.append('scope/rohdeschwarz/rto-1024/State')
mod.append('scope/rohdeschwarz/rto-1024/AcquireAvailable')
print 'pjb', mod
controlwidget = PanelDescription('Control',
                                 classname='Control',
                                 modulename='tgconf_scope.panels',
                                 area = Qt_Qt.TopDockWidgetArea,
                                 model=mod)



#===============================================================================
# Define custom toolbars to be shown. To define a toolbar, instantiate a
# ToolbarDescription object (see documentation for the gblgui_utils module)
#===============================================================================


#===============================================================================
# Define custom applets to be shown in the applets bar (the wide bar that
# contains the logos). To define an applet, instantiate an AppletDescription
# object (see documentation for the gblgui_utils module)
#===============================================================================


#===============================================================================
# Define which External Applications are to be inserted.
# To define an external application, instantiate an ExternalApp object
# See TaurusMainWindow.addExternalAppLauncher for valid values of ExternalApp
#===============================================================================


#===============================================================================
# Macro execution configuration
# (comment out or make MACRO_SERVER=None to skip creating a macro execution 
# infrastructure)
#===============================================================================
#MACROSERVER_NAME = 
#DOOR_NAME = 
#MACROEDITORS_PATH = 

#===============================================================================
# Monitor widget (This is obsolete now, you can get the same result defining a
# custom applet with classname='TaurusMonitorTiny')
#===============================================================================
# MONITOR = ['sys/tg_test/1/double_scalar_rww']

#===============================================================================
# Adding other widgets to the catalog of the "new panel" dialog.
# pass a tuple of (classname,screenshot)
# -classname may contain the module name.
# -screenshot can either be a file name relative to the application dir or 
# a resource URL or None
#===============================================================================
