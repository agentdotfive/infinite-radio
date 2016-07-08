
import os
import json

from .api import *  # noqa
from .google_metagraph import GoogleMetagraph  # noqa

__version__ = "1.0.0-pre"

#
# Find any Git info the build system left for us
#

_git_info_filename = os.path.join(os.path.dirname(__file__),
                                  '__git__.json')

if os.path.exists(_git_info_filename):
    with open(_git_info_filename) as git_info_file:
        __git__ = json.load(git_info_file)
else:
    __git__ = None
