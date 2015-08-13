#!/usr/bin/python
"""
twitter_api.py -- contains methods useful for interacting with the Twitter API 
"""
import base64
import logging
import json
import requests

API_KEY = 'hhoGSNh6JkursHppu74AGnK5r:i7lLGpPSX1KESNNiAJgikHGuUsrZZaR0dRF9SvSTECxon7aPX6'
BASE64_API_KEY = base64.b64encode(API_KEY)
TWITTER_TOKEN_API = 'https://api.twitter.com/oauth2/token'
TWITTER_SEARCH_API = 'https://api.twitter.com/1.1/search/tweets.json?q=%s'
DEFAULT_CONTENT_TYPE = 'application/x-www-form-urlencoded;charset=UTF-8'
TWITTER_API_HOST = 'api.twitter.com'
TOKEN_REQUEST_PAYLOAD = 'grant_type=client_credentials'

LOGFILE = '/home/bcrom/twitter_api.log'
logging.basicConfig(filename=LOGFILE, level=logging.DEBUG)

def get_topic(search_string, access_token):
    """ Perform a Twitter search given a search string and access token. """
    headers = {
        'Authorization': 'Bearer %s' % access_token,
        'Content-Type': DEFAULT_CONTENT_TYPE,
        'Host': TWITTER_API_HOST,
    }

    response = requests.get(TWITTER_SEARCH_API % search_string, headers=headers)

    if response.status_code == 200:
        response_dict = json.loads(response.text)
    else:
        logging.warning('Twitter token API did not return a 200 HTTP code when '
                        'asked for a bearer token.')
        response_dict = None

    return response_dict

def get_bearer_token():
    """ Return bearer token from Twitter API using appliation API key. """
    request_headers = {
        'Authorization': 'Basic %s' % BASE64_API_KEY,
        'Content-Type': DEFAULT_CONTENT_TYPE,
        'Host': TWITTER_API_HOST,

    }

    response = requests.post(TWITTER_TOKEN_API,
                             headers=request_headers,
                             data=TOKEN_REQUEST_PAYLOAD)

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        if 'access_token' in response_dict:
            bearer_token = response_dict['access_token']
        else:
            raise KeyError('Access token is not present in response from '
                           "Twitter's bearer token API.")
    else:
        raise Exception('Twitter token API did not return a 200 HTTP code '
                        'when asked for a bearer token.')


    return bearer_token
