import logging
from flight_tweeter import flight_tweeter
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World'
    
@app.route('/test')
def test_tweet():
    """Return test tweet."""
    bot = flight_tweeter()
    msg = bot.tweet_tester()
    return msg
    
@app.route('/flightBot')
def send_tweet():
    """Return tweet."""
    bot = flight_tweeter()
    msg = bot.tweet_cheapest()
    return msg


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
