"""Provide the taurus gui configuration for the scope devices."""

__all__ = ["main", "ScopeWidget"]

# Imports
from scopegui.main import main
from scopegui.widget import ScopeWidget

# Configuration
ORGANIZATION = 'MAXIV'
CUSTOM_LOGO = 'images/maxivlogo.png'
INSTRUMENTS_FROM_POOL = False
