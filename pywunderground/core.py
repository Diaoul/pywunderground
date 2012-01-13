# -*- coding: utf-8 -*-
# Copyright (c) 2011-2012 Antoine Bertin <diaoulael@gmail.com>
#
# This file is part of pywunderground.
#
# pywunderground is free software; you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# pywunderground is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with pywunderground.  If not, see <http://www.gnu.org/licenses/>.
import requests
import json
from urllib import quote


__all__ = ['FEATURES', 'autocomplete', 'request']


#: Available API request features
FEATURES = ['geolookup', 'conditions', 'forecast', 'astronomy', 'radar', 'satellite', 'webcams', 'history',
            'alerts', 'hourly', 'hourly7day', 'forecast7day', 'yesterday', 'autocomplete', 'almanac', 'lang']
AUTOCOMPLETE_URL = 'http://autocomplete.wunderground.com/aq?query={query}&format={format}&c={country}&h={hurricanes}&cities={cities}'
API_URL = 'http://api.wunderground.com/api/{key}/{features}/q/{query}.{format}'


def autocomplete(query, country=None, hurricanes=False, cities=True, timeout=5):
    """Make an autocomplete API request

    This can be used to find cities and/or hurricanes by name

    :param string query: city
    :param string country: restrict search to a specific country. Must be a two letter country code
    :param boolean hurricanes: whether to search for hurricanes or not
    :param boolean cities: whether to search for cities or not
    :param integer timeout: timeout of the api request
    :returns: result of the autocomplete API request
    :rtype: dict

    """
    data = {}
    data['query'] = quote(query)
    data['country'] = country or ''
    data['hurricanes'] = 1 if hurricanes else 0
    data['cities'] = 1 if cities else 0
    data['format'] = 'JSON'
    r = requests.get(AUTOCOMPLETE_URL.format(**data), timeout=timeout)
    results = json.loads(r.content)['RESULTS']
    return results


def request(key, features, query, timeout=5):
    """Make an API request

    :param string key: API key to use
    :param list features: features to request. It must be a subset of :data:`FEATURES`
    :param string query: query to send
    :param integer timeout: timeout of the request
    :returns: result of the API request
    :rtype: dict

    """
    data = {}
    data['key'] = key
    data['features'] = '/'.join([f for f in features if f in FEATURES])
    data['query'] = quote(query)
    data['format'] = 'json'
    r = requests.get(API_URL.format(**data), timeout=timeout)
    results = json.loads(_unicode(r.content))
    return results


def _unicode(string):
    """Try to convert a string to unicode using different encodings"""
    fallback = 'utf-8'
    for encoding in ['utf-8', 'latin1']:
        try:
            result = unicode(string, encoding)
            return result
        except UnicodeDecodeError:
            pass
    result = unicode(string, fallback, 'replace')
    return result
