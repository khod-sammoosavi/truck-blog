import os
from settings import wsgi

BASE_DIR = os.path.join(os.path.dirname(__file__))

from settings.configs import Development

if __name__ == "__main__":
    wsgi.app.run(host=Development.HOST,
                 port=Development.PORT,
                 debug=Development.DEBUG)
