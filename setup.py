#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="taurusgui-scope",
      version="4.1.3",
      packages=find_packages(),
      entry_points={'gui_scripts': ['ctscope = scopegui:main']},

      include_package_data=True,
      package_data={'': ['*.png']},
      data_files=[('/usr/share/applications', ['maxiv-scope.desktop'])],

      license="GPLv3",
      description="TaurusGUI for oscilloscopes",
      author="Vincent Michel",
      url="http://www.maxlab.lu.se",
      )
