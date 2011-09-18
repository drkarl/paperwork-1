#!/usr/bin/env python

from distutils.core import setup

setup(name="Paperwork",
      version="0.1",
      description="Grep for dead trees",
      author="Jerome Flesch",
      author_email="jflesch@gmail.com",
      packages=['paperwork'],
      package_dir={ 'paperwork': 'src' },
      data_files=[('share/paperwork', [
          'src/aboutdialog.glade',
          'src/mainwindow.glade',
          'src/searchwindow.glade',
          'src/settingswindow.glade',
      ])],
      scripts=['scripts/paperwork'],
     )

