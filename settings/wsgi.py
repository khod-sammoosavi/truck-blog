import os
from flask import Flask
from home import Home
from main import BASE_DIR

template_dir = os.path.join(BASE_DIR, "templates")
static_dir = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.config.from_pyfile("settings", silent=True)

app.register_blueprint(Home)
