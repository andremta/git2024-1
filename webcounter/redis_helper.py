import redis
import time

from os import environ

# Request redis url from environment variable
if "REDIS_URL" in environ:
    __redis_url__ = environ["REDIS_URL"]
else:
    __redis_url__ = 'localhost'

# Create a redis cache
print('Starting redis helper')
cache = redis.Redis(host=__redis_url__, port=6379)


def get_hits_count():
    """ Get and increment cache on redis """
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


if __name__ == '__main__':  # pragma: no cover, don't test main
    for _ in range(10):
        print(get_hits_count())
