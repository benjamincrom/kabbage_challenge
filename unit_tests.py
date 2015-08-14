#!/usr/bin/python
import requests
import base64

import wikipedia_api_wrapper
import twitter_api_wrapper
import app

WORKING_API_ENDPOINT = 'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=football'
NOT_WORKING_API_ENDPOINT = 'https://en.wikipedia.org/dfjkldsfjkd'
NOT_WORKING_API_ENDPOINT_WITH_ARG = 'https://en.wikipedia.org/dfjkldsfjkd%s'

def test_twitter_get_bearer_token_has_access_token():
    twitter_api_obj = twitter_api_wrapper.TwitterAPIWrapper()
    assert(twitter_api_obj.get_bearer_token())

def test_twitter_get_topic():
    twitter_api_obj = twitter_api_wrapper.TwitterAPIWrapper()
    assert(
        len(twitter_api_obj.get_topic('football')) > 0
    )

def test_twitter_extract_response_dict_with_200():
    response = requests.get(WORKING_API_ENDPOINT)
    twitter_api_obj = twitter_api_wrapper.TwitterAPIWrapper()
    assert(
        len(twitter_api_obj.extract_response_dict(response).keys()) > 0
    )

def test_twitter_extract_response_dict_with_400():
    response = requests.get(NOT_WORKING_API_ENDPOINT)
    twitter_api_obj = twitter_api_wrapper.TwitterAPIWrapper()
    assert(
        twitter_api_obj.extract_response_dict(response) is None
    )

def test_twitter_get_bearer_token_no_access_token():
    twitter_api_obj = twitter_api_wrapper.TwitterAPIWrapper()
    twitter_api_wrapper.TwitterAPIWrapper.BASE64_API_KEY = base64.b64encode('yaaaaaaaaay')
    assert(twitter_api_obj.get_bearer_token() == None)

def test_wikipedia_get_topic_with_200():
    assert(
        len(wikipedia_api_wrapper.get_topic('football')) > 0
    )

def test_wikipedia_get_topic_with_400():
    wikipedia_api_wrapper.WIKIPEDIA_SEARCH_API = NOT_WORKING_API_ENDPOINT_WITH_ARG
    assert(
        len(wikipedia_api_wrapper.get_topic('football')) == 0
    )
    