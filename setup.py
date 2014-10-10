#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = "taurusgui-scope",
      version = "3.0.4",
      description = "TaurusGUI for the different scopes",
      author = "Vincent MICHEL",
      license = "GPLv3",
      packages = find_packages(),
      include_package_data=True,
      package_data={'': ['*.png']},
      data_files=[('/usr/share/applications', ['maxiv-scope.desktop'])],
      scripts = ['scripts/ctscope']
     )

