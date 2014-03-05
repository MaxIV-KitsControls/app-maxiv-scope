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
device_name = 'm4gun/scope/rohdeschwarz/'

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


display = PanelDescription(
    'Display',
    classname='TaurusForm',
    model=[device_name+'OffsetCh1',
           device_name+'OffsetCh2',
           device_name+'OffsetCh3',
           device_name+'OffsetCh4',
           device_name+'VScaleCh1',
           device_name+'VScaleCh2',
           device_name+'VScaleCh3',
           device_name+'VScaleCh4',
           device_name+'HScale'],
)

trigger = PanelDescription(
    'Trigger',
    classname='TaurusForm',
    model=[device_name+'Trig1Source',
           device_name+'Trig1Mode',
           device_name+'TrigLevel']
)

channels = PanelDescription(
    'Channels',
    classname='TaurusForm',
    model=[device_name+'CouplingCh1',
           device_name+'CouplingCh2',
           device_name+'CouplingCh3',
           device_name+'CouplingCh4']
)


#custom panel
measurements = PanelDescription(
    'Measurements',
    classname='TaurusScopeMeasurements',
    modulename='tgconf_scope.panels',
    area=Qt_Qt.TopDockWidgetArea,
    model=[
        device_name+'Measurement1',
        device_name+'Measurement2',
        device_name+'Measurement3',
        device_name+'Measurement4',
        device_name+'Measurement5',
        device_name+'Measurement6',
        device_name+'Measurement7',
        device_name+'Measurement8',
        device_name+'Measurement1Res',
        device_name+'Measurement2Res',
        device_name+'Measurement3Res',
        device_name+'Measurement4Res',
        device_name+'Measurement5Res',
        device_name+'Measurement6Res',
        device_name+'Measurement7Res',
        device_name+'Measurement8Res',
        device_name+'Measurement1Source',
        device_name+'Measurement2Source',
        device_name+'Measurement3Source',
        device_name+'Measurement4Source',
        device_name+'Measurement5Source',
        device_name+'Measurement6Source',
        device_name+'Measurement7Source',
        device_name+'Measurement8Source',
        #
        device_name+'MeasurementGateOnOff',
        device_name+'MeasurementGateStart',
        device_name+'MeasurementGateStop',
        ],
    sharedDataRead={'SelectedInstrument':'updateCursors'},
    )

allwaveforms = PanelDescription(
    'AllWaveforms',
    classname='TestPlot',
    modulename='tgconf_scope.panels',
    area=Qt_Qt.TopDockWidgetArea,
    model=[
        device_name+'TimeScale|'+device_name+'WaveformDataCh1',
        device_name+'TimeScale|'+device_name+'WaveformDataCh2',
        device_name+'TimeScale|'+device_name+'WaveformDataCh3',
        device_name+'TimeScale|'+device_name+'WaveformDataCh4',
        ],
    sharedDataWrite={'SelectedInstrument':'sendPoint(QString)'}
)

#custom control panel
mod = []
mod.append(device_name+'Status')
mod.append(device_name+'State')
mod.append(device_name+'AcquireAvailable')
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
