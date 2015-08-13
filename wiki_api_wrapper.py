#!/usr/bin/python
"""
wiki_api_wrapper.py -- Wrapper for Wikipedia API
"""
import json
import logging
import requests

LOGFILE = '/home/bcrom/twitter_api.log'
logging.basicConfig(filename=LOGFILE, level=logging.DEBUG)


class WikiAPIWrapper(object):
    """ Return results from Wikipedia text search. """
    WIKIPEDIA_SEARCH_API = 'https://en.wikipedia.org/w/api.php?action=query&list=search&prop=info&format=json&srsearch=%s&generator=search&gsrsearch=%s'

    @classmethod
    def get_topic(cls, search_string):
        """ Perform a Wikipedia search given a search string. """
        response = requests.get(
            cls.WIKIPEDIA_SEARCH_API % (search_string, search_string)
        )

        if response.status_code == 200:
            response_dict = json.loads(response.text)
        else:
            response_dict = None

        return response_dict
