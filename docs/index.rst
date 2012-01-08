.. pywunderground documentation master file, created by
   sphinx-quickstart on Sat Jan  7 19:44:58 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============

Release v\ |version|.

.. toctree::
    :maxdepth: 2

pywunderground aims to provide a simple interface for retrieving weather data with `wunderground API <http://www.wunderground.com/>`_.
Returned data is always a directly usable dict

Examples
========

List cities
-----------

Listing cities in *France* with name *Paris*

::

    >>> cities = pywunderground.autocomplete('Paris', 'FR'):
    >>> cities
    ...

Get the weather
---------------

Get the current condition and forecast for *Paris* in *France*

::

    >>> current_weather = pywunderground.request('yourapikey', ['conditions', 'forecast'], 'Paris')
    ...

API Documentation
=================

More details about the use of the module can be found here

.. automodule:: pywunderground
    :members:
