import os
from main import BASE_DIR
from flask import Flask
from home import Home
from admin import Admin

template_dir = os.path.join(BASE_DIR, "templates")
static_dir = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.config.from_pyfile("settings", silent=True)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(Home)
app.register_blueprint(Admin)
