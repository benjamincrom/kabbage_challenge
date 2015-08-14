import wikipedia

from flask import Flask, render_template
from twitter_api_wrapper import TwitterAPIWrapper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    twitter_api = TwitterAPIWrapper()
    tweet_dict_list = twitter_api.get_topic('football')

    wikipedia_list = wikipedia.search('football', results=15)
    wikipedia_dict_list = []
    for entry in wikipedia_list:
        wikipedia_dict_list.append(
            {
                'title': entry,
                'summary': wikipedia.summary(entry, sentences=1),
            }
        )
    return render_template(
        'index.html',
        tweet_dict_list=tweet_dict_list,
        wikipedia_dict_list=wikipedia_dict_list
    )

if __name__ == '__main__':
    app.run()
