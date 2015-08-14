import wikipedia

from flask import Flask, render_template, request
from twitter_api_wrapper import TwitterAPIWrapper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tweet_dict_list = []
    wikipedia_dict_list = []

    import pdb
    pdb.set_trace()
    if 'search' in request.args:
        search_string = request.args.get('search')

        twitter_api = TwitterAPIWrapper()
        tweet_dict_list = twitter_api.get_topic(search_string)

        wikipedia_list = wikipedia.search(search_string, results=20)
        wikipedia_dict_list = []

        for entry in wikipedia_list:
            try:
                summary = wikipedia.summary(entry, sentences=1)
            except wikipedia.exceptions.DisambiguationError as e:
                summary = str(e.options[0])

            wikipedia_dict_list.append(
                {
                    'title': entry,
                    'summary': summary,
                }
            )

    return render_template(
        'index.html',
        tweet_dict_list=tweet_dict_list,
        wikipedia_dict_list=wikipedia_dict_list
    )

if __name__ == '__main__':
    app.run()
