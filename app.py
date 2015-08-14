import wikipedia_api_wrapper

from flask import Flask, render_template, request
from twitter_api_wrapper import TwitterAPIWrapper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """ Return search page for tweets and wikipedia entries by keyword. """
    tweet_dict_list = []
    wikipedia_dict_list = []

    if 'search' in request.args and request.args['search'] != '':
        search_string = request.args.get('search')
        twitter_api_obj = TwitterAPIWrapper()
        tweet_dict_list = twitter_api_obj.get_topic(search_string)
        wikipedia_dict_list = wikipedia_api_wrapper.get_topic(search_string)

    return render_template('index.html',
                           tweet_dict_list=tweet_dict_list,
                           wikipedia_dict_list=wikipedia_dict_list)

if __name__ == '__main__':
    app.run()
