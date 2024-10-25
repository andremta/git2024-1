from flask import Flask, render_template
from waitress import serve


from webcounter import __version__
from webcounter import redis_helper as redis


# Create a Flask APP
app = Flask(__name__)


@app.route('/')
def index():
    """ Default page"""
    try:
        hits = redis.get_hits_count()
    except Exception as ex:
        return f'{ex}'
    return render_template('index.html', version=__version__, hits=hits)


if __name__ == '__main__':  # pragma: no cover, don't test main
    print(f'Starting webcounter v:{__version__}')
    serve(app, host='0.0.0.0', port=5000)
