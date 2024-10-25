""" Simple webcounter app """
from os import environ

import sys

# Verify minimum Python version
if sys.version_info[:2] < (3, 8):
    print('Error: Minimum python version 3.8. Aborting!')
    sys.exit(1)

# Request git HASH from environment variable
if "CI_COMMIT_SHORT_SHA" in environ:
    __version__ = environ["CI_COMMIT_SHORT_SHA"]
else:
    __version__ = "develop"
