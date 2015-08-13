from flask import Flask

app = Flask(__name__)

TWITTER_KEY = 'hhoGSNh6JkursHppu74AGnK5r:i7lLGpPSX1KESNNiAJgikHGuUsrZZaR0dRF9SvSTECxon7aPX6'
TWITTER_KEY_BASE64 = TWITTER_KEY.encode('base64')

@app.route('/')
def hello():
    return "Hello World!"

def twitter_bearer_token():



if __name__ == '__main__':
    app.run()
