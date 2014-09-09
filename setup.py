#!/usr/bin/env python

from setuptools import setup

setup(name = "taurusgui-rtmscope",
      version = "0.0.1",
      description = "TaurusGUI for the RTM Scope",
      author = "Vincent MICHEL",
      license = "GPLv3",
      packages = ["rtmscope"],
      include_package_data=True,
      package_data={'': ['*.png']},
      scripts = ['scripts/RtmScope']
     )

