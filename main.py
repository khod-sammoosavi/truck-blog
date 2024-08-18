import os
from settings import wsgi

BASE_DIR = os.path.join(os.path.dirname(__file__))

if __name__ == "__main__":
    wsgi.app.run(host="0.0.0.0", port="5000", debug=True, load_dotenv=True)
