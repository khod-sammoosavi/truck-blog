import os
from home import Home
from admin import Admin
from flask import Flask
from main import BASE_DIR
from .configs import Development

static_dir = os.path.join(BASE_DIR, "static")
template_dir = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir,
            instance_relative_config=True, instance_path=BASE_DIR)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_pyfile("settings", silent=True)
app.config["SQLALCHEMY_DATABASE_URI"] = Development.SQLALCHEMY_DATABASE_URI

from settings import database

app.register_blueprint(Home)
app.register_blueprint(Admin)
