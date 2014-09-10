#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = "taurusgui-rtmscope",
      version = "0.0.1",
      description = "TaurusGUI for the RTM Scope",
      author = "Vincent MICHEL",
      license = "GPLv3",
      packages = find_packages(),
      include_package_data=True,
      package_data={'': ['*.png']},
      scripts = ['scripts/RtmScope']
     )

