cmdchess
========
A Windows command line application to play chess (specifically) using the command prompt.

.. image:: https://badge.fury.io/py/cmdchess.svg
    :target: https://badge.fury.io/py/cmdchess

.. image:: https://travis-ci.org/leonarduschen/cmdchess.svg?branch=master
    :target: https://travis-ci.org/leonarduschen/cmdchess

.. image:: https://readthedocs.org/projects/cmdchess/badge/?version=latest
    :target: https://cmdchess.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Documentation
-------------
https://cmdchess.readthedocs.io/en/latest/

Overview
--------
Note: This project is still a work in progress and errors are expected to be fixed in a few days.

This project aims to serve as the go-to command line chess application for Windows users. As more and more windows users are becoming power users, a light-weight CLI chess application provides great convenience to access chess puzzles - which hopefully enables chess enthusiasts to practice more often and improve their tacticical abilities.

Since most command-line chess applications are catered to Unicode consoles (and somewhat alienating Windows users), the project has been developed to cater to ASCII consoles - and therefore can be run in what Windows users are familiar with: ``cmd.exe``

.. image:: docs/_static/ASCII.jpg

Upcoming core featues

* Short-algebraic notation to input moves
* Popular chess variants (e.g. chess960, horde)
* Puzzles from databases
* Popular games history

Errors

* Checkmate
* Promotion

Source location
~~~~~~~~~~~~~~~

Hosted on GitHub: https://github.com/leonarduschen/cmdchess

Installation
~~~~~~~~~~~~

``pip install cmdchess``


Quick Start
-----------
Launch app: ``cmdchess``

Run on unicode console: ``cmdchess -utf``

Help: ``cmdchess --help``


License
-------
This package is open sourced under the MIT license.