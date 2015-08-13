#!/usr/bin/python
"""
twitter_api_wrapper.py -- contains class used to interact with the Twitter API
"""
import base64
import logging
import json
import requests

LOGFILE = '/home/bcrom/twitter_api.log'
logging.basicConfig(filename=LOGFILE, level=logging.DEBUG)


class TwitterAPIWrapper(object):
    """
    TwitterAPIWrapper holds an API bearer token and returns twitter API searches
    """
    API_KEY = 'hhoGSNh6JkursHppu74AGnK5r:i7lLGpPSX1KESNNiAJgikHGuUsrZZaR0dRF9SvSTECxon7aPX6'
    BASE64_API_KEY = base64.b64encode(API_KEY)
    TWITTER_TOKEN_API = 'https://api.twitter.com/oauth2/token'
    TWITTER_SEARCH_API = 'https://api.twitter.com/1.1/search/tweets.json?q=%s'
    DEFAULT_CONTENT_TYPE = 'application/x-www-form-urlencoded;charset=UTF-8'
    TWITTER_API_HOST = 'api.twitter.com'
    TOKEN_REQUEST_PAYLOAD = 'grant_type=client_credentials'

    def __init__(self):
        self.bearer_token = self.get_bearer_token()

    @classmethod
    def get_bearer_token(cls):
        """ Return bearer token from Twitter API using appliation API key. """
        request_headers = {
            'Authorization': 'Basic %s' % cls.BASE64_API_KEY,
            'Content-Type': cls.DEFAULT_CONTENT_TYPE,
            'Host': cls.TWITTER_API_HOST,

        }

        response = requests.post(cls.TWITTER_TOKEN_API,
                                 headers=request_headers,
                                 data=cls.TOKEN_REQUEST_PAYLOAD)

        bearer_token = None
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            if 'access_token' in response_dict:
                bearer_token = response_dict['access_token']
            else:
                logging.warning("Access token is not present in response from "
                                "Twitter's bearer token API: %s", response.text)
        else:
            logging.warning('Twitter token API did not return a 200 HTTP code '
                            'when asked for a bearer token: %s', response.text)

        return bearer_token

    def get_topic(self, search_string):
        """ Perform a Twitter search given a search string and access token. """
        headers = {
            'Authorization': 'Bearer %s' % self.bearer_token,
            'Content-Type': self.DEFAULT_CONTENT_TYPE,
            'Host': self.TWITTER_API_HOST,
        }

        response = requests.get(self.TWITTER_SEARCH_API % search_string,
                                headers=headers)

        if response.status_code == 200:
            response_dict = json.loads(response.text)
        else:
            logging.warning('Twitter token API did not return a 200 HTTP code '
                            'when asked for a bearer token: %s', response.text)
            response_dict = None

        return response_dict
