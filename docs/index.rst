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

    >>> cities = pywunderground.autocomplete('Paris', 'FR')
    >>> cities
    [{u'c': u'FR', u'tz': u'Europe/Paris', u'name': u'Paris, France', u'tzs': u'CET', u'l': u'/q/zmw:00000.1.07157', u'type': u'city', u'zmw': u'00000.1.07157'}, {u'c': u'FR', u'tz': u'Europe/Paris', u'name': u'Paris Le Bourget, France', u'tzs': u'CET', u'l': u'/q/zmw:00000.1.07150', u'type': u'city', u'zmw': u'00000.1.07150'}, {u'c': u'FR', u'tz': u'Europe/Paris', u'name': u'Paris Orly, France', u'tzs': u'CET', u'l': u'/q/zmw:00000.1.07149', u'type': u'city', u'zmw': u'00000.1.07149'}, {u'c': u'FR', u'tz': u'Europe/Paris', u'name': u'Paris-Plage, France', u'tzs': u'CET', u'l': u'/q/zmw:00000.6.07003', u'type': u'city', u'zmw': u'00000.6.07003'}]

Get the weather
---------------

Get the current condition and forecast for *Paris* in *France*

    >>> weather = pywunderground.request('yourapikey', ['conditions', 'forecast'], 'Paris')
    >>> weather
    {u'response': {u'termsofService': u'http://www.wunderground.com/weather/api/d/terms.html', u'version': u'0.1', u'features': {u'conditions': 1, u'forecast': 1}, u'results': [{u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:72855.1.99999', u'state': u'AR', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'72855.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'FR', u'l': u'/q/zmw:00000.1.07157', u'state': u'', u'country_iso3166': u'FR', u'country_name': u'France', u'zmw': u'00000.1.07157'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:83261.1.99999', u'state': u'ID', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'83261.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:61944.1.99999', u'state': u'IL', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'61944.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:40361.1.99999', u'state': u'KY', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'40361.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:04271.1.99999', u'state': u'ME', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'04271.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:49338.1.99999', u'state': u'MI', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'49338.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:38949.2.99999', u'state': u'MS', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'38949.2.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:65275.1.99999', u'state': u'MO', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'65275.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:13456.2.99999', u'state': u'NY', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'13456.2.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:44669.1.99999', u'state': u'OH', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'44669.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:15021.2.99999', u'state': u'PA', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'15021.2.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:38242.1.99999', u'state': u'TN', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'38242.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:75460.1.99999', u'state': u'TX', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'75460.1.99999'}, {u'city': u'Paris', u'name': u'Paris', u'country': u'US', u'l': u'/q/zmw:20130.1.99999', u'state': u'VA', u'country_iso3166': u'US', u'country_name': u'USA', u'zmw': u'20130.1.99999'}]}}

API Documentation
=================

More details about the use of the module can be found here

.. automodule:: pywunderground
    :members:
