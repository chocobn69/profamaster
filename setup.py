#!/usr/bin/env python

from distutils.core import setup

setup(name='profamaster',
      version='1.0',
      description='Simili rest web server to control profalux panes',
      author='Nicolas Baccelli',
      author_email='nicolas.baccelli@gmail.com',
      url='https://github.com/chocobn69/profamaster',
      packages=['profamaster', 'profamaster.shiftpi'],
      scripts=['scripts/profamaster-server', ],
      )
