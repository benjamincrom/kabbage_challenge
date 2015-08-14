#!/usr/bin/python
"""
wikipedia_api_wrapper.py -- Module to contain method which searches Wikipedia
                            via its api
"""
import json
import requests
import logging

LOGFILE = 'topics-bcrom.log'
logging.basicConfig(filename=LOGFILE, level=logging.DEBUG)

WIKIPEDIA_SEARCH_API = 'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=%s'
WIKIPEDIA_TITLE_URI = 'https://en.wikipedia.org/wiki/%s'

def get_topic(search_string):
    """
    Return list of wikipedia pages with the snippet of this search string.
    """
    return_dict_list = []
    try:
        response = requests.get(WIKIPEDIA_SEARCH_API % search_string)
    except Exception as e:
        logging.warning('Could not connect to API: %s', e)
        response = None

    if response and response.status_code == 200:
        response_dict = json.loads(response.text)
        for search_obj in response_dict['query']['search']:
            return_dict_list.append(
                {
                    'title': search_obj['title'],
                    'snippet': search_obj['snippet'],
                    'wiki_url': WIKIPEDIA_TITLE_URI % search_obj['title']
                }
            )
    else:
        logging.warning('Wikipedia API did not return 200 response code.')

    return return_dict_list
