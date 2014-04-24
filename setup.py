#!/usr/bin/env python

from setuptools import setup

setup(name = "taurusgui-scope",
      version = "2.3.0",
      description = "TaurusGUI for Rohde&Schwarz oscilloscope",
      author = "Paul Bell",
      author_email = "paul.bell@maxlab.lu.se",
      license = "GPLv3",
      url = "http://www.maxlab.lu.se",
      package_dir = {'':'src',},
      packages = ['tgconf_scope', 'tgconf_scope.panels'],
      include_package_data=True,
      package_data={'tgconf_scope': ['images/maxivlogo.png']},
      scripts = ['scripts/ctScope']
     )

